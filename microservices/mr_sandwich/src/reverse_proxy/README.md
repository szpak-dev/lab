# Reverse Proxy
Responsible for passing request to their respective microservices. This is where the SSL is terminated and HTTP
connection is established in order to save some processor's time.

## Hosts
| Service | Development host | Compose/Swarm host |
|--------|------------------|--------------------|
| Proxy  | -                | mr.localhost:443/* |