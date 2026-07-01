# ADR-0011: Hexagonal Architecture for Backend Applications

Status: Accepted

## Context

Backend applications are built with different technology stacks ([Technology Freedom](../docs/01-goals.md#technology-freedom)), which makes it hard to reason about their capabilities and integration points consistently across the platform. AI-assisted development workflows and automated testing both benefit from a predictable structure where business logic, external dependencies and entry points are clearly separated.

## Decision

Backend applications must be structured using hexagonal architecture (ports and adapters), regardless of technology stack. Application and domain logic is isolated behind explicitly declared ports; infrastructure concerns (databases, message brokers, external APIs, HTTP frameworks) are implemented as adapters plugged into those ports.

See [Backend APIs](../docs/04-application-architecture.md#42-supported-application-types).

## Consequences

* Ports and adapters semantically declare each application's capabilities and external dependencies, independent of implementation technology.
* Business logic can be unit tested without booting infrastructure, since ports can be substituted with test doubles.
* AI-assisted development workflows have a predictable structure to navigate and generate code against.
* Adds upfront structural overhead compared to a framework-coupled, layered approach.
