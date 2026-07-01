# ADR-0012: Monorepo per Product

Status: Accepted

## Context

Products are typically made of multiple tightly coupled services (e.g. a backend API and a frontend SPA) that evolve together. Splitting them across separate repositories slows iteration, makes large-scale features and refactors spanning multiple services harder to land atomically, and fragments the context available to AI-assisted development workflows, which benefit from seeing an entire product in a single workspace.

## Decision

Each product is organized as a single monorepo containing all of its related applications, each isolated in its own subfolder (e.g. `backend/`, `frontend/`). Every subfolder is self-contained — source, tests, Dockerfile and so on live inside it, following [Repository Standards](../docs/04-application-architecture.md#411-repository-standards).

Applications within a monorepo remain independently deployable: the CI/CD pipeline deploys each application through its own workflow, scoped to its subfolder (e.g. `.github/workflows/deploy-backend.yml`, `.github/workflows/deploy-frontend.yml`). These workflows run independently and in parallel, so a change to one application does not block or wait on another.

See [Repository Standards](../docs/04-application-architecture.md#411-repository-standards) and [Continuous Integration](../docs/05-deployment.md#53-continuous-integration).

## Consequences

* Faster iteration, and large-scale features or refactors spanning multiple services of the same product can be implemented and reviewed atomically.
* AI-assisted development workflows have full product context in a single workspace.
* Applications stay independently deployable through per-application, parallel CI/CD jobs.
* CI/CD must scope builds, tests and deployments per subfolder (e.g. path filters) to avoid rebuilding or redeploying unaffected applications.
