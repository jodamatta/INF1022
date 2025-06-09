from sly import Parser
from obsact_lexer import ObsActLexer 

class ObsActParser(Parser):
    tokens = ObsActLexer.tokens
    
    # Define the start symbol
    start = 'program'

    def __init__(self):
        self.devices = []
        self.output = []

    @_('devices cmds')
    def program(self, p):
        c_code = '#include <stdio.h>\n\n' + \
                 'void ligar(char* dev) { printf("%s ligado!\\n", dev); }\n' + \
                 'void desligar(char* dev) { printf("%s desligado!\\n", dev); }\n' + \
                 'void alerta(char* dev, char* msg) { printf("%s recebeu o alerta:\\n%s\\n", dev, msg); }\n' + \
                 'void alerta_com_obs(char* dev, char* msg, int obs) { printf("%s recebeu o alerta:\\n%s %d\\n", dev, msg, obs); }\n\n' + \
                 'int main() {\n' + \
                 ''.join(p[1]) + \
                 'return 0;\n}\n'
        return c_code

    @_('device devices')
    def devices(self, p):
        return [p[0]] + p[1]

    @_('device')
    def devices(self, p):
        return [p[0]]

    @_('DISPOSITIVO ":" "{" ID "," ID "}"')
    def device(self, p):
        return (p[3], p[5])

    @_('DISPOSITIVO ":" "{" ID "}"')
    def device(self, p):
        return (p[3], None)

    @_('cmd "." cmds')
    def cmds(self, p):
        return [p[0]] + p[2]

    @_('cmd "."')
    def cmds(self, p):
        return [p[0]]

    @_('SET OBSERVATION EQ var')
    def cmd(self, p):
        return f'int {p[1]} = {p[3]};\n'

    @_('action ID')
    def cmd(self, p):
        return f'{p[0]}("{p[1]}");\n'

    @_('ENVIAR ALERTA "(" MSG ")" ID')
    def cmd(self, p):
        return f'alerta("{p[5]}", "{p[3]}");\n'

    @_('ENVIAR ALERTA "(" MSG "," OBSERVATION ")" ID')
    def cmd(self, p):
        return f'alerta_com_obs("{p[7]}", "{p[3]}", {p[5]});\n'

    @_('ENVIAR ALERTA "(" MSG ")" PARATODOS ":" namelist')
    def cmd(self, p):
        return ''.join([f'alerta("{name}", "{p[3]}");\n' for name in p[7]])

    @_('SE obs ENTAO act')
    def cmd(self, p):
        return f'if ({p[1]}) {{ {p[3]} }}\n'

    @_('SE obs ENTAO act SENAO act')
    def cmd(self, p):
        return f'if ({p[1]}) {{ {p[3]} }} else {{ {p[5]} }}\n'

    @_('NUM')
    def var(self, p):
        return str(p[0])

    @_('BOOL')
    def var(self, p):
        return '1' if p[0] else '0'

    @_('LIGAR')
    def action(self, p):
        return 'ligar'

    @_('DESLIGAR')
    def action(self, p):
        return 'desligar'

    # Define ACT as an action on a device
    @_('action ID')
    def act(self, p):
        return f'{p[0]}("{p[1]}");\n'

    @_('ID "," namelist')
    def namelist(self, p):
        return [p[0]] + p[2]

    @_('ID')
    def namelist(self, p):
        return [p[0]]

    @_('OBSERVATION oplogic var')
    def obs(self, p):
        return f'{p[0]} {p[1]} {p[2]}'

    @_('OBSERVATION oplogic var AND obs')
    def obs(self, p):
        return f'({p[0]} {p[1]} {p[2]} && {p[4]})'

    @_('GT')
    def oplogic(self, p):
        return p[0]
    
    @_('LT')
    def oplogic(self, p):
        return p[0]
    
    @_('GE')
    def oplogic(self, p):
        return p[0]
    
    @_('LE')
    def oplogic(self, p):
        return p[0]
    
    @_('EQ')
    def oplogic(self, p):
        return p[0]
    
    @_('NE')
    def oplogic(self, p):
        return p[0]

    def error(self, p):
        if p:
            print(f"Erro de sintaxe em '{p.value}' na linha {p.lineno}")
        else:
            print("Erro de sintaxe no final do arquivo")
