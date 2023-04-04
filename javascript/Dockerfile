FROM node:9-slim
WORKDIR /app

COPY package*.json ./

RUN npm install

COPY main.js /app

EXPOSE 8080

CMD ["node", "main.js"]