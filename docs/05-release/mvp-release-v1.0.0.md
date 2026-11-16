# MVP Release v1.0.0 - Corte 1

This document marks the official delivery of the **Salud Activa (GestionTurnosApp)** MVP for the first academic cut.

---

##  Release Information
- **Version:** `v1.0.0-corte1`
- **Date:** 2026-09-03
- **Branch:** `main`
- **Scope:** Complete MVP (Auth, Profile, Appointments, Offline Cache).

##  Included Features
1.  **Identity:** Secure registration and login using JWT.
2.  **Medical Profile:** Storage of blood type, allergies, and emergency contacts.
3.  **Appointment Management:** Real-time scheduling with doctor and specialty selection.
4.  **Offline Resilience:** Room-based caching to view appointments without internet.
5.  **Notifications:** Push alerts for appointment confirmation.

##  Delivery Artifacts
- **Source Code:** Available in the root of the main repository.
- **Documentation:** Full discovery, design, and architecture reports in the `docs/` folder.
- **Backend API:** Deployed/Moked in Node.js with MongoDB support.

##  Installation & Execution
1.  **Frontend:** Open the `app/` folder in Android Studio and run on an emulator/device (API 24+).
2.  **Backend:** Navigate to `backend/`, run `npm install` and `npm start`.
3.  **Database:** Ensure MongoDB is running or connected via the `.env` string.

---

##  Acceptance Criteria Status
- [x] All functionalities implemented and functional.
- [x] Code merged to the stable `main` branch.
- [x] Documentation synchronized in the docs repository.
