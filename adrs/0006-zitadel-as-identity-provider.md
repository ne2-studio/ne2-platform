# ADR-0006: Zitadel as Identity Provider

Status: Accepted

## Context

Authentication should be centralized and reusable across applications.

## Decision

Use [Zitadel](https://auth.ne2.studio) as the platform Identity Provider.

See [Identity Layer](../docs/03-platform.md#37-identity-layer) and [Authentication and Authorization](../docs/04-application-architecture.md#47-authentication-and-authorization) for how applications integrate with it.

## Consequences

* Consistent authentication model.
* Reduced duplication.
* Dependency on a centralized identity service.
