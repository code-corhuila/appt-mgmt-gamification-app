# Documentation: HU-003 - MVP Delivery (Cut 1)

Documentation on the delivery process and the components included in the Cut 1 MVP.

## MVP Scope
The Cut 1 MVP focuses on the application's base access and security system. It includes:
1. **Authentication Module:** Based on the scope defined in HU-02.
2. **Base Infrastructure:** Architecture (MVVM) and database configuration.
3. **Workflow:** Implementation of the Gitflow model (`develop` -> `qa` -> `main`).

## Deliverables
- **Repository:** Complete source code on the `main` branch.
- **Binary:** APK file generated and available in the GitHub Releases section.
- **Documentation:** Architecture guides, requirements, and deployment manual in the `docs/` folder.

## Branch Flow
- `develop`: Active development and new features.
- `qa`: Integration testing, bug fixing, and stabilization.
- `main`: Production versions, official deliveries, and releases.

## Technologies Used
- **Language:** Kotlin.
- **UI:** Jetpack Compose (Material 3).
- **Red:** Retrofit + OkHttp (for Auth).
- **Persistence:** Jetpack DataStore.
- **Architecture:** MVVM (Model-View-ViewModel).
