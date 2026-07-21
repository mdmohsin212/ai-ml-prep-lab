from threading import Lock
from typing import Any
import time

class ModelProvider:
    def __init__(self):
        self._model: Any = None
        self._lock = Lock()
    
    def get(self):
        if self._model is None:
            with self._lock:
                if self._model is None:
                    self._model = self._load()
        return self._model
    
    def _load(self):
        raise NotImplementedError
    
    
class MyModelProvider(ModelProvider):
    def _load(self):
        print("Loading model...")
        time.sleep(2)
        return "BIG_MODEL"


provider = MyModelProvider()
model1 = provider.get()
print(model1)

model2 = provider.get()
print(model2)