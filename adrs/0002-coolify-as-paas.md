# ADR-0002: Coolify as Platform Layer

Status: Accepted

## Context

Managing Docker workloads directly on a VPS introduces operational overhead.

## Decision

[Coolify](https://coolify.ne2.studio/) will be used as the platform layer for deploying and operating application containers.

See [Platform Overview § Coolify](../docs/03-platform.md#coolify) for its full responsibilities.

## Consequences

* Faster deployments.
* Lower operational complexity.
* Dependency on the Coolify ecosystem.
