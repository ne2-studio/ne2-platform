# 4. Application Architecture Standards

## 4.1 Purpose

This document defines the architectural standards every application deployed on the Ne2 Platform is expected to follow.

The goal is not identical implementations across projects, but a consistent operational model that simplifies development, deployment and maintenance. Applications are free to choose different implementation technologies when justified, but must conform to the standards described here.

---

## 4.2 Supported Application Types

The platform currently supports three application categories.

### Static Websites

Used for marketing sites, landing pages, documentation portals and product websites. Default stack: **Hugo, Nginx, Docker**. Static websites should not require a database or server-side logic — whenever a website can be static, it should be.

### Single Page Applications (SPA)

Used for product frontends, internal tools, dashboards and administrative interfaces. Default stack: **React, Vite, TypeScript** ([ADR-0007](../adrs/0007-react-as-default-frontend.md)). Alternative frontend technologies may be used when justified. SPAs are built as static assets and served through a lightweight web server.

### Backend APIs

Contain application business logic. Default stack: **ASP.NET, PostgreSQL, Docker** ([ADR-0008](../adrs/0008-aspnet-as-default-backend.md)). Alternative backend technologies are permitted — see [Technology Freedom](01-goals.md#technology-freedom). Backend applications should expose HTTP APIs and follow standard web application practices.

---

## 4.3 Docker-First Architecture

Every deployable component must be packaged as a Docker image and be runnable locally through Docker before being deployed to production (see [Docker is the Universal Deployment Unit](02-principles.md#24-docker-is-the-universal-deployment-unit)). This guarantees consistent environments, predictable deployments and technology independence.

---

## 4.4 Twelve-Factor Applications

Applications should follow the [Twelve-Factor App](https://12factor.net/) methodology whenever practical. The following principles are mandatory.

### Codebase

Each application must have a single authoritative source repository.

### Dependencies

Dependencies must be declared explicitly; applications should not depend on software manually installed on servers.

### Configuration

Configuration must live outside the codebase and never be hardcoded — see [Configuration Standards](#45-configuration-standards).

### Backing Services

Databases, queues, storage providers and external services are treated as attached resources; applications should be able to switch providers through configuration.

### Build, Release and Run

Build, release and execution are clearly separated stages. Applications are deployable from immutable Docker images.

### Processes

Applications should be stateless whenever possible; persistent state belongs in backing services.

### Logs

Applications write logs to standard output and do not manage log files directly; the observability layer is responsible for collection and retention (see [Logging Standards](#48-logging-standards)).

---

## 4.5 Configuration Standards

### Environment Variables

Application configuration must be provided through environment variables, never stored in source code. Examples:

```text
DATABASE_CONNECTION_STRING
ASPNETCORE_ENVIRONMENT
ZITADEL_AUTHORITY
ZITADEL_CLIENT_ID
PUBLIC_API_URL
```

### Secrets

Secrets (API keys, database passwords, access tokens, signing certificates) must never be committed to Git repositories. They are managed through Coolify environment variables — see [Secrets Management](05-deployment.md#secrets-management) for how they're injected at deploy time.

### Environment Separation

Applications should support different environments (typically local and production) through configuration rather than code changes. Additional environments may be introduced when required.

---

## 4.6 Data Access Standards

### PostgreSQL

PostgreSQL is the default persistence technology; applications should use it unless there is a strong justification for an alternative datastore.

### Schema Ownership

Each application owns its own schema and must never directly manipulate data owned by another application ([ADR-0003](../adrs/0003-shared-postgresql-instance.md)). Cross-application integrations occur through APIs or events.

### Migrations

Schema changes must be versioned through migrations rather than manual database changes. For ASP.NET applications, Entity Framework migrations are the default mechanism — see [Database Deployment](05-deployment.md#59-database-deployment) for how migrations run during deployment.

---

## 4.7 Authentication and Authorization

### Authentication

Authentication is delegated to Zitadel (see [Identity Layer](03-platform.md#37-identity-layer)). Applications trust identity claims provided by the platform and must not implement custom username/password systems.

### Authorization

Authorization remains an application concern: roles, permissions, ownership rules and business-specific access policies.

---

## 4.8 Logging Standards

Applications must emit structured logs with, at minimum, a timestamp, log level, message and context information — this enables effective querying and diagnostics through [Seq](03-platform.md#38-observability-layer).

### Log Levels

* **Debug** — diagnostic information useful during development.
* **Information** — normal business and operational events.
* **Warning** — unexpected situations that do not prevent execution.
* **Error** — failures affecting application behaviour.
* **Critical** — failures requiring immediate attention.

### Sensitive Data

Applications must not log passwords, access tokens, secrets, or personal information unless strictly necessary.

---

## 4.9 Health Checks

Applications should expose a lightweight, fast health endpoint (e.g. `/health`) that verifies application startup status, database connectivity and critical dependencies.

---

## 4.10 Testing Standards

Automated testing is required; the exact strategy may vary by application but typically includes unit, integration and end-to-end tests. All tests must execute as part of the CI pipeline, and applications should not be deployable when tests fail.

---

## 4.11 Repository Standards

Every application repository should contain:

```text
README.md
Dockerfile
.github/workflows/
src/
tests/
```

Repositories should be self-contained and executable by a new developer with minimal setup effort.

---

## 4.12 Definition of Done

An application is production-ready when:

* Source code is versioned in Git.
* Automated tests exist and the CI pipeline passes.
* The application is containerized and configuration is externalized.
* Authentication is delegated to Zitadel.
* Structured logging and health checks are implemented.
* Database migrations are versioned.
* Deployment can be performed automatically through the platform.

Applications that do not satisfy these requirements are considered incomplete regardless of functional status.
