# kafka-connect
### endpoint
- schema-registry: http://localhost:8081/subjects
- connect(list, create and delete connector): http://localhost:8083/connectors/

### install plugin
- confluent-hub install debezium/debezium-connector-postgresql:latest --no-prompt

### check message
- kafka-console-consumer --bootstrap-server kafka1:29092 --topic poc-pg-change.inventory.customers --from-beginning
