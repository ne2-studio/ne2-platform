## 1. Purpose

### 1.1 What is the Ne2 Platform

Ne2 Platform is the internal application platform used to build, deploy and operate products, prototypes, MVPs and business applications.

Its purpose is to minimize the friction between identifying a problem and having a working solution running in production, through a consistent set of infrastructure, deployment processes, architectural conventions and operational practices.

Although originally designed for personal projects and small products, the platform is built around technologies and practices that are transferable to larger-scale environments.

---

### 1.2 Goals

#### Fast idea-to-production cycle

The time between having an idea and deploying a working version should be measured in hours or days, not weeks. Creating a new application should require minimal infrastructure work and minimal operational decisions.

#### Low operational overhead

Applications should require as little manual maintenance as possible. Operational complexity should be avoided unless it solves a real, existing problem.

#### Low cost

Infrastructure costs should remain predictable and independent from the number of experiments, prototypes or early-stage products being developed, so the platform encourages experimentation rather than discouraging it through expense.

#### Technology freedom

Developers are free to choose the most appropriate technology stack for a given application. The platform standardizes deployment and operations (see [Architecture Principles](02-principles.md)), not implementation details.

#### Incremental scalability

Applications should be able to evolve progressively. The platform supports replacing individual components as scaling requirements emerge, without requiring a complete redesign from day one.

---

### 1.3 Non-Goals

The platform explicitly does not optimize for:

* **Enterprise-grade infrastructure** — it is not designed to satisfy enterprise governance, compliance or regulatory requirements.
* **Multi-region deployments** — applications are deployed in a single region; global distribution is delegated to external services when needed.
* **Infinite scalability** — the platform is not built to handle internet-scale workloads from day one; infrastructure complexity is only introduced when justified by actual demand.
* **Maximum availability** — simplicity and speed of iteration are prioritized over sophisticated high-availability architectures.
* **Technology standardization** — the platform does not force applications into a single language, framework or architectural style; consistency is achieved through deployment and operational standards instead (see [Application Architecture Standards](04-application-architecture.md)).
