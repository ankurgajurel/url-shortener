FROM node:18-alpine

WORKDIR /app

COPY package*.json /app

RUN npm i

COPY . /app

CMD ["npm", "start"]