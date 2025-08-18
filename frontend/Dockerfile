# Etapa 1: build da aplicação React
FROM node:20 AS build

WORKDIR /app

# Copia os arquivos do projeto
COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# Etapa 2: servidor Nginx para servir o build
FROM nginx:alpine

# Remove a página default do Nginx
RUN rm -rf /usr/share/nginx/html/*

# Copia os arquivos gerados pelo build do React
COPY --from=build /app/build /usr/share/nginx/html

# Copia um arquivo de config nginx (opcional)
COPY config/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]