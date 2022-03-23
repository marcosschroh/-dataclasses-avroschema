Minimal redis [example](https://github.com/marcosschroh/dataclasses-avroschema/tree/master/examples#dataclasses-avroschema-and-redis-streams-with-walrus) using `redis streams` with [walrus](https://github.com/coleifer/walrus) driver.

```python
from dataclasses import dataclass
import enum
import random
from time import sleep

from walrus import Database  # A subclass of the redis-py Redis client.

from dataclasses_avroschema import AvroModel, types


class FavoriteColor(enum.Enum):
    BLUE = "Blue"
    YELLOW = "Yellow"
    GREEN = "Green"

@dataclass
class UserModel(AvroModel):
    "An User"
    name: str
    age: int
    favorite_colors: FavoriteColor = FavoriteColor.BLUE
    country: str = "Argentina"
    address: str = None
    testing: bool = False

    class Meta:
        namespace = "User.v1"
        aliases = ["user-v1", "super user"]


def consume(consumer_group):
    # read new messages in the stream

    while True:
        result = consumer_group.my_stream.read(count=1, block=1000)
        # Each record has the followinf format
        # [(b'1598545738231-0', {b'message': b'\x06KimT\x00\x12Argentina\x00\x00'})]

        if result:
            message_id, message_content = result[0]

            if message_id:
                value = message_content[b'message']
                print(f"Processing message {message_id} with value {value}")
                user = UserModel.deserialize(value)
                print(user)


def produce(consumer_group):
    for i in range(10):
        # create an instance of User v1
        user = UserModel(
            name=random.choice(["Juan", "Peter", "Michael", "Moby", "Kim",]),
            age=random.randint(1, 50)
        )

        msgid = consumer_group.my_stream.add({"message": user.serialize()})
        print(f"Producing message {msgid}")

    print("Producer finished....")
    print("#" * 80)
    sleep(2)


if __name__ == "__main__":
    db = Database()
    stream_name = 'my-stream'
    db.Stream(stream_name)  # Create a new stream instance

    # create the consumer group
    consumer_group = db.consumer_group('my-consumer-group-1', [stream_name])
    consumer_group.create()  # Create the consumer group.
    consumer_group.set_id('$')

    produce(consumer_group)
    consume(consumer_group)
```

*(This script is complete, it should run "as is")*
