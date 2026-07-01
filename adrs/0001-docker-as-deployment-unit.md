# ADR-0001: Docker as Deployment Unit

Status: Accepted

## Context

The platform must support multiple technology stacks while maintaining a consistent deployment model.

## Decision

All deployable workloads must be packaged as Docker images.

See [Docker-First Architecture](../docs/04-application-architecture.md#43-docker-first-architecture) for the resulting application standard.

## Consequences

* Technology-independent deployments.
* Consistent operational model.
* Simplified infrastructure management.
* Containerization required for all applications.
