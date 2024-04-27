from abc import ABC, abstractmethod


class BaseModel(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def predict(self, image, **kwargs):
        pass
