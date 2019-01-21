FROM node:11-alpine
WORKDIR /www/angular

COPY package.json .

RUN npm install -g @angular/cli
RUN npm install --quiet

EXPOSE 4200 49153
COPY . .
