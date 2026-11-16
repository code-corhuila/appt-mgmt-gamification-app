const { ensureDatabaseConnected } = require('../../../../config/dbConnections');
const User = require('../../../../models/User');
const UserEntity = require('../../../../src/domain/entities/User');
const UserRepository = require('../../../../src/domain/ports/UserRepository');

class MongooseUserRepository extends UserRepository {
    async findByEmail(email) {
        if (!email) return null;
        await ensureDatabaseConnected();
        const userDoc = await User.findOne({ email });
        if (!userDoc) return null;
        return this._mapToEntity(userDoc);
    }

    async findById(id) {
        if (!id) return null;
        await ensureDatabaseConnected();
        const userDoc = await User.findById(id);
        if (!userDoc) return null;
        return this._mapToEntity(userDoc);
    }

    async save(userEntity) {
        await ensureDatabaseConnected();
        const userDoc = new User({
            nombre: userEntity.nombre,
            email: userEntity.email,
            telefono: userEntity.telefono,
            contrasena: userEntity.contrasena,
            isVerified: userEntity.isVerified,
            verificationCode: userEntity.verificationCode,
            fcmToken: userEntity.fcmToken,
            tipoSanguineo: userEntity.tipoSanguineo,
            alergias: userEntity.alergias,
            condiciones: userEntity.condiciones,
            contactoEmergencia: userEntity.contactoEmergencia
        });
        const savedDoc = await userDoc.save();
        return this._mapToEntity(savedDoc);
    }

    async update(id, userData) {
        if (!id) return null;
        await ensureDatabaseConnected();
        const updatedDoc = await User.findByIdAndUpdate(id, userData, { new: true });
        if (!updatedDoc) return null;
        return this._mapToEntity(updatedDoc);
    }

    _mapToEntity(userDoc) {
        return new UserEntity({
            id: userDoc._id ? userDoc._id.toString() : userDoc.id,
            nombre: userDoc.nombre,
            email: userDoc.email,
            telefono: userDoc.telefono || "",
            contrasena: userDoc.contrasena,
            isVerified: userDoc.isVerified || false,
            verificationCode: userDoc.verificationCode || null,
            fcmToken: userDoc.fcmToken || null,
            tipoSanguineo: userDoc.tipoSanguineo || "",
            alergias: userDoc.alergias || "",
            condiciones: userDoc.condiciones || "",
            contactoEmergencia: userDoc.contactoEmergencia || "",
            fechaCreacion: userDoc.fechaCreacion
        });
    }
}

module.exports = MongooseUserRepository;
