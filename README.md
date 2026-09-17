
# Gerador de código
Esse é um gerador de código feito como exercício do livro "O Programador Pragmático".

Enunciado:
> Exercício 13: de Geradores de Código na página 128
> 
> Crie um gerador de código que pegue o arquivo de entrada da Figura 3.4 e
> gere saída em duas linguagens à sua escolha. Tente tornar fácil adicionar
> novas linguagens.

## Como adicionar uma nova linguagem
Em ```./generators```, adicione o arquivo python referente ao gerador de código da linguagem desejada. Ele deve implementar a classe ```BaseGenerator```.
Os arquivos são importados em runtime, então não é necessário alterar nada no arquivo principal.