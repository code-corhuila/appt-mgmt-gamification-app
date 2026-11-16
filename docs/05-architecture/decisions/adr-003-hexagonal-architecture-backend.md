# ADR-003: Hexagonal Architecture for Backend Services

*   **Status:** Accepted
*   **Date:** 2024-09-04
*   **Authors:** GestionTurnosApp Development Team

---

## 1. Context
The project requires a robust, maintainable, and testable backend service. As per the evaluation criteria for MVP 1 (Corte 1), the system must demonstrate clear architectural boundaries using Domain-Driven Design (DDD) and Hexagonal Architecture (Ports and Adapters).

## 2. Decision
We will refactor the existing Node.js backend to follow the **Hexagonal Architecture** pattern. This involves decoupling the core business logic from external concerns like databases, web frameworks, and third-party services.

### Architectural Layers:
1.  **Domain Layer (Core):** Contains business entities, value objects, and domain services. It also defines the **Ports** (interfaces) for external communication (e.g., `IUserRepository`). This layer has zero dependencies on external libraries.
2.  **Application Layer:** Implements the **Use Cases** (e.g., `RegisterUser`, `LoginUser`). It orchestrates the domain entities and uses the ports defined in the domain layer.
3.  **Infrastructure Layer (Adapters):** Contains the technical implementations of the ports.
    *   **Driving Adapters:** Express.js controllers and routes that receive requests.
    *   **Driven Adapters:** Mongoose/MongoDB implementations for persistence, BCrypt for hashing, and JWT for token generation.

## 3. Rationale
-   **Testability:** Business logic can be tested in isolation using mocks for ports.
-   **Maintainability:** Changes in infrastructure (e.g., switching from MongoDB to PostgreSQL) do not affect the business logic.
-   **Compliance:** Directly fulfills the "Hexagonal/DDD limits" and "Ports/Adapters" criteria of the project rubric.

## 4. Consequences
-   **Positive:** Highly decoupled code, easier to unit test, and clear separation of concerns.
-   **Negative:** Increased initial complexity due to the number of files and interfaces required.
