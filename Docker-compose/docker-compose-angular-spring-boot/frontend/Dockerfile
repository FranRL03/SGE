# FROM node:12.22-alpine as angular
FROM node as build
WORKDIR /usr/angular
COPY package*.json .
RUN npm install
COPY . .
RUN npm build

FROM nginx:alpine
RUN rm -rf /usr/share/nginx/html/*
COPY --from=build /usr/angular/dist/frontend* /usr/share/nginx/html/
