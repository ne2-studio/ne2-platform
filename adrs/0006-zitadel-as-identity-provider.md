# ADR-0006: Zitadel as Identity Provider

Status: Accepted

## Context

Authentication should be centralized and reusable across applications.

## Decision

Use Zitadel as the platform Identity Provider.

Applications delegate authentication to Zitadel and focus on authorization.

## Consequences

* Consistent authentication model.
* Reduced duplication.
* Dependency on a centralized identity service.
