# Discovery Report - Salud Activa (GestionTurnosApp)

This report summarizes the initial research and discovery phase of the project, establishing the groundwork for the development of the MVP.

---

## 1. Problem Identification
The discovery phase identified a critical gap in medical coordination within local clinics.
- **Hypothesis:** Manual scheduling is the root cause of high absenteeism.
- **Evidence:** Benchmark data shows a 20% no-show rate due to lack of automated reminders and fragmented communication.
- **Value Proposition:** A unified mobile assistant for patients that manages appointments, medications, and medical records in a single, offline-capable interface.

## 2. User Research (Personas)
We identified two primary personas through clinic observation:
1. **Andrés (The Chronic Patient):** 45 years old, takes multiple medications, needs to coordinate monthly follow-ups. Frustration: Forgetting doses and losing physical appointment papers.
2. **Dr. Elena (The Specialist):** Needs to manage her agenda across two clinics. Frustration: Patients not showing up without notice, leaving empty slots.

## 3. Market Research (Benchmark)
We compared local and regional solutions:
- **Solution A (Web Portals):** Slow, not optimized for mobile, zero offline support.
- **Solution B (WhatsApp/Manual):** High human error rate, no data privacy (GDPR/Habeas Data concerns).
- **Salud Activa Advantage:** Native Android performance, push notifications (FCM), and encrypted local persistence (Room).

## 4. Key Findings for MVP
- **Critical Feature:** Offline access to appointment data is mandatory for users in low-signal clinic basements.
- **Critical Feature:** The "Checkmark" for medication intake provides a psychological reward (gamification seed).
- **Constraint:** Biometric authentication is required to protect sensitive health data.

---

##  Related Discovery Artifacts
- **Problem Framing:** [problem-framing.md](../03-product/problem-framing.md)
- **MVP Scope:** [mvp-definition-corte-1.md](../03-product/mvp-definition-corte-1.md)
- **System Overview:** [overview.md](overview.md)
