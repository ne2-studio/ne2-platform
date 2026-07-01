# 3. Platform Overview

## 3.1 Overview

The Ne2 Platform is a self-hosted application platform built on a single Virtual Private Server (VPS).

Applications are developed locally, versioned in GitHub, built and tested through GitHub Actions, packaged as Docker images and deployed automatically through Coolify — a consistent deployment and operational model regardless of the technology stack used by individual applications.

At a high level, the platform consists of:

* A VPS that hosts all workloads.
* Coolify as the deployment platform.
* GitHub as source control and GitHub Actions as the CI/CD system.
* GitHub Container Registry (GHCR) as the image registry.
* Cloudflare as CDN and DNS provider.
* PostgreSQL as the primary database platform.
* Supporting services for identity, observability and automation.

---

## 3.2 High-Level Architecture

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions (build, test, package)
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

Applications are exposed to the internet through Cloudflare and routed internally by Coolify. See [Deployment Pipeline Overview](05-deployment.md#52-deployment-pipeline-overview) for the detailed CI/CD workflow.

---

## 3.3 Core Infrastructure

### VPS

The VPS is the physical foundation of the platform: a single Linux host that runs all application and platform containers and provides storage, CPU and memory resources. The platform currently prioritizes simplicity and cost-efficiency over infrastructure redundancy.

### Coolify

Coolify is the platform-as-a-service layer: a simplified operational model on top of Docker responsible for deployments, reverse proxy configuration, SSL certificate provisioning, environment variable management and application lifecycle management. It is the central operational component of the platform — see [Deployment Execution](05-deployment.md#deployment-execution) for how it performs a deployment.

### Docker

Docker is the universal deployment standard: every application and service is distributed as a container image, which standardizes runtime environments and isolates workloads. See [Docker is the Universal Deployment Unit](02-principles.md#24-docker-is-the-universal-deployment-unit).

---

## 3.4 Source Control and Delivery

### GitHub

GitHub is the system of record for source code: version control, pull requests, code review and collaboration. All platform applications are versioned in Git repositories.

### GitHub Actions

GitHub Actions is the standard CI/CD system, responsible for building, testing, packaging and publishing Docker images and triggering deployments. See [Continuous Integration](05-deployment.md#53-continuous-integration) for pipeline details.

### GitHub Container Registry

GHCR stores all deployable artifacts and is the deployment source Coolify pulls from. Applications are deployed from container images, never directly from source. See [Container Registry](05-deployment.md#54-container-registry).

---

## 3.5 Networking

### Cloudflare

Cloudflare is the external edge of the platform, providing DNS management, CDN, TLS termination and basic protection against malicious traffic. It reduces load on the origin server while improving global content delivery.

### Internal Routing

Internal application routing is handled by Coolify through Traefik: host-based routing, SSL certificate provisioning and traffic forwarding. Applications are not responsible for managing their own ingress infrastructure.

---

## 3.6 Data Layer

### PostgreSQL

PostgreSQL is the primary persistence technology, currently run as a shared instance with applications isolated through dedicated users and schemas. See [Data Access Standards](04-application-architecture.md#46-data-access-standards) for schema ownership and migration rules.

---

## 3.7 Identity Layer

### Zitadel

The platform uses Zitadel as its centralized Identity Provider (IdP), handling authentication, SSO, OAuth 2.0 / OpenID Connect flows and user and organization management.

Authentication is a platform capability, not an application concern: applications trust the identity claims Zitadel provides and focus exclusively on application-level authorization — see [Authentication and Authorization](04-application-architecture.md#47-authentication-and-authorization).

---

## 3.8 Observability Layer

The platform distinguishes between infrastructure observability and application observability.

### Infrastructure Observability

Beszel monitors the health and resource consumption of the underlying platform — CPU, memory, disk, network and container resource usage — to answer operational questions such as:

* Is the server healthy?
* Is a container consuming abnormal resources?
* Do we have capacity to deploy additional applications?
* Is a particular service under heavy load?

Beszel provides visibility into the platform itself, not into individual application behaviour.

### Application Observability

Seq is the centralized log management and diagnostics platform for all applications, and the primary source of truth when diagnosing application-level problems: investigating errors, understanding behaviour and following business workflows. See [Logging Standards](04-application-architecture.md#48-logging-standards) for what applications must log and how.

---

## 3.9 Automation Layer

### n8n

n8n provides workflow automation: process automation, third-party integrations, scheduled jobs, AI agents and event-driven workflows. Not every business problem requires a custom application; when automation alone is sufficient, workflows are preferred over building new software.

---

## 3.10 Platform Boundaries

The platform is responsible for infrastructure, deployments, networking, data services, identity services, observability and automation.

Individual applications remain responsible for business logic, domain models, user experience, product-specific requirements and application-level authorization rules.

This separation allows platform concerns to evolve independently from application concerns while maintaining a consistent operational model across all products.
