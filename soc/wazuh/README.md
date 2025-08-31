# wazuh stack
---
### how to start stack
1. docker compose -f generate-indexer-certs.yml run --rm generator
2. docker compose up -d

### how to cleanup stack
1. docker compose down --volumes