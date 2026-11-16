FROM node:22-alpine

WORKDIR /app

# Copiar archivos de definición de dependencias
COPY package*.json ./

# Instalar dependencias de producción
RUN npm ci --omit=dev

# Copiar el código fuente
COPY . .

# Exponer el puerto del API Gateway
EXPOSE 3000

# Comando de arranque
CMD [ "node", "server.js" ]
