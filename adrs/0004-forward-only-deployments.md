# ADR-0004: Forward-Only Deployments

Status: Accepted

## Context

Rollback strategies increase deployment complexity.

## Decision

Deployments and database migrations evolve forward only.

Issues are resolved by deploying a fix rather than reverting state.

## Consequences

* Simpler deployment model.
* Smaller releases encouraged.
* Greater discipline required when shipping changes.
