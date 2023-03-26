from kafka import KafkaConsumer
from kafka.errors import KafkaError
from json import loads

def main():
    try:
        consumer=KafkaConsumer(
            bootstrap_servers=["localhost:9092"],
            value_deserializer=lambda m: loads(m.decode("utf-8"))
        )
        consumer.subscribe(["test-topic"])

        for message in consumer:
            print(message.value)

    except KafkaError as exception:
        print(exception)
        exit()

if __name__ == "__main__":
    main()
