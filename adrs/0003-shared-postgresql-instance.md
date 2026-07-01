# ADR-0003: Shared PostgreSQL Instance

Status: Accepted

## Context

Most applications are prototypes, MVPs or low-traffic products.

## Decision

Use a single PostgreSQL instance shared by all applications, isolated at the schema level.

See [Data Access Standards § Schema Ownership](../docs/04-application-architecture.md#46-data-access-standards).

## Consequences

* Lower infrastructure costs.
* Simpler operations.
* Reduced isolation between applications.
