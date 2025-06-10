from sly import Parser
from obsact_lexer import ObsActLexer 

# Language generator classes
class LangC:
    @staticmethod
    def program(devices, cmds):
        c_code = '#include <stdio.h>\n\n' + \
                 'void ligar(char* dev) { printf("%s ligado!\\n", dev); }\n' + \
                 'void desligar(char* dev) { printf("%s desligado!\\n", dev); }\n' + \
                 'void alerta(char* dev, char* msg) { printf("%s recebeu o alerta:\\n%s\\n", dev, msg); }\n' + \
                 'void alerta_com_obs(char* dev, char* msg, int obs) { printf("%s recebeu o alerta:\\n%s %d\\n", dev, msg, obs); }\n\n' + \
                 'int main() {\n' + \
                 ''.join(cmds) + \
                 'return 0;\n}\n'
        return c_code
    
    @staticmethod
    def set_var(var_name, value):
        return f'int {var_name} = {value};\n'
    
    @staticmethod
    def action_cmd(action, device):
        return f'{action}("{device}");\n'
    
    @staticmethod
    def send_alert(device, message):
        return f'alerta("{device}", "{message}");\n'
    
    @staticmethod
    def send_alert_with_obs(device, message, obs):
        return f'alerta_com_obs("{device}", "{message}", {obs});\n'
    
    @staticmethod
    def send_alert_to_all(message, devices):
        return ''.join([f'alerta("{name}", "{message}");\n' for name in devices])
    
    @staticmethod
    def if_then(obs, act):
        return f'if ({obs}) {{ {act} }}\n'
    
    @staticmethod
    def if_then_else(obs, act1, act2):
        return f'if ({obs}) {{ {act1} }} else {{ {act2} }}\n'
    
    @staticmethod
    def convert_bool(value):
        return '1' if value else '0'
    
    @staticmethod
    def get_action_name(action):
        return action  # In C, we use the function names directly
    
    @staticmethod
    def format_obs(var, op, value):
        return f'{var} {op} {value}'
    
    @staticmethod
    def format_obs_and(var, op, value, rest):
        return f'({var} {op} {value} && {rest})'

class LangJava:
    @staticmethod
    def program(devices, cmds):
        java_code = 'public class ObsActProgram {\n' + \
                   '    public static void ligar(String dev) { System.out.println(dev + " ligado!"); }\n' + \
                   '    public static void desligar(String dev) { System.out.println(dev + " desligado!"); }\n' + \
                   '    public static void alerta(String dev, String msg) { System.out.println(dev + " recebeu o alerta:\\n" + msg); }\n' + \
                   '    public static void alerta_com_obs(String dev, String msg, int obs) { System.out.println(dev + " recebeu o alerta:\\n" + msg + " " + obs); }\n\n' + \
                   '    public static void main(String[] args) {\n' + \
                   ''.join(['        ' + cmd for cmd in cmds]) + \
                   '    }\n}\n'
        return java_code
    
    @staticmethod
    def set_var(var_name, value):
        return f'int {var_name} = {value};\n'
    
    @staticmethod
    def action_cmd(action, device):
        return f'{action}("{device}");\n'
    
    @staticmethod
    def send_alert(device, message):
        return f'alerta("{device}", "{message}");\n'
    
    @staticmethod
    def send_alert_with_obs(device, message, obs):
        return f'alerta_com_obs("{device}", "{message}", {obs});\n'
    
    @staticmethod
    def send_alert_to_all(message, devices):
        return ''.join([f'alerta("{name}", "{message}");\n' for name in devices])
    
    @staticmethod
    def if_then(obs, act):
        return f'if ({obs}) {{ {act} }}\n'
    
    @staticmethod
    def if_then_else(obs, act1, act2):
        return f'if ({obs}) {{ {act1} }} else {{ {act2} }}\n'
    
    @staticmethod
    def convert_bool(value):
        return 'true' if value else 'false'
    
    @staticmethod
    def get_action_name(action):
        return action  # In Java, we use the method names directly
    
    @staticmethod
    def format_obs(var, op, value):
        return f'{var} {op} {value}'
    
    @staticmethod
    def format_obs_and(var, op, value, rest):
        return f'({var} {op} {value} && {rest})'

class LangJS:
    @staticmethod
    def program(devices, cmds):
        js_code = 'function ligar(dev) { console.log(dev + " ligado!"); }\n' + \
                 'function desligar(dev) { console.log(dev + " desligado!"); }\n' + \
                 'function alerta(dev, msg) { console.log(dev + " recebeu o alerta:\\n" + msg); }\n' + \
                 'function alerta_com_obs(dev, msg, obs) { console.log(dev + " recebeu o alerta:\\n" + msg + " " + obs); }\n\n' + \
                 '// Main program\n' + \
                 ''.join(cmds)
        return js_code
    
    @staticmethod
    def set_var(var_name, value):
        return f'let {var_name} = {value};\n'
    
    @staticmethod
    def action_cmd(action, device):
        return f'{action}("{device}");\n'
    
    @staticmethod
    def send_alert(device, message):
        return f'alerta("{device}", "{message}");\n'
    
    @staticmethod
    def send_alert_with_obs(device, message, obs):
        return f'alerta_com_obs("{device}", "{message}", {obs});\n'
    
    @staticmethod
    def send_alert_to_all(message, devices):
        return ''.join([f'alerta("{name}", "{message}");\n' for name in devices])
    
    @staticmethod
    def if_then(obs, act):
        return f'if ({obs}) {{ {act} }}\n'
    
    @staticmethod
    def if_then_else(obs, act1, act2):
        return f'if ({obs}) {{ {act1} }} else {{ {act2} }}\n'
    
    @staticmethod
    def convert_bool(value):
        return 'true' if value else 'false'
    
    @staticmethod
    def get_action_name(action):
        return action
    
    @staticmethod
    def format_obs(var, op, value):
        return f'{var} {op} {value}'
    
    @staticmethod
    def format_obs_and(var, op, value, rest):
        return f'({var} {op} {value} && {rest})'

# Set the current parser language (can be changed as needed)
parser_atual = LangC  # Options: LangC, LangJava, LangJS

class ObsActParser(Parser):
    tokens = ObsActLexer.tokens
    
    # Define the start symbol
    start = 'program'

    def __init__(self, lang_class=None):
        self.devices = []
        self.output = []
        self.lang = lang_class or parser_atual

    @_('devices cmds')
    def program(self, p):
        return self.lang.program(p[0], p[1])

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

    @_('SET ID "=" var')
    def cmd(self, p):
        return self.lang.set_var(p[1], p[3])

    @_('action ID')
    def cmd(self, p):
        return self.lang.action_cmd(p[0], p[1])

    @_('ENVIAR ALERTA "(" MSG ")" ID')
    def cmd(self, p):
        return self.lang.send_alert(p[5], p[3])

    @_('ENVIAR ALERTA "(" MSG "," ID ")" ID')
    def cmd(self, p):
        return self.lang.send_alert_with_obs(p[7], p[3], p[5])

    @_('ENVIAR ALERTA "(" MSG ")" PARATODOS ":" namelist')
    def cmd(self, p):
        return self.lang.send_alert_to_all(p[3], p[7])

    @_('SE obs ENTAO act')
    def cmd(self, p):
        return self.lang.if_then(p[1], p[3])

    @_('SE obs ENTAO act SENAO act')
    def cmd(self, p):
        return self.lang.if_then_else(p[1], p[3], p[5])

    @_('NUM')
    def var(self, p):
        return str(p[0])

    @_('BOOL')
    def var(self, p):
        return self.lang.convert_bool(p[0])

    @_('LIGAR')
    def action(self, p):
        return self.lang.get_action_name('ligar')

    @_('DESLIGAR')
    def action(self, p):
        return self.lang.get_action_name('desligar')

    # Define ACT as an action on a device
    @_('action ID')
    def act(self, p):
        return self.lang.action_cmd(p[0], p[1])

    @_('ID "," namelist')
    def namelist(self, p):
        return [p[0]] + p[2]

    @_('ID')
    def namelist(self, p):
        return [p[0]]

    @_('ID oplogic var')
    def obs(self, p):
        return self.lang.format_obs(p[0], p[1], p[2])

    @_('ID oplogic var AND obs')
    def obs(self, p):
        return self.lang.format_obs_and(p[0], p[1], p[2], p[4])

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