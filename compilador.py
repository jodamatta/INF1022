from obsact_lexer import ObsActLexer
from obsact_parser import ObsActParser, LangC, LangJava, LangJS

with open("entrada.txt", "r", encoding="utf-8") as f:
    data = f.read()

lexer = ObsActLexer()

# lista de linguagens e suas configurações
languages = [
    {"class": LangC, "extension": ".c", "name": "C"},
    {"class": LangJava, "extension": ".java", "name": "Java"},
    {"class": LangJS, "extension": ".js", "name": "JavaScript"}
]

for lang_config in languages:
    try:
        # criar o parser para a linguagem atual
        parser = ObsActParser(lang_config["class"])
        
        # parse + geracao de codigo
        result = parser.parse(lexer.tokenize(data))
        
        # salvar na extensao correta
        output_filename = f"saida{lang_config['extension']}"
        
        if result:
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(result)
            print(f"✓ {lang_config['name']} código gerado com sucesso: {output_filename}")
        else:
            print(f"✗ Erro: Nenhum código {lang_config['name']} foi gerado.")
            
    except Exception as e:
        print(f"✗ Erro gerando código {lang_config['name']}: {str(e)}")