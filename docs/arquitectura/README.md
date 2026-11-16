# Índice Central de Arquitectura de Software — Salud Activa

Este documento centraliza el acceso a todos los artefactos de arquitectura, diseño técnico y decisiones del sistema **Salud Activa**, preparados para la evaluación de **Corte 3 (CORHUILA)**.

---

## 🏛️ 1. Decisiones de Arquitectura (ADRs)

| ID | Título | Estado | Documento |
| :--- | :--- | :--- | :--- |
| **ADR-001** | Lenguaje de Código y Documentación en Inglés | Aceptado | [ADR-001](../../TECHNICAL_MASTER_DOC.md#adr-001-documentation-and-code-language) |
| **ADR-002** | Selección de Tecnologías (Node.js, Kotlin, MongoDB, Docker) | Aceptado | [ADR-002](../05-architecture/decisions/adr-002-tech-stack-selection.md) |
| **ADR-003** | Arquitectura Hexagonal y Puertos/Adaptadores en Backend | Aceptado | [ADR-003](../05-architecture/decisions/adr-003-hexagonal-architecture-backend.md) |
| **ADR-004** | Proveedor de Nube y Cómputo (AWS ECS Fargate & ALB) | Aceptado | [ADR-004](../../certification/adr-001-cloud-provider-and-compute.md) |
| **ADR-005** | Persistencia Administrada y Bus de Eventos (MongoDB + RabbitMQ) | Aceptado | [ADR-005](../../certification/adr-002-managed-persistence-and-event-bus.md) |

---

## 📐 2. Diagramas C4 y Vistas de Arquitectura

- **C4 Nivel 1 (Contexto):** [Ver Vista General](../05-architecture/overview.md#c4-context-diagram)
- **C4 Nivel 2 (Contenedores):** [Ver Vista de Contenedores](../05-architecture/overview.md#c4-container-diagram)
- **Diagrama de Componentes y Redimensionamiento Nube:** [Nota de Rediseño Cloud](../../certification/design-note.md)
- **Catálogo de Servicios y Microservicios:** [Service Catalog](../09-microservices/service-catalog.md)

---

## 🔒 3. Seguridad y Modelado de Amenazas

- **Modelado de Amenazas STRIDE:** [Informe STRIDE](../05-architecture/security/stride-BrayanYara1.md)
- **Gobernanza y Políticas de Seguridad:** [Security Policy](../00-governance/security-policy.md)

---

## 💾 4. Modelos de Datos y Contratos de API

- **Modelos de Datos de Dominio:** [DATA_MODELS_MASTER.md](../../DATA_MODELS_MASTER.md)
- **Contratos de API REST (MVP 2):** [MVP2 Contracts](../07-api/contracts/mvp2-contracts.md)

---

## 🛠️ 5. Infraestructura y Despliegue

- **Configuración Docker Compose Local:** [compose.yml](../../compose.yml) & [compose.prod.yml](../../compose.prod.yml)
- **IaC AWS Terraform:** [README Terraform](../../terraform_aws/README.md)
- **Guía de Certificación y Evidencias:** [Certification Guide](../../certification/README.md)
