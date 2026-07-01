# ADR-0004: Forward-Only Deployments

Status: Accepted

## Context

Rollback strategies increase deployment complexity.

## Decision

Deployments and database migrations evolve forward only.

See [Forward-Only Evolution](../docs/02-principles.md#27-forward-only-evolution) and [Deployment Strategy](../docs/05-deployment.md#56-deployment-strategy) for how this is applied.

## Consequences

* Simpler deployment model.
* Smaller releases encouraged.
* Greater discipline required when shipping changes.
