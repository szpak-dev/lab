FROM caddy:2.6.1-alpine

COPY ./Caddyfile /etc/caddy/

RUN caddy fmt /etc/caddy/Caddyfile --overwrite
