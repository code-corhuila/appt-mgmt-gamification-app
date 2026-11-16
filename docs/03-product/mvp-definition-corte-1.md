# MVP Definition - Corte 1 (Salud Activa)

This document consolidates the context analysis, MVP scope, and initial design for the first academic cut (Corte 1) of the **Salud Activa (GestionTurnosApp)** project.

---

## 1. Context Analysis

### 1.1. Problem Definition
Patients and clinics face high inefficiency in medical coordination. Manual processes (calls/WhatsApp) lead to:
- **20% Absenteeism:** No automated reminders.
- **Data Fragmentation:** Medical records and appointment dates are scattered.
- **Administrative Overhead:** Clinic staff spend ~4 hours daily on manual confirmations.

### 1.2. Target Users (Personas)
- **Primary: The Recurring Patient.** Needs to manage multiple appointments and follow-up medications. Values speed and offline access.
- **Secondary: The Independent Doctor.** Needs a clear, real-time view of their daily agenda without paper-based risks.

### 1.3. Market Benchmarking
- **Doctoralia:** Strong directory but high friction for quick scheduling.
- **Mi Salud (Standard Apps):** Lacks integrated medication tracking and robust offline support for low-connectivity areas.

---

## 2. MVP Definition (Scope)

### 2.1. Candidate Features
1. Secure Authentication (JWT).
2. Patient Medical Profile.
3. Real-time Appointment Booking.
4. Push Notification Reminders (FCM).
5. Offline Mode (Room DB).
6. Medication Tracking & Reminders.
7. Medical Study PDF Storage.
8. Integrated Chat.
9. Gamification (Achievements).

### 2.2. Scope for Corte 1 (The MVP)
- **Auth:** Login/Register with email.
- **Profile:** Basic medical data (Blood type, Allergies).
- **Appointments:** List and request new slots.
- **Offline Support:** Local cache for viewing existing appointments.
- **Notifications:** Receive confirmation alerts.

### 2.3. Out of Scope (Post-MVP)
- **Corte 2:** Integrated Chat and PDF Study management.
- **Corte 3:** Gamification, AI text recognition (OCR) for medical results.

---

## 3. Initial Design

### 3.1. Main User Flows
1. **Onboarding:** Register -> Complete Profile -> Dashboard.
2. **Scheduling:** Dashboard -> Select Specialty -> Pick Slot -> Confirm -> Notification.

### 3.2. Data Model (Initial Entities)
- **User:** `id, email, password, blood_type, allergies`.
- **Appointment:** `id, user_id, date, specialty, doctor, status`.
- **Medication:** `id, user_id, name, dosage, frequency`.

### 3.3. UI/UX Reference
- **Wireframes:** Mapped in `docs/12-ux-ui/navigation-map.md`.
- **Design Tokens:** Defined in `docs/12-ux-ui/design-system.md` (Azul Salud #0056B3).

---

## 4. Documentation Consolidation
All deliverables are versioned in the following paths:
- Context/Problem: `docs/01-context/overview.md` & `docs/03-product/problem-framing.md`
- Design: `docs/12-ux-ui/`
- Domain: `docs/02-domain/`
- Technical Decisions: `docs/05-architecture/decisions/`
