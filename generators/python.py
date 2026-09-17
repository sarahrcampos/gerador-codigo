from generators.basegenerator import BaseGenerator

class PythonGenerator(BaseGenerator):
    def __init__(self, file_name):
        print("PythonGenerator initialized")
        self.dsl2python = {
            'int': 'int',
            'char': 'str'            
        }
        super().__init__(file_name)

    def generateMessage(self, message: str):        
        return f"class {message.strip()}:"

    def generateField(self, field: str):
        field_name, field_type = field.split()
        field_type = ''.join(filter(str.isalpha, field_type))
        field = f"{field_name}: {self.dsl2python.get(field_type, 'Any')}"
        return f"    {field}"

    def generateEndOfMessage(self, endOfMessage: str):
        return ""

    def save(self, buffer: list[str]):
        with open("./generated-code/" + self.file_name.stem + ".py", "w") as f:
            f.write("\n".join(filter(None, buffer)))