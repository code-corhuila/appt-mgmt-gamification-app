const express = require('express');
const router = express.Router();
const Medicamento = require('../models/Medicamento');
const { connectDatabase } = require('../config/dbConnections');
const authenticateToken = require('../middleware/auth');

router.get('/', authenticateToken, async (req, res) => {
    try {
        await connectDatabase();
        const medicamentos = await Medicamento.find({ usuarioId: req.userId });
        res.json(medicamentos);
    } catch (error) {
        console.error("❌ Error en GET /medicamentos:", error);
        res.status(500).json({ mensaje: "Error al obtener medicamentos", detalle: error.message });
    }
});

router.post('/', authenticateToken, async (req, res) => {
    try {
        await connectDatabase();
        const med = new Medicamento({ ...req.body, usuarioId: req.userId });
        await med.save();
        res.status(201).json(med);
    } catch (error) {
        console.error("❌ Error en POST /medicamentos:", error);
        res.status(500).json({ mensaje: "Error al crear medicamento", detalle: error.message });
    }
});

router.put('/:id', authenticateToken, async (req, res) => {
    try {
        await connectDatabase();
        const med = await Medicamento.findOneAndUpdate(
            { _id: req.params.id, usuarioId: req.userId },
            req.body,
            { new: true }
        );
        res.json(med);
    } catch (error) {
        console.error("❌ Error en PUT /medicamentos:", error);
        res.status(500).json({ mensaje: "Error al actualizar medicamento", detalle: error.message });
    }
});

router.delete('/:id', authenticateToken, async (req, res) => {
    try {
        await connectDatabase();
        await Medicamento.findOneAndDelete({ _id: req.params.id, usuarioId: req.userId });
        res.status(200).send();
    } catch (error) {
        console.error("❌ Error en DELETE /medicamentos:", error);
        res.status(500).json({ mensaje: "Error al eliminar medicamento", detalle: error.message });
    }
});

module.exports = router;
