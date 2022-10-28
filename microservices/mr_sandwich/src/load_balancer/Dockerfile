FROM caddy:2.6.1-alpine

ENV DOMAIN=mr_sandwich.localhost
ENV LOG_LEVEL=warn

COPY ./Caddyfile /etc/caddy/

RUN caddy fmt /etc/caddy/Caddyfile --overwrite

CMD ["caddy", "run", \
     "--config", "/etc/caddy/Caddyfile", \
     "--adapter", "caddyfile" \
]