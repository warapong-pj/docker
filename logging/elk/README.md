# elk

### step to initial
1. docker compose exec -i -t elasticsearch /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic
2. docker compose exec -i -t elasticsearch /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana
3. docker compose exec -i -t kibana /usr/share/kibana/bin/kibana-verification-code
4. chown root:root filebeat.yml
