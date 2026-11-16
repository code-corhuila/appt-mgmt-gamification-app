import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE

def create_parcial_doc():
    doc = docx.Document()

    # Page Margins
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Document Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_title = p_title.add_run("PARCIAL DE PREGUNTAS ABIERTAS — TALLERES W11 Y W13")
    run_title.font.name = 'Calibri'
    run_title.font.size = Pt(18)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(31, 78, 121) # Dark Blue

    # Metadata Paragraph
    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_meta = p_meta.add_run("Estudiante: Brayan Yara (@BrayanYara1)  |  Sistemas Distribuidos 2026-B  |  CORHUILA\nProyecto: Salud Activa — Gestión de Bienestar Médico")
    run_meta.font.name = 'Calibri'
    run_meta.font.size = Pt(11)
    run_meta.font.italic = True
    run_meta.font.color.rgb = RGBColor(89, 89, 89)

    doc.add_paragraph() # Spacer

    cases = [
        {
            "num": "1",
            "title": "El salto que usted marcó (W11)",
            "evidencias": [
                ("Enlace a la fila del salto (Paso 2 api-gateway -> auth-service):", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/blob/da3a25e5a9a0ef0e3cb87a2c5f8cf7159160ab9f/11-week/workshop/01-journey.md#L12"),
                ("Enlace a la línea de código que inyecta la traza (downstream.js):", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/blob/da3a25e5a9a0ef0e3cb87a2c5f8cf7159160ab9f/11-week/workshop/03-instrumentation/downstream.js#L4")
            ],
            "fundamentacion": "En la llamada del salto 2 de api-gateway hacia auth-service (POST /api/v1/auth/verify-token), la línea 4 de downstream.js asigna el header traceparent con el valor traceCtx.traceparent. Si esta línea no existiera, el encabezado HTTP de contexto de traza no se transmitiría en la solicitud al servicio receptor. Al consultar por el trace_id de la transacción, dejaría de visualizarse el span secundario ejecutado por auth-service, rompiéndose la propagación de contexto distribuida y fragmentando el árbol de traza en spans huérfanos sin correlación."
        },
        {
            "num": "2",
            "title": "Una línea de log de su incidente (W11)",
            "evidencias": [
                ("Enlace a la línea de log del simulacro (08-incident.md):", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/blob/da3a25e5a9a0ef0e3cb87a2c5f8cf7159160ab9f/11-week/workshop/08-incident.md#L22"),
                ("Enlace a la regla del contrato de logs (02-log-contract.md):", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/blob/da3a25e5a9a0ef0e3cb87a2c5f8cf7159160ab9f/11-week/workshop/02-log-contract.md#L47")
            ],
            "fundamentacion": "La línea 22 de 08-incident.md registra el evento auth.internal.timeout con nivel ERROR. Según la regla del contrato en la línea 47 de 02-log-contract.md, el nivel ERROR se aplica a fallos críticos que requieren intervención, incluyendo explícitamente el caso donde un servicio downstream excede el tiempo límite de SLA (duration_ms: 3004). Las otras tres líneas del log generadas durante esta solicitud se agrupan y consultan mediante el campo correlation_id (valor drill-88121) o el trace_id (8ff92f3577b34da6a3ce929d0e0e9999), asegurando la trazabilidad completa entre microservicios."
        },
        {
            "num": "3",
            "title": "Su código contra su test (W11)",
            "evidencias": [
                ("Enlace a la línea del middleware que crea el contexto (middleware.js):", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/blob/da3a25e5a9a0ef0e3cb87a2c5f8cf7159160ab9f/11-week/workshop/03-instrumentation/middleware.js#L7"),
                ("Enlace a la aserción del test (index.test.js):", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/blob/da3a25e5a9a0ef0e3cb87a2c5f8cf7159160ab9f/11-week/workshop/03-instrumentation/index.test.js#L17")
            ],
            "fundamentacion": "La línea 7 de middleware.js lee el header traceparent de la solicitud entrante y genera el objeto traceCtx mediante generateTraceContext(incomingHeader). Si esta línea se borra o no procesa el encabezado entrante, el sistema no puede asociar el traceId recibido (4bf92f3577b34da6a3ce929d0e0e4736) y generará un ID aleatorio nuevo. Como resultado, falla la aserción de la línea 17 en index.test.js (assert.strictEqual(traceCtx.traceId, '4bf92f3577b34da6a3ce929d0e0e4736')) con un AssertionError por desigualdad de cadenas, rompiendo la propagación distribuida."
        },
        {
            "num": "4",
            "title": "Su presupuesto de errores (W11)",
            "evidencias": [
                ("Enlace al objetivo y ventana del SLO de disponibilidad (05-slo.md):", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/blob/da3a25e5a9a0ef0e3cb87a2c5f8cf7159160ab9f/11-week/workshop/05-slo.md#L6"),
                ("Enlace al tráfico mensual estimado (05-slo.md):", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/blob/da3a25e5a9a0ef0e3cb87a2c5f8cf7159160ab9f/11-week/workshop/05-slo.md#L36"),
                ("Enlace a la operación del presupuesto de error (05-slo.md):", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/blob/da3a25e5a9a0ef0e3cb87a2c5f8cf7159160ab9f/11-week/workshop/05-slo.md#L40-L41")
            ],
            "fundamentacion": "Para el SLO de disponibilidad con objetivo del 99.5%, una ventana de 30 días (43,200 minutos) y un tráfico estimado de 15,000 peticiones/día (450,000 peticiones/mes), las operaciones completas son:\n1. Peticiones fallidas permitidas: (100% - 99.5%) * 450,000 = 0.5% * 450,000 = 2,250 peticiones fallidas/mes.\n2. Minutos de presupuesto de error: 0.5% * 43,200 minutos = 0.005 * 43,200 = 216 minutos de presupuesto (3 horas y 36 minutos) al mes."
        },
        {
            "num": "5",
            "title": "La primera alerta (W11)",
            "evidencias": [
                ("Enlace a la regla de la alerta (06-alerts.yml):", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/blob/da3a25e5a9a0ef0e3cb87a2c5f8cf7159160ab9f/11-week/workshop/06-alerts.yml#L4-L16"),
                ("Enlace a la línea del incidente con el minuto (08-incident.md):", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/blob/da3a25e5a9a0ef0e3cb87a2c5f8cf7159160ab9f/11-week/workshop/08-incident.md#L30")
            ],
            "fundamentacion": "La primera alerta en dispararse es AppointmentServiceFastBurnErrorBudget, la cual se activa en el minuto 5 del simulacro (15:05 UTC). Este minuto resulta de sumar los 3 minutos iniciales requeridos para acumular la tasa de errores que supera el umbral de quemado rápido (Burn Rate 14.4) tras la inyección del fallo a las 15:00 UTC (minuto 0), más la ventana de evaluación obligatoria definida en la regla con for: 2m (3 min + 2 min = 5 min)."
        },
        {
            "num": "6",
            "title": "Un dato que cruza su frontera (W13)",
            "evidencias": [
                ("Enlace a la fila del dato clasificado (AST-02 en 01-attack-surface.md):", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/blob/da3a25e5a9a0ef0e3cb87a2c5f8cf7159160ab9f/13-week/workshop/01-attack-surface.md#L63"),
                ("Enlace al reclamo de la frontera (TB1 en README.md e Issue #1):", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/blob/da3a25e5a9a0ef0e3cb87a2c5f8cf7159160ab9f/13-week/workshop/README.md#L13-L15")
            ],
            "fundamentacion": "Tomando el dato AST-02 (JWT Bearer Tokens) clasificado como Confidential, el cual cruza la frontera TB1 (Cliente Android a API Gateway): si este token se expone o es interceptado, un atacante obtiene autorización completa en la API sin conocer la contraseña. El daño concreto hacia el usuario es la suplantación de identidad para agendar o cancelar citas médicas a su nombre y la exposición ilegítima de sus datos de salud al consultar /api/turnos/usuario/:id. Para el producto, esto implica la violación de la privacidad de datos médicos (PHI), sanciones regulatorias e invalidez de la autenticidad del sistema."
        },
        {
            "num": "7",
            "title": "Su amenaza de mayor riesgo (W13)",
            "evidencias": [
                ("Enlace al Pull Request (security/stride-BrayanYara1):", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/pull/1"),
                ("Enlace a la fila de la amenaza de mayor riesgo (stride-BrayanYara1.md):", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/blob/da3a25e5a9a0ef0e3cb87a2c5f8cf7159160ab9f/docs/05-architecture/security/stride-BrayanYara1.md#L45")
            ],
            "fundamentacion": "La amenaza de mayor riesgo es Denial of Service (D) sobre POST /api/auth/login y /api/turnos con Probabilidad 3 e Impacto 3 (Riesgo 9 Crítico). La probabilidad no es menor porque los endpoints de la frontera TB1 están expuestos públicamente en internet a través del API Gateway sin ningún control inicial de tasa de peticiones (express-rate-limit). El impacto no es menor porque una ráfaga masiva agota los pools de conexiones del Gateway y de la base de datos MongoDB, causando la indisponibilidad total del sistema para todos los pacientes reales."
        },
        {
            "num": "8",
            "title": "Lo que tomó del libro (W13)",
            "evidencias": [
                ("Enlace a la fila marcando la mitigación con [B] (stride-BrayanYara1.md):", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/blob/da3a25e5a9a0ef0e3cb87a2c5f8cf7159160ab9f/docs/05-architecture/security/stride-BrayanYara1.md#L34"),
                ("Enlace a la sección de References con autor, título y páginas (stride-BrayanYara1.md):", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/blob/da3a25e5a9a0ef0e3cb87a2c5f8cf7159160ab9f/docs/05-architecture/security/stride-BrayanYara1.md#L90-L94"),
                ("Enlace al issue que cita la referencia del libro (Issue #2 / 03-security-backlog.md):", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/issues/2")
            ],
            "fundamentacion": "De la lectura del libro de Matt Bishop (Computer Security: Art and Science, 2da ed., Cap. 14, pp. 340-348), se tomó la idea de que la validación pasiva de la firma JWT es insuficiente si el token es interceptado, requiriendo un control del ciclo de vida con expiración corta e invalidación explícita. Gracias a esta lectura, en la fila de Spoofing (S) se modificó la acción de mitigación: se pasó de verificar únicamente la firma estática en el Gateway a exigir el uso de tokens de acceso de corta duración (15 minutos), junto con un mecanismo activo de lista negra de revocación en Redis."
        },
        {
            "num": "9",
            "title": "La revisión de su PR (W13)",
            "evidencias": [
                ("Enlace directo al comentario/registro de revisión entre pares (stride-BrayanYara1.md):", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/blob/da3a25e5a9a0ef0e3cb87a2c5f8cf7159160ab9f/docs/05-architecture/security/stride-BrayanYara1.md#L52-L57"),
                ("Enlace al commit del cambio derivado de la revisión (361f1b5):", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/commit/361f1b52f68e95ccb1e128f0e6b4aa6e47008a36")
            ],
            "fundamentacion": "El revisor señaló la necesidad de asegurar que la validación de payloads y el control de tasa de peticiones se apliquen obligatoriamente a nivel del API Gateway (backend/server.js) antes de delegar tráfico a los microservicios downstream. En respuesta al comentario, se actualizó el modelo STRIDE mediante el commit 361f1b52f68e95ccb1e128f0e6b4aa6e47008a36, formalizando en la sección CP6 que los middlewares top-level de Express (express-rate-limit y Joi) deben proteger el perímetro de la frontera TB1 previa llamada a auth-service y appointments-service."
        },
        {
            "num": "10",
            "title": "Su prueba negativa (W13)",
            "evidencias": [
                ("Enlace a la salida real en HOW-TO-RUN.md:", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/blob/da3a25e5a9a0ef0e3cb87a2c5f8cf7159160ab9f/13-week/workshop/04-security-ci/HOW-TO-RUN.md#L31-L41"),
                ("Enlace a la aserción de la prueba (auth-negative.test.js):", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/blob/da3a25e5a9a0ef0e3cb87a2c5f8cf7159160ab9f/13-week/workshop/04-security-ci/auth-negative.test.js#L81"),
                ("Enlace al issue (Issue #3 / 03-security-backlog.md):", "https://github.com/BrayanYara1/ProyectoDistribuidos2026/issues/3")
            ],
            "fundamentacion": "Salida real de Jest:\nPASS 13-week/workshop/04-security-ci/auth-negative.test.js\n  ✓ 3. Patient user attempting to invoke Admin purge endpoint MUST fail with 403 Forbidden (3 ms)\nTest Suites: 1 passed, 1 total | Tests: 3 passed, 3 total | Time: 0.412 s\n\nEn la prueba #3 (auth-negative.test.js#L81), el sistema responde 403 Forbidden y no 401 Unauthorized porque el usuario sí presenta un JWT válido y autenticado (role: patient), pero carece del alcance administrativo (role: admin) exigido por la ruta /api/turnos/admin/purge. Esta aserción demuestra el Criterio de Aceptación AC2 del Issue #3 (Security User Story 2), que requiere validar rechazos por falta de privilegios RBAC."
        }
    ]

    for c in cases:
        # Case Heading
        p_case = doc.add_paragraph()
        run_c = p_case.add_run(f"CASO {c['num']}: {c['title']}")
        run_c.font.name = 'Calibri'
        run_c.font.size = Pt(14)
        run_c.font.bold = True
        run_c.font.color.rgb = RGBColor(31, 78, 121)

        # Evidencia Header
        p_ev_hdr = doc.add_paragraph()
        p_ev_hdr.paragraph_format.space_after = Pt(2)
        run_ev_hdr = p_ev_hdr.add_run("Evidencia:")
        run_ev_hdr.font.name = 'Calibri'
        run_ev_hdr.font.size = Pt(11)
        run_ev_hdr.font.bold = True

        for label, url in c["evidencias"]:
            p_ev = doc.add_paragraph(style='List Bullet')
            p_ev.paragraph_format.space_after = Pt(2)
            p_ev.paragraph_format.left_indent = Inches(0.25)

            run_lbl = p_ev.add_run(f"{label}\n")
            run_lbl.font.name = 'Calibri'
            run_lbl.font.size = Pt(10)

            run_url = p_ev.add_run(url)
            run_url.font.name = 'Calibri'
            run_url.font.size = Pt(9.5)
            run_url.font.color.rgb = RGBColor(5, 99, 193) # Hyperlink blue
            run_url.font.underline = True

        # Fundamentacion Header
        p_fund_hdr = doc.add_paragraph()
        p_fund_hdr.paragraph_format.space_before = Pt(4)
        p_fund_hdr.paragraph_format.space_after = Pt(2)
        run_fund_hdr = p_fund_hdr.add_run("Fundamentación:")
        run_fund_hdr.font.name = 'Calibri'
        run_fund_hdr.font.size = Pt(11)
        run_fund_hdr.font.bold = True

        # Fundamentacion Text
        p_fund = doc.add_paragraph()
        p_fund.paragraph_format.space_after = Pt(12)
        run_fund = p_fund.add_run(c["fundamentacion"])
        run_fund.font.name = 'Calibri'
        run_fund.font.size = Pt(10.5)

        # Divider
        p_div = doc.add_paragraph()
        p_div.paragraph_format.space_after = Pt(8)
        run_div = p_div.add_run("―" * 55)
        run_div.font.color.rgb = RGBColor(200, 200, 200)

    output_path = "C:/Users/andyb/AndroidStudioProjects/GestionTurnosApp/Parcial_W11_W13_Brayan_Yara.docx"
    doc.save(output_path)
    print("SUCCESS")

if __name__ == "__main__":
    create_parcial_doc()
