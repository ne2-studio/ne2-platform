# ADR-0005: Public Source Repositories

Status: Accepted

## Context

Most platform applications do not contain sensitive business logic or secrets.

## Decision

Application repositories and container images are public by default.

Secrets are managed outside source control.

## Consequences

* Simpler CI/CD configuration.
* Reduced infrastructure costs.
* Increased transparency and reusability.
