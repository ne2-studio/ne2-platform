# ADR-0009: Cloudflare as Edge Layer

Status: Accepted

## Context

Applications are hosted on a single VPS and require CDN and DNS capabilities.

## Decision

Cloudflare will act as the platform edge layer.

## Consequences

* Improved global delivery.
* Reduced origin load.
* Dependency on Cloudflare services.
