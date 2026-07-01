# ADR-0003: Shared PostgreSQL Instance

Status: Accepted

## Context

Most applications are prototypes, MVPs or low-traffic products.

## Decision

Use a single PostgreSQL instance shared by all applications.

Each application owns its own schema and database user.

## Consequences

* Lower infrastructure costs.
* Simpler operations.
* Reduced isolation between applications.
