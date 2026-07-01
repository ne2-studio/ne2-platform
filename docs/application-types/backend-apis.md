# Backend APIs

Contain application business logic. Default stack: **ASP.NET, PostgreSQL, Docker** ([ADR-0008](../../adrs/0008-aspnet-as-default-backend.md)). Alternative backend technologies are permitted — see [Technology Freedom](../01-goals.md#technology-freedom). Backend applications should expose HTTP APIs and follow standard web application practices.

Regardless of technology stack, backend applications must be structured using hexagonal architecture (ports and adapters), with business logic isolated behind explicitly declared ports and infrastructure concerns implemented as adapters ([ADR-0011](../../adrs/0011-hexagonal-architecture-for-backends.md)). This semantically declares each application's ports and capabilities, eases AI-assisted development workflows, and enables testing business logic without infrastructure dependencies.

---

See [Application Architecture Standards](../04-application-architecture.md).
