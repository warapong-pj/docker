from kafka import KafkaProducer
from kafka.errors import KafkaError
from json import dumps
from time import sleep

def main():
    try:
        producer=KafkaProducer(
            bootstrap_servers=["localhost:9092"],
            value_serializer=lambda v: dumps(v).encode("utf-8")
        )

        for i in range(1000):
            producer.send("test-topic", {"data": i})
            sleep(5)

    except KafkaError as exception:
        print(exception)
        exit()

if __name__ == "__main__":
    main()
