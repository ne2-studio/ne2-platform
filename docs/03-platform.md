# 3. Platform Overview

## 3.1 Overview

The Ne2 Platform is a self-hosted application platform built on top of a single Virtual Private Server (VPS).

Applications are developed locally, versioned in GitHub, built and tested through GitHub Actions, packaged as Docker images and deployed automatically through Coolify.

The platform provides a consistent deployment and operational model regardless of the technology stack used by individual applications.

At a high level, the platform consists of:

* A VPS that hosts all workloads.
* Coolify as the deployment platform.
* GitHub as source control.
* GitHub Actions as the CI/CD system.
* GitHub Container Registry (GHCR) as the image registry.
* Cloudflare as CDN and DNS provider.
* PostgreSQL as the primary database platform.
* Supporting services such as identity providers, observability tooling and automation platforms.

The result is a lightweight platform that enables applications to move from source code to production with minimal operational overhead.

---

## 3.2 High-Level Architecture

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Run Tests
    ├── Build Application
    └── Build Docker Image
            │
            ▼
GitHub Container Registry (GHCR)
            │
            ▼
Coolify Deployment
            │
            ▼
Application Containers
            │
            ├── PostgreSQL
            ├── Identity Provider
            ├── n8n
            ├── Monitoring
            └── Other Services
```

Applications are exposed to the internet through Cloudflare and routed internally by Coolify.

---

## 3.3 Core Infrastructure

### VPS

The VPS is the physical foundation of the platform.

All platform services and applications ultimately run on a single Linux host.

Responsibilities:

* Host application containers.
* Host platform services.
* Provide storage, CPU and memory resources.
* Serve as the operational boundary of the platform.

The platform currently prioritizes simplicity and cost-efficiency over infrastructure redundancy.

---

### Coolify

Coolify acts as the Platform-as-a-Service layer.

It provides a simplified operational model on top of Docker.

Responsibilities:

* Application deployments.
* Service deployments.
* Reverse proxy configuration.
* SSL certificate provisioning.
* Environment variable management.
* Application lifecycle management.

Coolify is considered the central operational component of the platform.

Every deployable workload should be managed through Coolify whenever possible.

---

### Docker

Docker is the universal deployment standard of the platform.

Every application and service is expected to be distributed as a container image.

Responsibilities:

* Packaging applications.
* Standardizing runtime environments.
* Isolating workloads.
* Simplifying deployments.

If a workload can run inside a Docker container, it can run on the platform.

---

## 3.4 Source Control and Delivery

### GitHub

GitHub is the system of record for source code.

Responsibilities:

* Source control.
* Pull requests.
* Code reviews.
* Project visibility.
* Collaboration.

All platform applications are expected to be versioned in Git repositories.

---

### GitHub Actions

GitHub Actions is the standard CI/CD system.

Responsibilities:

* Building applications.
* Running automated tests.
* Building Docker images.
* Publishing images.
* Triggering deployments.

Applications should be deployable through automated pipelines without requiring manual intervention.

---

### GitHub Container Registry

GitHub Container Registry (GHCR) stores all deployable artifacts.

Responsibilities:

* Hosting Docker images.
* Version distribution.
* Deployment source for Coolify.

Applications are deployed from container images, never directly from source code.

---

## 3.5 Networking

### Cloudflare

Cloudflare acts as the external edge of the platform.

Responsibilities:

* DNS management.
* CDN capabilities.
* TLS termination.
* Traffic acceleration.
* Basic protection against malicious traffic.

Cloudflare reduces the load on the origin server while improving global content delivery.

---

### Internal Routing

Internal application routing is handled by Coolify through Traefik.

Responsibilities:

* Host-based routing.
* SSL certificate provisioning.
* Traffic forwarding.
* Service exposure.

Applications are not responsible for managing their own ingress infrastructure.

---

## 3.6 Data Layer

### PostgreSQL

PostgreSQL is the primary persistence technology used by the platform.

Responsibilities:

* Transactional data storage.
* Application persistence.
* Reporting and operational data.

The platform currently uses a shared PostgreSQL instance.

Individual applications are isolated through dedicated users and schemas.

---

## 3.7 Identity Layer

### Zitadel

The platform uses Zitadel as its centralized Identity Provider (IdP).

Responsibilities:

* User registration and account management.
* Authentication.
* Single Sign-On (SSO).
* OAuth 2.0 and OpenID Connect flows.
* Access token issuance.
* User and organization management.
* Identity federation.

Applications should delegate authentication concerns to Zitadel rather than implementing their own authentication systems.

Authentication is considered a platform capability, not an application concern.

Applications are expected to trust the identity claims provided by Zitadel and focus exclusively on application-level authorization.

---

## 3.8 Observability Layer

The platform distinguishes between infrastructure observability and application observability.

---

### Infrastructure Observability

Infrastructure observability is provided by Beszel.

Beszel is responsible for monitoring the health and resource consumption of the underlying platform.

Responsibilities:

* CPU monitoring.
* Memory monitoring.
* Disk usage monitoring.
* Network monitoring.
* Container resource monitoring.
* Capacity planning.

The primary purpose of Beszel is to answer operational questions such as:

* Is the server healthy?
* Is a container consuming abnormal resources?
* Do we have capacity to deploy additional applications?
* Is a particular service under heavy load?

Beszel provides visibility into the platform itself, not into the behaviour of individual applications.

---

### Application Observability

Application observability is provided by Seq.

Seq acts as the centralized log management and diagnostics platform for all applications running on the Ne2 Platform.

Responsibilities:

* Structured log ingestion.
* Log storage.
* Log search.
* Log filtering.
* Application diagnostics.
* Error investigation.

Applications are expected to emit structured logs in JSON format.

Logs should be written to standard output and collected by the platform, or sent directly to Seq depending on the deployment model.

The platform standardizes on structured logging rather than text-based logs to enable efficient querying and diagnostics.

Typical use cases include:

* Investigating application errors.
* Understanding application behaviour.
* Troubleshooting production issues.
* Following business workflows.
* Monitoring operational events.

Seq is considered the primary source of truth when diagnosing application-level problems.

---

### Logging Standards

All applications running on the platform should:

* Produce structured JSON logs.
* Include log levels.
* Include timestamps.
* Include correlation identifiers when available.
* Avoid logging sensitive information.
* Write meaningful, actionable log messages.

Logs are treated as a first-class operational capability and should be considered part of the application's public operational interface.

---

## 3.9 Automation Layer

### n8n

n8n provides workflow automation capabilities.

Responsibilities:

* Process automation.
* Third-party integrations.
* Scheduled jobs.
* AI agents.
* Event-driven workflows.

Not every business problem requires a custom application.

When automation alone is sufficient, workflows should be preferred over building new software.

---

## 3.10 Platform Boundaries

The platform provides a standardized environment for deploying and operating applications.

The platform is responsible for:

* Infrastructure.
* Deployments.
* Networking.
* Data services.
* Identity services.
* Observability.
* Automation capabilities.

Individual applications remain responsible for:

* Business logic.
* Domain models.
* User experience.
* Product-specific requirements.
* Application-level authorization rules.

This separation allows platform concerns to evolve independently from application concerns while maintaining a consistent operational model across all products.
