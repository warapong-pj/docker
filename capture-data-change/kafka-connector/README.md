# kafka-connect

### initial kafka cluster
1. generate cluster id `export CLUSTER_ID=$(docker run --rm confluentinc/cp-kafka:7.6.0 kafka-storage random-uuid)`
2. start kafka cluster `docker compose up -d`

### endpoint
- schema-registry: http://localhost:8081/subjects
- connect(list, create and delete connector): http://localhost:8083/connectors/

### install plugin
- confluent-hub install debezium/debezium-connector-postgresql:latest --no-prompt

### check message
- kafka-topics --bootstrap-server kafka1:9092 --list
- kafka-console-consumer --bootstrap-server kafka1:29092 --topic poc-pg-change.inventory.customers --from-beginning
