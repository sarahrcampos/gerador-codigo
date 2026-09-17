from importlib import import_module
from inspect import isabstract, isclass
from pathlib import Path

from generators.basegenerator import BaseGenerator


p = Path('.')
generators_path = p / 'generators'

# recuperar todos os arquivos geradores de código 
generator_classes = []
for generator_file in generators_path.glob('*.py'):
    if generator_file.stem == 'basegenerator':
        continue

    module = import_module(f'generators.{generator_file.stem}')
    for candidate in module.__dict__.values():
        if (
            isclass(candidate)
            and issubclass(candidate, BaseGenerator)
            and candidate is not BaseGenerator
            and not isabstract(candidate)
        ):
            generator_classes.append(candidate)


#recuperar todos os arquivos .message
models = list(p.glob('**/models/*.message'))

content = []
for model in models:    
    fileContent = [model]
    with model.open('r') as f:
        fileContent = fileContent + f.readlines()
    content.append(fileContent)

print(content)

for model in content:
    for generator_class in generator_classes:    
        generator = generator_class(model[0])
        generator.generate(model)