const express = require('express');
const router = express.Router();
const Estudio = require('../models/Estudio');
const { connectDatabase } = require('../config/dbConnections');
const authenticateToken = require('../middleware/auth');

router.get('/', authenticateToken, async (req, res) => {
    try {
        await connectDatabase();
        const estudios = await Estudio.find({ usuarioId: req.userId });
        res.json(estudios);
    } catch (error) {
        console.error("❌ Error en GET /estudios:", error);
        res.status(500).json({ mensaje: "Error al obtener estudios", detalle: error.message });
    }
});

router.post('/', authenticateToken, async (req, res) => {
    try {
        await connectDatabase();
        const estudio = new Estudio({ ...req.body, usuarioId: req.userId });
        await estudio.save();
        res.status(201).json(estudio);
    } catch (error) {
        console.error("❌ Error en POST /estudios:", error);
        res.status(500).json({ mensaje: "Error al crear estudio", detalle: error.message });
    }
});

router.delete('/:id', authenticateToken, async (req, res) => {
    try {
        await connectDatabase();
        await Estudio.findOneAndDelete({ _id: req.params.id, usuarioId: req.userId });
        res.status(200).send();
    } catch (error) {
        console.error("❌ Error en DELETE /estudios:", error);
        res.status(500).json({ mensaje: "Error al eliminar estudio", detalle: error.message });
    }
});

module.exports = router;
