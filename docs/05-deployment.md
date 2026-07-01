# 5. Deployment Model

## 5.1 Purpose

This document defines how applications are built, tested, packaged and deployed within the Ne2 Platform. The deployment model is designed around fully automated deployments, repeatable builds, immutable artifacts, minimal operational overhead, fast feedback cycles and forward-only evolution (see [Architecture Principles](02-principles.md)). Every application deployed on the platform is expected to follow this model.

---

## 5.2 Deployment Pipeline Overview

```text id="deployflow"
Developer
    │
    ▼
Git Commit
    │
    ▼
GitHub Actions
    │
    ├── Build
    ├── Test
    ├── Package
    └── Publish Image
    │
    ▼
GHCR
    │
    ▼
Coolify Deployment
    │
    ▼
Production
```

Applications are never deployed directly from source code — production deployments always originate from a Docker image stored in GitHub Container Registry (GHCR).

---

## 5.3 Continuous Integration

Every repository defines an automated CI pipeline that validates the application remains deployable after every change: dependency restoration, compilation, automated testing and Docker image creation. Any failed step fails the pipeline.

### Build

The build stage compiles the application and produces deployable artifacts (e.g. Hugo static assets, React bundles, ASP.NET binaries). A successful build must be reproducible from source code alone.

### Test

Automated tests (unit, integration, end-to-end, depending on the application) run immediately after the build to prevent broken applications from reaching production. Any failure fails the pipeline.

### Docker Packaging

Once validation succeeds, the application is packaged as a Docker image — the deployable artifact. The platform deploys images, not source code, which keeps local environments consistent, production reproducible and runtime dependencies explicit.

---

## 5.4 Container Registry

All deployable artifacts are published to GitHub Container Registry (GHCR), the central, immutable source of deployment artifacts for the platform and the deployment source for Coolify. Applications are never deployed from local developer machines.

---

## 5.5 Continuous Deployment

### Deployment Trigger

After publishing a Docker image, the CI pipeline triggers a deployment through a Coolify webhook. This is fully automated — no manual deployment steps are required under normal circumstances.

### Deployment Execution

Coolify performs the deployment by pulling the latest image from GHCR, creating a new container instance, injecting environment variables, starting the application, and registering routes and SSL certificates. Applications should remain unaware of deployment details.

---

## 5.6 Deployment Strategy

### Forward-Only Deployments

New versions replace previous versions through new deployments; rollback is intentionally not part of the normal operational workflow (see [Forward-Only Evolution](02-principles.md#27-forward-only-evolution)). Issues are resolved by deploying a fix, creating a new migration, or shipping a corrected version.

### Small Releases

Applications should be deployed frequently. Smaller deployments give faster feedback, easier troubleshooting, lower risk and simpler root-cause analysis — large infrequent releases are discouraged.

---

## 5.7 Environment Strategy

### Local Environment

Every application must support local execution, independent from production, for development, testing and experimentation.

### Production Environment

Production is the canonical runtime environment, fully automated and managed by Coolify, with configuration injected through environment variables.

### Future Environments

Additional environments (e.g. staging, pre-production, ephemeral) may be introduced when justified. The platform currently optimizes for simplicity and avoids maintaining unnecessary environments.

---

## 5.8 Configuration Management

### Configuration Through Environment Variables

Application configuration is provided through environment variables — see [Configuration Standards](04-application-architecture.md#45-configuration-standards) for the standard variables applications must expose. Applications must not rely on machine-specific configuration.

### Secrets Management

Secrets (database credentials, API keys, access tokens, signing secrets) are managed separately from source code and must never be committed to Git. Backend application secrets are stored within Coolify.

### Frontend Configuration

Frontend applications do not contain secrets. Frontend configuration (API endpoints, client identifiers, public values) is typically injected at build time through GitHub Actions — any value exposed to frontend code should be assumed public.

---

## 5.9 Database Deployment

### Schema Migrations

Database schema changes are deployed together with application changes and must be versioned through migrations (see [Data Access Standards](04-application-architecture.md#46-data-access-standards)); manual schema changes are discouraged.

### Migration Execution

For ASP.NET applications, Entity Framework migrations run automatically during deployment. Applications are responsible for bringing their own database schema to the expected version, keeping schema changes versioned, deployments reproducible and environment drift minimized.

### Forward-Only Migrations

Migrations follow the same philosophy as application deployments: they evolve schemas forward, and down migrations are not part of normal operations.

---

## 5.10 Failure Handling

### Deployment Failures

If a deployment fails, the failure should be visible in CI logs, diagnosed, and resolved by deploying a corrected version — shipping a fix is preferred over reverting infrastructure state.

### Runtime Failures

Runtime issues are diagnosed through Seq logs, application health endpoints and Beszel infrastructure metrics (see [Observability Layer](03-platform.md#38-observability-layer)). Observability is the primary troubleshooting mechanism.

---

## 5.11 Operational Ownership

Applications are expected to be self-contained: source code, tests, Docker image definition, database migrations, CI pipeline and deployment configuration all live in the application repository. Any application should be able to move from repository creation to production deployment with minimal platform-specific work — deployability is a first-class feature of every application.
