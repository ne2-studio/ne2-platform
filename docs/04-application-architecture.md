# 4. Application Architecture Standards

## 4.1 Purpose

This document defines the architectural standards that every application deployed on the Ne2 Platform is expected to follow.

The goal is not to enforce identical implementations across all projects, but rather to establish a consistent operational model that simplifies development, deployment and maintenance.

Applications are free to choose different implementation technologies when justified. However, they should conform to the platform standards described in this document.

---

## 4.2 Supported Application Types

The platform currently supports three primary application categories.

### Static Websites

Static websites are used for:

* Marketing websites.
* Landing pages.
* Documentation portals.
* Personal websites.
* Product websites.

The default technology stack is:

* Hugo
* Nginx
* Docker

Static websites should not require a database or server-side application logic.

Whenever a website can be implemented as static content, it should be.

---

### Single Page Applications (SPA)

Single Page Applications are used for:

* Product frontends.
* Internal tools.
* Dashboards.
* Administrative interfaces.

The default technology stack is:

* React
* Vite
* TypeScript

Alternative frontend technologies may be used when justified.

All SPA applications are expected to be built as static assets and served through a lightweight web server.

---

### Backend APIs

Backend APIs contain application business logic.

The default technology stack is:

* ASP.NET
* PostgreSQL
* Docker

Alternative backend technologies are permitted.

The platform standardizes deployment and operations, not programming languages.

Backend applications should expose HTTP APIs and follow standard web application practices.

---

## 4.3 Docker-First Architecture

Every deployable component must be packaged as a Docker image.

Docker images are the only deployment artifact supported by the platform.

Applications must be runnable locally through Docker before being deployed to production.

Benefits:

* Consistent environments.
* Predictable deployments.
* Technology independence.
* Simplified operations.

If an application cannot be containerized, it is not compatible with the platform.

---

## 4.4 Twelve-Factor Applications

Applications should follow the principles described in the Twelve-Factor App methodology whenever practical.

The following principles are considered mandatory.

### Codebase

Each application must have a single authoritative source repository.

---

### Dependencies

Dependencies must be declared explicitly.

Applications should not depend on software manually installed on servers.

---

### Configuration

Configuration must live outside the codebase.

Environment-specific settings must be injected through environment variables.

Configuration should never be hardcoded.

---

### Backing Services

Applications should treat databases, queues, storage providers and external services as attached resources.

Applications should be able to switch providers through configuration.

---

### Build, Release and Run

Build, release and execution should be clearly separated stages.

Applications should be deployable from immutable Docker images.

---

### Processes

Applications should be stateless whenever possible.

Persistent state belongs in backing services.

---

### Logs

Applications should write logs to standard output.

Applications should not manage log files directly.

The observability layer is responsible for log collection and retention.

---

## 4.5 Configuration Standards

### Environment Variables

Application configuration must be provided through environment variables.

Examples:

```text
DATABASE_CONNECTION_STRING
ZITADEL_AUTHORITY
ZITADEL_CLIENT_ID
PUBLIC_API_URL
```

Configuration should never be stored inside source code.

---

### Secrets

Secrets must not be committed to Git repositories.

Examples:

* API keys.
* Database passwords.
* Access tokens.
* Signing certificates.

Secrets should be managed through Coolify environment variables.

---

### Environment Separation

Applications should support different environments through configuration rather than code changes.

Typical environments include:

* Local
* Production

Additional environments may be introduced when required.

---

## 4.6 Data Access Standards

### PostgreSQL

PostgreSQL is the default persistence technology.

Applications should use PostgreSQL unless a strong justification exists for an alternative datastore.

---

### Schema Ownership

Each application owns its own schema.

Applications must never directly manipulate data owned by another application.

Cross-application integrations should occur through APIs or events.

---

### Migrations

Database schema changes must be versioned.

Schema modifications should be performed through migrations rather than manual database changes.

For ASP.NET applications, Entity Framework migrations are the default mechanism.

---

## 4.7 Authentication and Authorization

### Authentication

Authentication is delegated to Zitadel.

Applications should trust identity claims provided by the platform.

Applications must not implement custom username/password systems.

---

### Authorization

Authorization remains an application concern.

Each application is responsible for:

* Roles.
* Permissions.
* Ownership rules.
* Business-specific access policies.

---

## 4.8 Logging Standards

Applications must emit structured logs.

Minimum requirements:

* Timestamp.
* Log level.
* Message.
* Context information.

Structured logging enables effective querying and diagnostics through Seq.

---

### Log Levels

Applications should use log levels consistently.

#### Debug

Diagnostic information useful during development.

#### Information

Normal business and operational events.

#### Warning

Unexpected situations that do not prevent execution.

#### Error

Failures affecting application behaviour.

#### Critical

Failures requiring immediate attention.

---

### Sensitive Data

Applications must not log:

* Passwords.
* Access tokens.
* Secrets.
* Personal information unless strictly necessary.

---

## 4.9 Health Checks

Applications should expose health endpoints.

Example:

```text
/health
```

Health checks should verify:

* Application startup status.
* Database connectivity.
* Critical dependencies.

Health checks should remain lightweight and fast.

---

## 4.10 Testing Standards

Automated testing is required.

The exact testing strategy may vary by application.

Recommended layers include:

* Unit tests.
* Integration tests.
* End-to-end tests.

All automated tests must execute as part of the CI pipeline.

Applications should not be deployable when tests fail.

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

An application is considered production-ready when:

* Source code is versioned in Git.
* Automated tests exist.
* CI pipeline passes.
* Application is containerized.
* Configuration is externalized.
* Authentication is delegated to Zitadel.
* Structured logging is implemented.
* Health checks are available.
* Database migrations are versioned.
* Deployment can be performed automatically through the platform.

Applications that do not satisfy these requirements are considered incomplete regardless of their functional status.
