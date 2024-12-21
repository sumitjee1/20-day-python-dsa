#code to build compiler to do basic arithmatic evaluations
class SimpleCompiler:
    def __init__(self):
        self.variables = {}

    def process(self, code):
        lines = code.split('\n')
        
        for line in lines:
            line = line.strip()
            
            if not line:
                continue
            
            try:
                if '=' in line:
                    var, expr = line.split('=')
                    var = var.strip()
                    value = eval(expr, {}, self.variables)
                    self.variables[var] = value
                    print(f"{var} = {value}")
                else:
                    print(f"Output: {eval(line, {}, self.variables)}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    compiler = SimpleCompiler()
    code = """
    x = 10 + 5
    y = x * 2
    z = y - 4
    z / 2
    """
    compiler.process(code)
