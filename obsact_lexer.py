from sly import Lexer

class ObsActLexer(Lexer):
    tokens = {
        NUM, BOOL, ID, MSG,
        GT, LT, GE, LE, EQ, NE,
        AND,
        SET, SE, ENTAO, SENAO,
        ENVIAR, ALERTA,
        LIGAR, DESLIGAR,
        DISPOSITIVO, PARATODOS
    }

    literals = {':', ',', '{', '}', '(', ')', '.', '='}

    ignore = ' \t'
    ignore_comment = r'\#.*'

    SET      = r'set'
    SE       = r'se'
    ENTAO    = r'entao'
    SENAO    = r'senao'
    ENVIAR   = r'enviar'
    ALERTA   = r'alerta'
    LIGAR    = r'ligar'
    DESLIGAR = r'desligar'
    DISPOSITIVO = r'dispositivo'
    PARATODOS   = r'para\s+todos'

    AND = r'&&'
    GE  = r'>='  
    LE  = r'<='  
    NE  = r'!='  
    EQ  = r'=='  
    GT  = r'>'
    LT  = r'<'

    @_(r'TRUE|FALSE')
    def BOOL(self, t):
        t.value = True if t.value == "TRUE" else False
        return t

    @_(r'\d+')
    def NUM(self, t):
        t.value = int(t.value)
        return t

    @_(r'"[^"]*"')
    def MSG(self, t):
        t.value = t.value.strip('"')
        return t

    @_(r'=')
    def EQ(self, t):
        return t

    @_(r'[a-zA-Z_][a-zA-Z0-9_]*')
    def ID(self, t):
        if t.value.lower() in {
            'set', 'se', 'entao', 'senao', 'enviar', 'alerta', 
            'ligar', 'desligar', 'dispositivo'
        }:
            t.type = t.value.upper()
        elif t.value in {'TRUE', 'FALSE'}:
            t.type = 'BOOL'
            t.value = True if t.value == "TRUE" else False
        elif t.value == 'para':
            t.type = 'PARATODOS'  # This will need special handling for "para todos"
        else:
            # For now, treat all non-keyword identifiers as either ID or OBSERVATION
            # We'll let the parser context determine the difference
            t.type = 'ID'
        return t

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    def error(self, t):
        print(f"✗ Erro léxico: Caractere ilegal '{t.value[0]}' na linha {self.lineno}")
        raise SyntaxError(f"Caractere ilegal '{t.value[0]}' na linha {self.lineno}")