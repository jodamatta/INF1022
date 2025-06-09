from sly import Lexer

class ObsActLexer(Lexer):
    tokens = {
        NUM, BOOL, ID, OBSERVATION, MSG,
        GT, LT, GE, LE, EQ, NE,
        AND,
        SET, SE, ENTAO, SENAO,
        ENVIAR, ALERTA,
        LIGAR, DESLIGAR,
        DISPOSITIVO, PARATODOS
    }

    literals = {':', ',', '{', '}', '(', ')', '.'}

    ignore = ' \t'
    ignore_comment = r'\#.*'

    # Keywords (these need to be defined before the general ID pattern)
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

    # Operators
    AND = r'&&'
    GE  = r'>='  # >= must come before >
    LE  = r'<='  # <= must come before <
    NE  = r'!='  # != must come before =
    EQ  = r'=='  # == must come before =
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

    # General identifier pattern - this should come after all keywords
    @_(r'[a-zA-Z_][a-zA-Z0-9_]*')
    def ID(self, t):
        # Check if it's a keyword, if so return the appropriate token type
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
            # Check if this looks like an observation variable (lowercase)
            if t.value.islower():
                t.type = 'OBSERVATION'
            else:
                t.type = 'ID'  # Device names, etc.
        return t

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    def error(self, t):
        print(f"Caractere ilegal '{t.value[0]}' na linha {self.lineno}")
        self.index += 1