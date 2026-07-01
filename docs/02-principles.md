# 2. Architecture Principles

These principles drive every architectural decision within the platform. When a technical decision is unclear, they serve as the primary decision-making framework.

---

### 2.1 Simplicity Over Sophistication

The simplest solution that satisfies current requirements is preferred. Additional complexity must justify itself through measurable benefits, not hypothetical future requirements.

---

### 2.2 Optimize for Speed of Iteration

The platform exists to accelerate learning. Reducing deployment friction, shortening feedback loops and enabling experimentation take priority over theoretical architectural perfection.

---

### 2.3 Build for Today's Scale

Infrastructure should solve today's problems. Future scalability concerns only influence decisions when there is evidence they will become relevant soon. Premature optimization is considered a form of waste.

---

### 2.4 Docker is the Universal Deployment Unit

Every deployable component must be packaged as a Docker image. Deployment, operations and infrastructure management are standardized around containers — see [Docker-First Architecture](04-application-architecture.md#43-docker-first-architecture) for the application-level requirements this implies.

---

### 2.5 Open Source First

Open source solutions are preferred whenever they satisfy platform requirements. Hosted SaaS products may be used when they offer clear advantages in simplicity, reliability or operational efficiency.

---

### 2.6 Shared Infrastructure Until Proven Otherwise

Infrastructure resources are shared by default. Dedicated infrastructure is only introduced when there is a demonstrated need related to security, performance, availability or operational isolation.

---

### 2.7 Forward-Only Evolution

Applications, databases and infrastructure evolve by moving forward, in small incremental changes. Rollbacks are exceptional events rather than a standard operational mechanism — see [Deployment Strategy](05-deployment.md#56-deployment-strategy) for how this applies to releases and migrations.

---

### 2.8 Operational Consistency Over Technological Consistency

Applications may use different implementation technologies, but operational practices — deployment, monitoring, configuration management, observability — remain consistent across the platform regardless of stack.

---

### 2.9 Everything as Code

Application code, infrastructure definitions, deployment pipelines and operational configuration are versioned whenever practical. Manual changes are minimized; repeatability is preferred over convenience.
