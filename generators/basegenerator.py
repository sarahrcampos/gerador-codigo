from abc import ABC, abstractmethod

class BaseGenerator(ABC):
    def __init__(self, file_name):
        self.command2method = {
            'M': self.generateMessage,
            'F': self.generateField,
            'E': self.generateEndOfMessage,
        }
        self.file_name = file_name
        print("Initializing BaseGenerator with file_name:", self.file_name)
    
    def generate(self, content: list[str]):
        buffer = []
        for line in content[1:]:
            if not line:
                continue
            buffer.append(self.command2method.get(line[0], lambda x: None)(line[2:]))
        self.save(buffer)

    @abstractmethod
    def generateMessage(self, message: str):
        pass

    @abstractmethod
    def generateField(self, field: str):
        pass

    @abstractmethod
    def generateEndOfMessage(self, endOfMessage: str):
        pass


    @abstractmethod
    def save(self, buffer: list[str]):
        pass