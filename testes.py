#!/usr/bin/env python3

from obsact_lexer import ObsActLexer
from obsact_parser import ObsActParser, LangC, LangJava, LangJS

def test_obsact_compiler():
    obsact_code = """
    dispositivo: {Sensor1, temperatura}
    dispositivo: {Lampada1}
    dispositivo: {Sensor2, umidade}
    
    set temperatura = 25.
    set umidade = 60.
    
    ligar lampada1.
    
    se temperatura > 30 entao ligar sensor1.
    
    se temperatura > 35 && umidade < 40 entao 
        enviar alerta ("Temperatura alta e umidade baixa!") sensor1
    senao 
        desligar sensor1.
    
    enviar alerta ("Sistema inicializado") para todos: sensor1, lampada1, sensor2.
    """
    languages = {
        'C': LangC,
        'Java': LangJava,
        'JavaScript': LangJS
    }
    
    lexer = ObsActLexer()
    
    for lang_name, lang_class in languages.items():
        print(f"\n{'='*50}")
        print(f"Compilando em {lang_name}")
        print(f"{'='*50}")
        
        try:
            parser = ObsActParser(lang_class)
            tokens = lexer.tokenize(obsact_code)
            result = parser.parse(tokens)
            
            if result:
                print(result)
            else:
                print("Compilacao falhou!")
                
        except Exception as e:
            print(f"Erro durante a compilacao: {e}")

def test_semantic_errors():
    print("\n" + "="*60)
    print("ERROS SEMANTICOS")
    print("="*60)

    test_cases = [
        {
            "name": "device nao declarado em ligar",
            "code": """
            dispositivo: {sensor1, temperatura}
            ligar lampada_inexistente.
            """
        },
        {
            "name": "device nao declarado em enviar alerta",
            "code": """
            dispositivo: {sensor1, temperatura}
            enviar alerta ("teste") dispositivo_inexistente.
            """
        },
        {
            "name": "device desligado",
            "code": """
            dispositivo: {sensor1, temperatura}
            dispositivo: {sensor1, umidade}
            ligar sensor1.
            """
        },
        {
            "name": "varios erros semanticos",
            "code": """
            dispositivo: {sensor1, temperatura}
            set pressao = 25.
            ligar lampada_inexistente.
            se temperatura > 30 entao ligar outro_inexistente.
            """
        }
    ]
    
    lexer = ObsActLexer()
    
    for test_case in test_cases:
        print(f"\nTeste: {test_case['name']}")
        print("-" * 40)
        
        try:
            parser = ObsActParser(LangC)
            tokens = lexer.tokenize(test_case['code'])
            result = parser.parse(tokens)
            print("❌ Esperava erro, mas a analise lexica foi bem-sucedida!")
            
        except SyntaxError as e:
            print(f"✅ Erro corretamente detectado: {e}")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")

def test_lexical_errors():
    print("\n" + "="*60)
    print("ERROS LEXICOS")
    print("="*60)
    
    # Test cases with lexical errors
    test_cases = [
        {
            "name": "caractere invalido @",
            "code": """
            dispositivo: {sensor1, temperatura}
            set temperatura = 25@.
            """
        },
        {
            "name": "caractere invalido ?",
            "code": """
            dispositivo: {sensor1, temperatura}
            ligar sensor1?.
            """
        },
        {
            "name": "caractere invalido $",
            "code": """
            dispositivo: {sensor$1, temperatura}
            """
        }
    ]
    
    lexer = ObsActLexer()
    
    for test_case in test_cases:
        print(f"\nTeste: {test_case['name']}")
        print("-" * 40)
        
        try:
            tokens = list(lexer.tokenize(test_case['code']))
            print("❌ Esperava erro, mas a analise lexica foi bem-sucedida!")
            
        except SyntaxError as e:
            print(f"✅ Erro corretamente detectado: {e}")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    print("\n\nTestando compilador ObsAct...")
    test_obsact_compiler()
    
    print("\n\nTestando erro de compilacao...")
    test_semantic_errors()
    test_lexical_errors()