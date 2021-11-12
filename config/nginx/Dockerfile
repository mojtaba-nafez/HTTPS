FROM nginx:1.15
LABEL MAINTAINER="mojtaba_nafez"

COPY localhost.crt /etc/ssl/certs/localhost.crt
COPY localhost.key /etc/ssl/private/localhost.key

COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]