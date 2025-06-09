from obsact_lexer import ObsActLexer
from obsact_parser import ObsActParser

with open("entrada.txt", "r", encoding="utf-8") as f:
    data = f.read()

lexer = ObsActLexer()
parser = ObsActParser()

result = parser.parse(lexer.tokenize(data))

with open("saida.c", "w") as f:
    if result:
        f.write(result)
    else:
        print("Erro: Nenhum código foi gerado")