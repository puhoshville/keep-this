from pymemcache import serde
from pymemcache.client import base


class MemcachedConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def __enter__(self):
        self.connection = base.Client(
            (self.host, self.port),
            serializer=serde.python_memcache_serializer,
            deserializer=serde.python_memcache_deserializer,
        )
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
