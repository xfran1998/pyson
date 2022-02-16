import json
import operator
import re
from numpy import array

class JSON_Program:
    def __init__(self, path):
        self.vars = {}
        self.path = path

        self.operations = self.get_program()

    def get_program(self):
        f = open(self.path)
        data = json.load(f)
        f.close()

        if not 'start' in data:
            raise Exception("No start setted in bot_actions.js")

        return data['start']

    def set_vars(self, vars):
        for name in vars:
            self.vars[name] = vars[name]

    def get_var_from_string(self, pos, pos_end, string):
        pos = string.find('${', pos)
        pos_end = string.find('}', pos+2)
        var = string[(pos+2):(pos_end)]

        return var, pos, pos_end

    def replace_var_from_string(self, pos, pos_end, string, var):
        string = string[:pos] + str(self.vars[var]) + string[pos_end+1:]
        return string

    def get_value(self, var_name):
        return self.vars[var_name]

    def get_print(self, string):
        pos_end = len(string)
        pos = 0        

        var, pos, pos_end = self.get_var_from_string(pos, pos_end, string)

        while (pos != -1):
            # print(f"pos: {pos}")
            # print(f"pos_end: {pos_end}")
            if pos_end == -1:
                raise Exception("Error creating variable, missing }")
            

            if not self.is_var_setted(var):
                output = f"Accessing variable not setted: {var}"
                raise Exception(output)
                
            string = self.replace_var_from_string(pos, pos_end, string, var)
            # print(f"string: {string}")
            var, pos, pos_end = self.get_var_from_string(pos, pos_end, string)


        return string

    def set_value(self, name, value):
        self.vars[name] = value

    def loop(self, operation):
        if 'times' not in operation:
            raise Exception("No times setted in loop")

        times = operation['times']

        if 'condition' in operation:
            condition = operation['condition']
        else:
            condition = None

        if condition is not None or condition is False:
            pass

        for _i in range(times):
            self.do_op(operation)

    def split_calc_term(self, operation):
        # first_split = re.split(r'\s', operation)

        # while '' in first_split:
        #     first_split.remove('')
        splited = re.findall(r'[a-z,1-9]+|\^|\*|-|\+|=|/|\$\{.\}+', operation)

        for var in splited:
            error_var = re.findall(r'^[1-9].*[a-z]', var)
            if len(error_var) > 0:
                output = f"Error in operation expresion, Not valid name variable: {error_var[0]}"
                raise Exception(output)

        if splited.count('=') > 1:
            raise Exception("Error in operation expresion, only allowed '=' once")
        
        if not self.is_var_setted(splited[0]):
            raise Exception("Error in operation expresion, first parameter should be a variable already setted")
        
        if splited[1] != '=':
            raise Exception("Error in operation expresion, '=' should be second parameter in expresion (x = x + 1)")
                
        return splited

    def is_valid_var(self, string):
        var = re.findall(r'^[a-z].*[1-9]*', string)
        if len(var) > 0:
            return True
        
        return False

    def is_rvalue(self, string):
        var = re.findall(r'^[a-z]|^[0-9]', string)
        if len(var) > 0:
            return True
        
        return False

    def check_op_list(self, op_list):
        allowed_op = ['+', '-', '*', '/', '^', '=']

        is_var = True

        for var in op_list:
            if is_var != self.is_rvalue(var):
                output = f"Error in operation expresion, invalid '{var}'. Varible must be followed by allowed operator (+,-,*,/,^)"
                raise Exception(output)

            # Check if var is already setted
            if is_var and self.is_valid_var(var):
                if not self.is_var_setted(var):
                    output = f"Error in operation expresion, invalid '{var}'. Varible must be initiallized before using it"
                    raise Exception(output)

            is_var = not is_var

        if is_var:
            raise Exception("Error in operation expresion, last term can't be a operator")
    
    def is_var_setted(self, var):
        if var in self.vars:
            return True
        return False

    def convert_str_to_var(self, string):
        if self.is_var_setted(string):
            value = self.get_value(string)
        else:
            value = int(string)

        return value

    def calc_operation(self, x, y, op):
        if op == '+':
            return x+y
        if op == '-':
            return x-y
        if op == '*':
            return x*y
        if op == '/':
            return x/y
        if op == '^':
            return x**y

    def calculate(self, operation):
        # print(operation)
        op_list = self.split_calc_term(operation)
        self.check_op_list(op_list)

        value = self.convert_str_to_var(op_list[2])
        i = 4

        while (i < len(op_list)):
            value2 = self.convert_str_to_var(op_list[i])
            value = self.calc_operation(value, value2, op_list[i-1])
            
            i += 2

        # print(op_list)
        # print(f'value2: {value2}')

        self.set_value(op_list[0], value)


    def start(self):
        self.do_op(self.operations)

    def do_specific_op(self, op, new_operation):
        if op == 'var':
            self.set_vars(new_operation)
        elif op == 'print':
            print_string = self.get_print(new_operation)
            print(print_string)
        elif op == 'loop':
            self.loop(new_operation)
        elif op == 'operation':
            self.calculate(new_operation)
        else:
            self.do_op(new_operation)

    def do_op(self, opetaration):
        if type(opetaration) is dict:
            for op in opetaration:
                new_operation = opetaration[op]
                self.do_specific_op(op, new_operation)

        elif type(opetaration) is list:
            for op in opetaration:
                new_operation = op
                self.do_specific_op(op, new_operation)      
                # print('op1:', op)
                # print('new1:', new_operation)
        else:
            # print('op2:', type(opetaration))
            pass


if __name__ == "__main__":
    program_path = 'main.json'

    prog = JSON_Program(program_path)
    prog.start()

