from sly import Parser
from obsact_lexer import ObsActLexer 

# Language generator classes
class LangC:
    @staticmethod
    def program(devices, cmds):
        # Store device names for reference
        device_names = [name for name, obs in devices]
        
        c_code = '#include <stdio.h>\n\n' + \
                 'void ligar(char* dev) { printf("%s ligado!\\n", dev); }\n' + \
                 'void desligar(char* dev) { printf("%s desligado!\\n", dev); }\n' + \
                 'void alerta(char* dev, char* msg) { printf("%s recebeu o alerta:\\n%s\\n", dev, msg); }\n' + \
                 'void alerta_com_obs(char* dev, char* msg, int obs) { printf("%s recebeu o alerta:\\n%s %d\\n", dev, msg, obs); }\n\n' + \
                 'int main() {\n' + \
                 ''.join(['    ' + cmd for cmd in cmds]) + \
                 '    return 0;\n}\n'
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
        return f'if ({obs}) {{\n        {act}    }}\n'
    
    @staticmethod
    def if_then_else(obs, act1, act2):
        return f'if ({obs}) {{\n        {act1}    }} else {{\n        {act2}    }}\n'
    
    @staticmethod
    def convert_bool(value):
        return '1' if value else '0'
    
    @staticmethod
    def get_action_name(action):
        return action
    
    @staticmethod
    def format_obs(var, op, value):
        return f'{var} {op} {value}'
    
    @staticmethod
    def format_obs_and(var, op, value, rest):
        return f'({var} {op} {value} && {rest})'

class LangJava:
    @staticmethod
    def program(devices, cmds):
        device_names = [name for name, obs in devices]
        
        java_code = 'public class saida {\n' + \
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
        return f'if ({obs}) {{\n            {act}        }}\n'
    
    @staticmethod
    def if_then_else(obs, act1, act2):
        return f'if ({obs}) {{\n            {act1}        }} else {{\n            {act2}        }}\n'
    
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

class LangJS:
    @staticmethod
    def program(devices, cmds):
        device_names = [name for name, obs in devices]
        
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
        return f'if ({obs}) {{\n    {act}}}\n'
    
    @staticmethod
    def if_then_else(obs, act1, act2):
        return f'if ({obs}) {{\n    {act1}}} else {{\n    {act2}}}\n'
    
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

parser_atual = LangC  # Options: LangC, LangJava, LangJS

class ObsActParser(Parser):
    tokens = ObsActLexer.tokens
    
    start = 'program'

    def __init__(self, lang_class=None):
        super().__init__()
        self.devices = []
        self.device_names = set()  # Track declared device names
        self.observation_names = set()  # Track declared observation names
        self.defined_variables = set()  # Track variables that have been explicitly set
        self.output = []
        self.lang = lang_class or parser_atual
        self.errors = []  # Track semantic errors

    def _check_length(self, value, name_type, max_length=100):
        """Helper method to check if a string exceeds maximum length"""
        if len(value) > max_length:
            self.errors.append(f"{name_type} '{value}' excede o limite de {max_length} caracteres (atual: {len(value)})")
            return False
        return True

    @_('devices cmds')
    def program(self, p):
        self.devices = p.devices
        
        # Initialize undefined variables used in observations to 0
        undefined_vars = []
        for obs_name in self.observation_names:
            if obs_name not in self.defined_variables:
                undefined_vars.append(self.lang.set_var(obs_name, '0'))
        
        # Check if there were any semantic errors
        if self.errors:
            error_msg = "Erros semânticos encontrados:\n" + "\n".join(self.errors)
            raise SyntaxError(error_msg)
        
        # Prepend undefined variable initializations to commands
        all_cmds = undefined_vars + p.cmds
        return self.lang.program(p.devices, all_cmds)

    @_('device devices')
    def devices(self, p):
        return [p.device] + p.devices

    @_('device')
    def devices(self, p):
        return [p.device]

    @_('DISPOSITIVO ":" "{" ID "," ID "}"')
    def device(self, p):
        device_name = p.ID0
        obs_name = p.ID1
        
        # Check character limits
        self._check_length(device_name, "Nome do dispositivo")
        self._check_length(obs_name, "Nome da observação")
        
        # Check for duplicate device names
        if device_name in self.device_names:
            self.errors.append(f"Dispositivo '{device_name}' já foi declarado")
        else:
            self.device_names.add(device_name)
            
        # Check for duplicate observation names
        if obs_name in self.observation_names:
            self.errors.append(f"Observação '{obs_name}' já foi declarada")
        else:
            self.observation_names.add(obs_name)
            
        return (device_name, obs_name)

    @_('DISPOSITIVO ":" "{" ID "}"')
    def device(self, p):
        device_name = p.ID
        
        # Check character limits
        self._check_length(device_name, "Nome do dispositivo")
        
        # Check for duplicate device names
        if device_name in self.device_names:
            self.errors.append(f"Dispositivo '{device_name}' já foi declarado")
        else:
            self.device_names.add(device_name)
            
        return (device_name, None)

    def _check_device_exists(self, device_name, context=""):
        """Helper method to check if a device exists"""
        if device_name not in self.device_names:
            self.errors.append(f"Dispositivo '{device_name}' não foi declarado{context}")
            return False
        return True
    
    def _check_observation_exists(self, obs_name, context=""):
        """Helper method to check if an observation exists"""
        if obs_name not in self.observation_names:
            self.errors.append(f"Observação '{obs_name}' não foi declarada{context}")
            return False
        return True
    
    @_('cmd "." cmds')
    def cmds(self, p):
        return [p.cmd] + p.cmds

    @_('cmd "."')
    def cmds(self, p):
        return [p.cmd]

    @_('SET ID "=" var')
    def cmd(self, p):
        # Check if the ID is a declared observation
        self._check_observation_exists(p.ID, " em comando de atribuição")
        # Mark this variable as defined
        self.defined_variables.add(p.ID)
        return self.lang.set_var(p.ID, p.var)

    @_('action ID')
    def cmd(self, p):
        # Check if the device exists
        self._check_device_exists(p.ID, " em comando de ação")
        return self.lang.action_cmd(p.action, p.ID)

    @_('ENVIAR ALERTA "(" MSG ")" ID')
    def cmd(self, p):
        # Check character limits for message
        self._check_length(p.MSG, "Mensagem de alerta")
        # Check if the device exists
        self._check_device_exists(p.ID, " em comando de alerta")
        return self.lang.send_alert(p.ID, p.MSG)

    @_('ENVIAR ALERTA "(" MSG "," ID ")" ID')
    def cmd(self, p):
        # Check character limits for message
        self._check_length(p.MSG, "Mensagem de alerta")
        # Check if the observation and device exist
        self._check_observation_exists(p.ID0, " em comando de alerta com observação")
        self._check_device_exists(p.ID1, " em comando de alerta com observação")
        return self.lang.send_alert_with_obs(p.ID1, p.MSG, p.ID0)

    @_('ENVIAR ALERTA "(" MSG ")" PARATODOS ":" namelist')
    def cmd(self, p):
        # Check character limits for message
        self._check_length(p.MSG, "Mensagem de alerta")
        # Check if all devices in the namelist exist
        for device in p.namelist:
            self._check_device_exists(device, " em comando de alerta para todos")
        return self.lang.send_alert_to_all(p.MSG, p.namelist)

    @_('SE obs ENTAO act')
    def cmd(self, p):
        return self.lang.if_then(p.obs, p.act)

    @_('SE obs ENTAO act SENAO act')
    def cmd(self, p):
        return self.lang.if_then_else(p.obs, p.act0, p.act1)

    @_('NUM')
    def var(self, p):
        return str(p.NUM)

    @_('BOOL')
    def var(self, p):
        return self.lang.convert_bool(p.BOOL)

    @_('LIGAR')
    def action(self, p):
        return self.lang.get_action_name('ligar')

    @_('DESLIGAR')
    def action(self, p):
        return self.lang.get_action_name('desligar')

    @_('action ID')
    def act(self, p):
        # Check if the device exists
        self._check_device_exists(p.ID, " em ação condicional")
        return self.lang.action_cmd(p.action, p.ID)

    @_('ENVIAR ALERTA "(" MSG ")" ID')
    def act(self, p):
        # Check character limits for message
        self._check_length(p.MSG, "Mensagem de alerta")
        # Check if the device exists
        self._check_device_exists(p.ID, " em ação de alerta condicional")
        return self.lang.send_alert(p.ID, p.MSG)

    @_('ENVIAR ALERTA "(" MSG "," ID ")" ID')
    def act(self, p):
        # Check character limits for message
        self._check_length(p.MSG, "Mensagem de alerta")
        # Check if the observation and device exist
        self._check_observation_exists(p.ID0, " em ação de alerta condicional com observação")
        self._check_device_exists(p.ID1, " em ação de alerta condicional com observação")
        return self.lang.send_alert_with_obs(p.ID1, p.MSG, p.ID0)

    @_('ID "," namelist')
    def namelist(self, p):
        # Check if the device exists
        self._check_device_exists(p.ID, " em lista de dispositivos")
        return [p.ID] + p.namelist

    @_('ID')
    def namelist(self, p):
        # Check if the device exists
        self._check_device_exists(p.ID, " em lista de dispositivos")
        return [p.ID]

    @_('ID oplogic var')
    def obs(self, p):
        # Check if the observation exists
        self._check_observation_exists(p.ID, " em condição")
        return self.lang.format_obs(p.ID, p.oplogic, p.var)

    @_('ID oplogic var AND obs')
    def obs(self, p):
        # Check if the observation exists
        self._check_observation_exists(p.ID, " em condição composta")
        return self.lang.format_obs_and(p.ID, p.oplogic, p.var, p.obs)

    @_('GT')
    def oplogic(self, p):
        return p.GT
    
    @_('LT')
    def oplogic(self, p):
        return p.LT
    
    @_('GE')
    def oplogic(self, p):
        return p.GE
    
    @_('LE')
    def oplogic(self, p):
        return p.LE
    
    @_('EQ')
    def oplogic(self, p):
        return p.EQ
    
    @_('NE')
    def oplogic(self, p):
        return p.NE

    def error(self, p):
        if p:
            error_msg = f"Erro de sintaxe em '{p.value}' na linha {p.lineno}"
            print(error_msg)
            raise SyntaxError(error_msg)
        else:
            error_msg = "Erro de sintaxe no final do arquivo"
            print(error_msg)
            raise SyntaxError(error_msg)