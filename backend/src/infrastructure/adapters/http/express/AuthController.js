class AuthController {
    constructor(registerUser, loginUser, userRepository) {
        this.registerUser = registerUser;
        this.loginUser = loginUser;
        this.userRepository = userRepository;
    }

    async register(req, res) {
        try {
            const result = await this.registerUser.execute(req.body);
            res.status(201).json({ mensaje: "OK", email: result.email });
        } catch (error) {
            if (error.message === "DATABASE_UNAVAILABLE" || error.message.includes("buffering timed out") || error.message.includes("selection timed out")) {
                return res.status(503).json({ mensaje: "Servicio de base de datos no disponible temporalmente en el servidor" });
            }
            res.status(400).json({ mensaje: error.message });
        }
    }

    async login(req, res) {
        try {
            const { email, contrasena } = req.body || {};
            if (!email || !contrasena) {
                return res.status(401).json({ mensaje: "Credenciales inválidas" });
            }
            const result = await this.loginUser.execute(req.body);
            res.json({ mensaje: "OK", ...result });
        } catch (error) {
            if (error.message === "Credenciales inválidas" || error.message === "Faltan email o contraseña") {
                return res.status(401).json({ mensaje: error.message });
            }
            if (error.message === "Faltan datos obligatorios" || error.message === "Formato de email inválido") {
                return res.status(400).json({ mensaje: error.message });
            }
            if (error.message === "DATABASE_UNAVAILABLE" || error.message.includes("buffering timed out") || error.message.includes("selection timed out")) {
                return res.status(503).json({ mensaje: "Servicio de base de datos no disponible temporalmente en el servidor" });
            }
            console.error("❌ Error en login:", error);
            res.status(500).json({ mensaje: "Error interno en el servidor", detalle: error.message });
        }
    }

    async updateProfile(req, res) {
        try {
            const { nombre, telefono, tipoSanguineo, alergias, condiciones, contactoEmergencia } = req.body;
            const user = await this.userRepository.update(
                req.userId,
                { nombre, telefono, tipoSanguineo, alergias, condiciones, contactoEmergencia }
            );
            if (!user) return res.status(404).json({ mensaje: "Usuario no encontrado" });

            res.json({
                id: user.id,
                nombre: user.nombre,
                email: user.email,
                telefono: user.telefono,
                tipoSanguineo: user.tipoSanguineo,
                alergias: user.alergias,
                condiciones: user.condiciones,
                contactoEmergencia: user.contactoEmergencia
            });
        } catch (error) {
            res.status(500).json({ mensaje: "Error al actualizar perfil", detalle: error.message });
        }
    }

    async updateFcmToken(req, res) {
        try {
            const { token } = req.body;
            await this.userRepository.update(req.userId, { fcmToken: token });
            res.status(200).send();
        } catch (error) {
            res.status(500).json({ mensaje: "Error FCM", detalle: error.message });
        }
    }
}

module.exports = AuthController;
