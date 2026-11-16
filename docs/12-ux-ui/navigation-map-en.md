# Navigation Map — Salud Activa

> Defines the screen structure of the system, how screens connect to each other, and what routes
> exist. It is the reference when frontend and backend discuss what endpoints exist
> or how to reach a feature.
>
> Extracted from the functional mockup `mockup-1.html` — a patient-facing mobile app (single role, no admin panel).
> The routes below don't exist literally in the mockup (it's a single-page prototype that uses
> `goTo(id)` to toggle views via CSS); they are proposed here as real-world equivalents for frontend/backend.

---

## Frontend route structure

```
/                              → Redirects to /auth/login or /dashboard depending on session
├── /auth
│   ├── /login                 → Login form (view-login)
│   ├── /register              → New account registration (view-register)
│   ├── /verify                → 4-digit OTP verification (view-verify)
│   └── /forgot-password       → Password recovery (minimal flow: link sent via Toast)
│
├── /dashboard                 → Home (view-home) — main tab bar
│   └── (next appointment + recent appointments list; reachable after login/verify)
│
├── /appointments               → "My appointments" (view-turnos)
│   ├── /new                    → Book appointment (view-reservar): specialty → doctor → date → time
│   │                              [POST] /appointments
│   └── /:id                    → Appointment detail, opened as a bottom sheet (no dedicated route in the mockup)
│       └── /cancel             → Cancel appointment (action inside the sheet) [PATCH] /appointments/:id/cancel
│
├── /appointments/confirmation  → Booking confirmation (view-confirmacion), intermediate screen post-creation
│
├── /health                     → "Health" (view-salud) — segmented control with 4 sub-views
│   ├── ?tab=medications         → Medications: list/add [GET|POST] /health/medications
│   ├── ?tab=symptoms            → Symptoms: list/log [GET|POST] /health/symptoms
│   ├── ?tab=studies             → Studies: list/scan (OCR) [GET|POST] /health/studies
│   └── ?tab=stats               → Stats: adherence, symptoms (7 days), studies stored [GET] /health/stats
│
├── /chat                       → Chat with the assigned doctor (view-chat)
│   └── (messages) [GET|POST] /chat/messages
│
└── /profile                    → Authenticated user's profile (view-perfil)
    ├── /profile/personal-data   → Personal data (accordion: name, email) [PATCH] /profile
    ├── /profile/medical-history → Medical history (accordion, read-only — Attended/Cancelled appointments)
    ├── /profile/privacy         → Privacy and data (accordion: switches for EPS sharing, push notifications,
    │                              email reminders, offline mode) [PATCH] /profile/preferences
    ├── /profile/achievements    → Achievements / gamification (accordion, read-only) [GET] /profile/achievements
    └── /auth/logout             → Log out (inside Profile)
```

**Note:** the mockup has no `ADMIN` role or admin panel — it's a single-role app (authenticated patient). If the real system includes a back office for medical staff or admins, that structure should be documented separately (it's not part of this mockup).

---

## Screen map

| Screen | Proposed route | Component (ID in the mockup) | Minimum role | Backend service |
|--------|-------|-----------|--------------|----------------|
| Login | `/auth/login` | `view-login` | Public | auth-service |
| Register | `/auth/register` | `view-register` | Public | auth-service |
| Verification (OTP) | `/auth/verify` | `view-verify` | Public (temporary session) | auth-service |
| Home / Dashboard | `/dashboard` | `view-home` | USER | appointments-service |
| My appointments | `/appointments` | `view-turnos` | USER | appointments-service |
| Book appointment | `/appointments/new` | `view-reservar` | USER | appointments-service |
| Appointment confirmation | `/appointments/confirmation` | `view-confirmacion` | USER | appointments-service |
| Health (medications / symptoms / studies / stats) | `/health` | `view-salud` | USER | health-service |
| Chat with doctor | `/chat` | `view-chat` | USER | chat-service |
| Profile | `/profile` | `view-perfil` | USER | auth-service / profile-service |

**Main tab bar (persistent on Home, Appointments, Health, Chat, Profile):** Home · Appointments · Health · Chat · Profile.
**FAB (floating action button):** visible on Home and Appointments, always navigates to `/appointments/new`.

---

## Main user flows

### Flow 1 — Registration and account verification
```
Login (/auth/login)
    │
    ▼ Click "Create your account"
Register (/auth/register)
    │
    ├── Incomplete fields ──► Toast "Fill in all fields" (stays on /auth/register)
    ├── Passwords don't match ──► Toast "Passwords don't match"
    │
    ▼ Valid data
OTP verification (/auth/verify)
    │
    ├── Incomplete code ──► Toast "Enter the full code" (stays on /auth/verify)
    │
    └── Complete code ──► Account verified ──► Home (/dashboard)
```
**Related HUs:** HU-AUTH-003 (registration), HU-AUTH-004 (OTP verification)

### Flow 2 — Authentication
```
Landing (/)
    │
    ▼ (no session)
Login (/auth/login)
    │
    ├── Valid credentials ──► Dashboard (/dashboard)
    │
    └── Empty fields ────► Error toast, stays on Login
```
**Related HUs:** HU-AUTH-001, HU-AUTH-002

### Flow 3 — Booking a medical appointment
```
Home (/dashboard) or My appointments (/appointments)
    │
    ▼ FAB "+" or "View all" button
Book appointment (/appointments/new)
    │
    ▼ Select specialty → available doctors reload
    ▼ Select doctor → date (next 4 days) → available time slot
    ▼ Click "Confirm appointment"
Confirmation (/appointments/confirmation)
    │
    └── Click "Back to home" ──► Dashboard (/dashboard), appointment shown as "Next appointment"
```
**Related HUs:** HU-APPT-001 (booking), HU-APPT-002 (confirmation)

### Flow 4 — View detail and cancel an appointment
```
My appointments (/appointments) or Home list
    │
    ▼ Tap an appointment (turno-item)
Detail bottom sheet (overlay, no route change)
    │
    ├── Status = Confirmed / Pending ──► "Cancel appointment" button visible
    │       │
    │       ▼ Click
    │   Appointment moves to "Cancelled" status + Toast "Appointment cancelled" + sheet closes
    │
    └── Status = Attended / Cancelled ──► only a "Close" button (no destructive action)
```
**Related HUs:** HU-APPT-003 (detail), HU-APPT-004 (cancellation)

### Flow 5 — Logging health information (medications, symptoms, studies)
```
Health (/health)
    │
    ▼ Segmented control
    ├── Medications → "Add medication" (inline form) → Save → Confirmation toast
    ├── Symptoms → select symptom + intensity (chips) → "Log symptom" → Confirmation toast
    ├── Studies → "Scan study (OCR)" → Toast "Processing image..." → study added + final Toast
    └── Stats → read-only view (adherence, symptoms in 7 days, studies stored)
```
**Related HUs:** HU-HEALTH-001 through HU-HEALTH-004

### Flow 6 — Offline mode (offline-first)
```
Profile (/profile/privacy)
    │
    ▼ Turns on "Offline mode (simulated)" switch
Banner "Offline · changes saved locally" (persistent, any screen)
    │
    ▼ User adds a medication / symptom / study / message / appointment
Every new item is flagged with a "Pending" / "Pending sync" tag
    │
    ▼ Turns off "Offline mode" switch
All pending items are marked as synced
    │
    └── Toast "Connection restored · N items synced"
```
**Related HUs:** HU-OFFLINE-001, HU-OFFLINE-002

---

## Navigation rules

| Rule | Description |
|------|-------------|
| Authentication | Routes under `/dashboard`, `/appointments`, `/health`, `/chat`, `/profile` should redirect to `/auth/login` if there's no session (not explicitly implemented in the mockup, since there's no real backend) |
| Account verification | A newly registered account must go through `/auth/verify` before reaching `/dashboard` |
| Role-based authorization | Not applicable — the mockup only covers the `USER` role; no routes are restricted by role |
| 404 | Not implemented in the mockup (single-page app); in production, undefined routes should show a 404 screen with a link to `/dashboard` |
| Confirmation for destructive actions | Cancelling an appointment does **not** go through an additional "Are you sure?" modal — the detail bottom sheet takes on that role. Evaluate whether this meets the design system's general rule (which requires explicit confirmation) |
| Persistent tab bar | Home, Appointments, Health, Chat, and Profile always show the bottom tab bar; Login, Register, Verification, Book Appointment, and Confirmation do not |
| Contextual back button | Register and Book Appointment use an explicit back button (`back-btn`) instead of relying on the system gesture |

---

## Correlations

- Design system (visual components) -> `12-ux-ui/design-system.md`
- Wireframes / functional mockup -> `mockup-1.html`
- Frontend API contracts -> `07-api/contracts/openapi/`
- Roles and permissions -> `00-governance/security-policy.md` (to be defined: this mockup covers no role beyond USER)
