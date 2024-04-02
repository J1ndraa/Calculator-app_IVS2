class InputArgs:
    def __init__(self, input):
        self._equation = []
        self.tmp_string = ""
        for line in input:
            for string in line.split():
                for char in string:
                    if char:
                        if not char.isdigit():
                            if len(self.tmp_string) != 0:
                                self._equation.append(self.tmp_string)
                                self.tmp_string = ""
                            self._equation.append(char)
                            continue
                        self.tmp_string += char

        if len(self.tmp_string) != 0:
            self._equation.append(self.tmp_string)
            self.tmp_string = ""

        self._equation.append('=')

    def get_equation(self):
        return self._equation

    def print_equation(self):
        print(self._equation)
