# 5. Deployment Model

## 5.1 Purpose

This document defines how applications are built, tested, packaged and deployed within the Ne2 Platform.

The deployment model is designed around the following principles:

* Fully automated deployments.
* Repeatable builds.
* Immutable deployment artifacts.
* Minimal operational overhead.
* Fast feedback cycles.
* Forward-only evolution.

Every application deployed on the platform is expected to follow this model.

---

## 5.2 Deployment Pipeline Overview

All deployments follow the same high-level workflow.

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

Applications are never deployed directly from source code.

Production deployments always originate from a Docker image stored in GitHub Container Registry (GHCR).

---

## 5.3 Continuous Integration

Every repository is expected to define an automated CI pipeline.

The primary purpose of Continuous Integration is to validate that the application remains deployable after every change.

Minimum responsibilities include:

* Dependency restoration.
* Compilation.
* Automated testing.
* Docker image creation.

Applications should fail fast whenever any validation step fails.

---

### Build

The build stage compiles the application and produces deployable artifacts.

Examples:

* Hugo sites generate static assets.
* React applications generate frontend bundles.
* ASP.NET applications generate application binaries.

A successful build must be reproducible from source code alone.

---

### Test

Automated tests execute immediately after the build phase.

The objective is to prevent broken applications from reaching production.

Depending on the application, tests may include:

* Unit tests.
* Integration tests.
* End-to-end tests.

Any test failure must fail the pipeline.

---

### Docker Packaging

Once validation succeeds, the application is packaged as a Docker image.

The Docker image becomes the deployable artifact.

The platform deploys Docker images, not source code.

This guarantees that:

* Local environments remain consistent.
* Production deployments remain reproducible.
* Runtime dependencies are explicitly defined.

---

## 5.4 Container Registry

### GitHub Container Registry

All deployable artifacts are published to GitHub Container Registry (GHCR).

GHCR acts as the central source of deployment artifacts for the platform.

Responsibilities:

* Store Docker images.
* Distribute application versions.
* Provide immutable deployment artifacts.

Applications should never be deployed from local developer machines.

---

## 5.5 Continuous Deployment

### Deployment Trigger

After publishing a Docker image, the CI pipeline triggers a deployment through a Coolify webhook.

This process is fully automated.

No manual deployment steps should be required under normal circumstances.

---

### Deployment Execution

Coolify performs the deployment by:

1. Pulling the latest Docker image from GHCR.
2. Creating a new container instance.
3. Injecting environment variables.
4. Starting the application.
5. Registering routes and SSL certificates.

The deployment platform is responsible for runtime management.

Applications should remain unaware of deployment details.

---

## 5.6 Deployment Strategy

### Forward-Only Deployments

The platform follows a forward-only deployment model.

New versions replace previous versions through new deployments.

Rollback mechanisms are intentionally not part of the normal operational workflow.

Instead, issues should be resolved by:

* Deploying a fix.
* Creating a new migration.
* Shipping a corrected version.

This approach reduces deployment complexity and encourages small incremental changes.

---

### Small Releases

Applications should be deployed frequently.

Smaller deployments provide:

* Faster feedback.
* Easier troubleshooting.
* Lower deployment risk.
* Simpler root-cause analysis.

Large infrequent releases are discouraged.

---

## 5.7 Environment Strategy

### Local Environment

Every application must support local execution.

Developers should be able to run the application independently from the production environment.

Local environments are responsible for:

* Development.
* Testing.
* Experimentation.

---

### Production Environment

Production is the canonical runtime environment.

Production deployments are fully automated and managed by Coolify.

Production configuration is injected through environment variables.

---

### Future Environments

Additional environments may be introduced when justified.

Examples:

* Staging.
* Pre-production.
* Ephemeral environments.

The platform currently optimizes for simplicity and therefore avoids maintaining unnecessary environments.

---

## 5.8 Configuration Management

### Configuration Through Environment Variables

Application configuration is provided through environment variables.

Examples include:

```text id="envvars"
DATABASE_CONNECTION_STRING
ASPNETCORE_ENVIRONMENT
ZITADEL_AUTHORITY
ZITADEL_CLIENT_ID
PUBLIC_API_URL
```

Applications must not rely on machine-specific configuration.

---

### Secrets Management

Secrets are managed separately from source code.

Examples:

* Database credentials.
* API keys.
* Access tokens.
* Signing secrets.

Backend application secrets are stored within Coolify.

Secrets must never be committed to Git repositories.

---

### Frontend Configuration

Frontend applications do not contain secrets.

Frontend configuration is typically injected during build time through GitHub Actions.

Examples:

* API endpoints.
* Client identifiers.
* Public configuration values.

Any value exposed to frontend code should be assumed public.

---

## 5.9 Database Deployment

### Schema Migrations

Database schema changes are deployed together with application changes.

Schema modifications must be versioned through migrations.

Manual schema changes are discouraged.

---

### Migration Execution

For ASP.NET applications, Entity Framework migrations are executed automatically during deployment.

Applications are responsible for bringing their own database schema to the expected version.

This guarantees that:

* Schema changes remain versioned.
* Deployments remain reproducible.
* Environment drift is minimized.

---

### Forward-Only Migrations

Database migrations follow the same philosophy as application deployments.

Migrations should evolve schemas forward.

Down migrations are not considered part of normal operations.

---

## 5.10 Failure Handling

### Deployment Failures

If a deployment fails:

1. The failure should be visible in CI logs.
2. The issue should be diagnosed.
3. A corrected version should be deployed.

The preferred response to failure is shipping a fix rather than reverting infrastructure state.

---

### Runtime Failures

Runtime issues should be diagnosed through:

* Seq logs.
* Application health endpoints.
* Beszel infrastructure metrics.

Observability is considered the primary troubleshooting mechanism.

---

## 5.11 Operational Ownership

Applications are expected to be self-contained.

A deployable application should include:

* Source code.
* Tests.
* Docker image definition.
* Database migrations.
* CI pipeline.
* Deployment configuration.

The objective is that any application can move from repository creation to production deployment with minimal platform-specific work.

Deployability is considered a first-class feature of every application.
