# Design System — Salud Activa

Integrantes:
- Andy Brahiam Yara Medina
- David Felipe Perdomo Castillo
- Sebastian Bermudez Gutierrez

> The design system is the shared visual language between design and development.
> It prevents inconsistencies, accelerates design, and reduces rework.
> **Rule:** Before creating a new component, check here if it already exists.
>
> Extracted from the functional mockup `mockup-1.html` (mobile app, patient-facing, Spanish UI).

---

## Design tokens

### Colors

```css
/* Base palette */
--color-primary-500: #0F3D3E;   /* Default — deep teal, brand color */
--color-primary-400: #1E5C5A;   /* Hover / lighter variant of primary */
--color-primary-50:  #EDF3F0;   /* Page background (tinted primary) */

--color-secondary-500: #D9A441; /* Gold accent — secondary CTAs, FAB, milestones */
--color-secondary-100: #F3E3BA; /* Soft accent background (avatars, highlighted cards) */

--color-neutral-50:  #FAFCFB;   /* Input backgrounds and list rows */
--color-neutral-100: #F0F4F2;   /* Secondary button background / back icon */
--color-neutral-200: #DCE7E2;   /* Borders and divider lines (--line) */
--color-neutral-900: #0E2A28;   /* Primary text / phone status bar background */

/* Semantic colors */
--color-success: #3E8F6B;      /* Confirmed, Attended, Mild severity, "on" switches */
--color-warning: #D9A441;      /* Pending (bg rgba(217,164,65,.18), text #9C7325) */
--color-error:   #C1533E;      /* Cancelled, Severe symptom, log out, offline banner */
--color-info:    (not defined in the mockup — no "info" state separate from warning/neutral)

/* Text */
--color-text-primary:   #0E2A28;  /* --ink */
--color-text-secondary: #5C7370;  /* --ink-soft */
--color-text-disabled:  (not defined — the mockup shows no disabled states;
                          recommend keeping the general convention: opacity 0.5)
--color-text-inverse:   #FFFFFF;  /* text on solid primary/accent/danger backgrounds */

/* Backgrounds */
--color-bg-page:    #EDF3F0;
--color-bg-card:    #FFFFFF;                 /* base card / phone surface */
--color-bg-subtle:  #FAFCFB;                 /* list item backgrounds, inputs, stat cards */
--color-bg-overlay: rgba(14,42,40,0.45);      /* bottom sheet backdrop */
```

**Note:** the mockup does not define a full 50–900 scale per color (it only uses 1–2 tones per role). If the system grows, generate the full scale from `--color-primary-500` (#0F3D3E) and `--color-secondary-500` (#D9A441) as the base.

### Typography

```css
/* Families */
--font-family-display: 'Space Grotesk', sans-serif;  /* Titles, brand, amounts, doctor names */
--font-family-sans:    'Inter', sans-serif;           /* Body text, labels, buttons */
--font-family-mono:    'JetBrains Mono', monospace;   /* Status bar, times, date badges, stats */

/* Sizes observed in the mockup (do not follow a strict modular scale) */
--font-size-2xs:  10px;     /* date labels (turno-date .m), badge-desc */
--font-size-xs:   11.5px;   /* label-sm, tabs, seg-btn */
--font-size-sm:   12.5px;   /* chips, toast, short subtitles */
--font-size-base: 13.5px;   /* list item text, menu-item */
--font-size-md:   15px;     /* doctor name on card, secondary section headers */
--font-size-lg:   17px;     /* top-nav h3 */
--font-size-xl:   21px;     /* confirmation h1, greeting */
--font-size-2xl:  26px;     /* login h1.title */

/* Weights */
--font-weight-regular: 400;
--font-weight-medium:  500;
--font-weight-semibold: 600;  /* buttons, Space Grotesk headings, section-title */
--font-weight-bold:    700;   /* brand-name, selected chips, badges, label-sm */

/* Line height */
--line-height-tight:  1.2;   /* headings */
--line-height-normal: 1.45;  /* chat bubbles, badge-desc */
--line-height-loose:  1.5;   /* subtitles, confirmation paragraphs */
```

### Spacing

```css
/* Scale observed (not strictly base-4; closer to base-2) */
--space-1:  4px;
--space-2:  6px;
--space-3:  8px;
--space-4:  10px;
--space-5:  12px;   /* standard list item padding */
--space-6:  14px;
--space-7:  16px;
--space-8:  18px;
--space-9:  20px;
--space-10: 22px;   /* standard horizontal content padding */
--space-12: 26px;
--space-16: 30px;
```

### Borders and shadows

```css
/* Border radius */
--radius-sm:   10px;   /* back-btn, time-chip */
--radius-md:   12px;   /* inputs, otp-box */
--radius-lg:   14px;   /* turno-item, med-item, stat-box, badge-card */
--radius-xl:   16px;   /* stat-card, summary-box */
--radius-2xl:  20px;   /* card-next, chips (pill) */
--radius-3xl:  24px;   /* bottom sheet (top corners) */
--radius-full: 9999px; /* avatars, FAB, switches, status badges */

/* Shadows */
--shadow-fab:   0 10px 24px -8px rgba(217,164,65,0.6);   /* floating action button (accent) */
--shadow-toast: 0 12px 30px -10px rgba(0,0,0,0.4);
--shadow-sheet: 0 -14px 40px -14px rgba(0,0,0,0.25);      /* bottom sheet, upward shadow */
--shadow-seg:   0 3px 8px -3px rgba(14,42,40,0.2);        /* active tab of the segmented control */
--shadow-frame: 0 20px 45px -20px rgba(14,42,40,0.35);    /* device frame, does not apply to real UI */
```

---

## Components

### Buttons

| Variant | Use | Example in the mockup |
|---------|-----|----------------|
| Primary (`btn-primary`) | Main action of the view | "Iniciar sesión" (Sign in), "Crear cuenta" (Create account), "Guardar medicamento" (Save medication) |
| Secondary (`btn-secondary`) | Secondary action inside a sheet/modal | "Cerrar" (Close) in the appointment detail sheet |
| Danger (`btn-danger`) | Destructive actions | "Cancelar turno" (Cancel appointment) |
| Accent (`btn-accent`) | Emphasis CTA, alternative to primary for "positive" flows | "Confirmar turno" (Confirm appointment), "Registrar síntoma" (Log symptom) |
| Ghost (`btn-ghost`) | Tertiary actions / text links | "¿Olvidaste tu contraseña?" (Forgot password?), "Reenviar código" (Resend code) |

** Gap vs. the base system:** the mockup does not implement a `disabled` state or a visible *loading* state on buttons (no `.btn:disabled` class or inline spinner exists in the CSS). It's recommended to add these before going to production, following the general rule (`opacity:0.5; cursor:not-allowed`) plus an inline spinner for async operations (see "Studies" -> OCR, which currently only uses a Toast as a substitute).

**Usage rules (as observed in the mockup):**
- Only one Primary or Accent action visible per view.
- Danger only appears inside the detail sheet, and only if the appointment status is `Confirmed` or `Pending`.
- There is no additional confirmation ("Are you sure?") before executing "Cancel appointment" — the sheet itself acts as the confirmation step. See the note under "Feedback".

### Forms

| Component | Use in the mockup |
|-----------|-------------|
| Text input | Login, registration, personal data editing, medication fields (name, dosage, frequency) |
| OTP input (4 digits) | Account verification — **did not exist in the base system, added as a new component** |
| Chip (single selection) | Medical specialty, symptom, intensity, quick date, available time slot — **did not exist in the base system, added as a new component** (replaces Select/Radio for fast flows) |
| Toggle / Switch | Privacy panel: share data with health insurer (EPS), push notifications, email reminders, offline mode |
| Textarea | Not used in the mockup |
| Select | Not used — replaced by Chips or by selectable card lists (`doc-option`) |
| Combobox | Not used |
| Checkbox | Not used — replaced by Switch/Toggle or Chip |
| Radio | Not used — replaced by Chip |
| DatePicker | Not used — replaced by pre-generated date chips (next 4 days) |

**Form errors — gap vs. the base system:**
The base system specifies a message below the field plus a red border. The mockup **does not implement this**: all form validation is resolved with a **generic Toast** (e.g. "Completa nombre, correo y contraseña" / "Fill in name, email and password", "Las contraseñas no coinciden" / "Passwords don't match", "Completa nombre, dosis y frecuencia" / "Fill in name, dosage and frequency"). There are no field-specific error messages or red borders. If the base system's rule is kept, this needs to be corrected in real development.

### Feedback

| Component | When | Duration / actual behavior in the mockup |
|-----------|------|---------|
| Toast/Snackbar | Action confirmations and validation errors | **2 seconds** (the base system specifies 4s — the mockup uses 2s; should be validated with UX) |
| Bottom sheet (`sheet`) | Appointment detail + destructive action (cancel) | Stays until the user closes it or cancels; acts as the base system's "Modal" for this use case |
| Status banner (`offline-banner`) | Offline mode active | Persistent at the top of the screen while the mode is active — **did not exist in the base system, added as a new component** |
| Inline alert | Not implemented (see gap under "Forms") |
| Classic confirmation modal ("Are you sure?") | Not implemented — the detail sheet takes on that role for cancelling appointments |
| Loading spinner | Not implemented — the OCR flow ("Scan study") simulates a wait with a Toast + `setTimeout`, with no visible spinner |
| Skeleton | Not implemented |

### Lists (replace "Data table" — there are no tables in the mockup)

The app is 100% mobile and doesn't use data tables; it uses card lists. Patterns found:

| Component | Use |
|--------|---------|
| `turno-item` | Appointment row (date, doctor, specialty, status badge). Tappable -> opens the detail sheet. |
| `med-item` / `study-item` | Medication / medical study row, with icon, name, subtitle, and a "Pending" tag (offline) |
| `symptom-item` | Symptom row with an intensity badge (Mild/Moderate/Severe) |
| `doc-option` | Selectable doctor card within the booking flow |
| Empty state | Simple gray text message ("No tienes turnos próximos." / "You have no upcoming appointments.", "Aún no hay historial." / "No history yet.") — **includes no illustration or CTA**, unlike what the base system calls for |

**Pagination / filters / multi-select:** not applicable — these don't exist in the mockup (short lists, no pagination).

---

## UX patterns

### Observed principles

1. **Confirm before destroying (partial):** cancelling an appointment doesn't go through an additional confirmation modal; the detail bottom sheet acts as an intermediate step, but there's no explicit second "Are you sure?".
2. **Immediate feedback:** every action shows a Toast or an immediate visual change (chip selection, sheet opening, etc.).
3. **Prevention vs. correction:** there is no real-time validation; validation only happens on submit, showing a Toast — a deviation from the base system, which calls for real-time validation.
4. **Empty state as a feature:** implemented minimally (text only), with no illustration or CTA.
5. **Offline mode as a cross-cutting feature (EP-007):** a pattern not covered by the original base system. Every write action (adding a medication, logging a symptom, sending a message, booking an appointment) is flagged with `pending:true` while offline mode is active, tagged with a "Pending" / "Pending sync" label in the UI, and "synced" (the flag is cleared) on reconnect, showing a Toast with the count of synced items.

### Error handling

The mockup **does not implement** the base system's HTTP error handling (401/403/404/500/timeout/network), since it's a functional prototype with no real backend (all state lives in memory/JS). When connecting to real services, the base system's error table should be implemented unchanged, since there is no divergent pattern replacing it.

---

## Accessibility — gaps found in the mockup

| Aspect | Status in the mockup |
|--------|-----------------|
| Text contrast | `--ink-soft` (#5C7370) on `--bg` (#EDF3F0) and on white should be validated against WCAG AA; not confirmed in the mockup |
| Form labels | `<label>` elements are visually associated with their inputs, but don't use explicit `for`/`id` attributes in the HTML — fix in development |
| Keyboard navigation | Not applicable in this prototype (touch-oriented); must be implemented in the real version |
| Images | No real images, only decorative SVG icons with no `aria-label` — add in development |
| Visible focus | Not implemented in the mockup |

---

## New components identified (not covered by the original base system)

- **Selection chip** (`chip`, `time-chip`): quick selection of one option among a few, used instead of Select/Radio.
- **OTP input** (`otp-box`): 4 single-digit boxes for account verification.
- **Bottom sheet** (`sheet` + `sheet-backdrop`): panel that slides up from the bottom to show detail and run contextual actions (including destructive ones).
- **Segmented control** (`segmented` / `seg-btn`): navigation between sub-sections within the same screen (Medications / Symptoms / Studies / Stats).
- **Profile accordion** (`menu-item` + `menu-panel`): expandable sections within Profile (Personal data, Medical history, Privacy, Achievements).
- **Global status banner** (`offline-banner`): persistent offline-mode notice.
- **Progress / achievement badge** (`badge-card`, gamification EP-006): card with icon, title, description, and progress bar.
- **FAB (Floating Action Button)**: direct access to "Book appointment" from Home and Appointments.

---

## Correlations

- Navigation map -> `12-ux-ui/navigation-map.md`
- Wireframes / functional mockup -> `mockup-1.html`
- UX non-functional requirements -> `04-requirements/non-functional.md`
