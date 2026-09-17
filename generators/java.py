from generators.basegenerator import BaseGenerator

class JavaGenerator(BaseGenerator):
    def __init__(self, file_name):
        print("JavaGenerator initialized")
        self.dsl2java = {
            'int': 'int',
            'char': 'String'
        }
        super().__init__(file_name)

    def generateMessage(self, message: str):
        return f"public class {message.strip()} {{"

    def generateField(self, field: str):
        field_name, field_type = field.split()
        field_type = ''.join(filter(str.isalpha, field_type))
        field = f"private {self.dsl2java.get(field_type, 'Object')} {field_name};"
        return f"    {field}"

    def generateEndOfMessage(self, endOfMessage: str):
        return "}"

    def save(self, buffer: list[str]):
        with open("./generated-code/" + self.file_name.stem + ".java", "w") as f:
            f.write("\n".join(filter(None, buffer)))