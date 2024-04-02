class Calculator:
    def __init__(self):
        self.postfix = []
        self.precedence = [
            ('+', 1),
            ('-', 1),
            ('*', 2),
            ('/', 2),
            ('%', 2),
            ('^', 3)
        ]

    def postfix_convert(self, stack, equation):
        for char in equation:
            if (char.isdigit()):
                self.postfix.append(char)
            elif (char == '('):
                stack.push(char)
            elif (char == ')'):
                self.untilLeftPar(stack)
            else:
                if (char == '='):
                    self.pop_stack(stack)

                self.operatorPrecedence(stack, char)

    def untilLeftPar(self, stack):
        while (stack.top() != '('):
            self.postfix.append(stack.pop())
        stack.pop()

    def operatorPrecedence(self, stack, char):
        if (stack.is_empty()):
            stack.push(char)
            return
        if (char == '(' or stack.top() == '('):
            stack.push(char)
            return
        if (self.get_precedence(char) > self.get_precedence(stack.top())):
            stack.push(char)
            return
        self.postfix.append(stack.pop())
        self.operatorPrecedence(stack, char)

    def pop_stack(self, stack):
        while (not stack.is_empty()):
            self.postfix.append(stack.pop())

        #self.print_postfix()

    def print_postfix(self):
        print("Postfix notation: ", end="")
        for char in self.postfix:
            print(char, end="")
        print("")

    def eval_expr(self, stack):
        for char in self.postfix:
            if char.isdigit():
                stack.push(char)
            else:
                val1, val2 = stack.pop_multiple()
                match char:
                    case '+':
                        result = val1 + val2
                        stack.push(result)
                    case '-':
                        result = val2 - val1
                        stack.push(result)
                    case '*':
                        result = val1 * val2
                        stack.push(result)
                    case '/':
                        result = val2 / val1
                        stack.push(result)
                    case '%':
                        result = val2 % val1
                        stack.push(result)
                    case '^':
                        result = val2 ** val1
                        stack.push(result)
                    case _  : 
                        exit(1)

    def print_result(self, stack):
        #print("Result: ", end="")
        result = stack.pop()
        if isinstance(result, float) and result.is_integer():
            print(int(result))
        else:
            print(result)

    def get_precedence(self, char):
        for op, prec in self.precedence:
            if op == char:
                return prec
        exit(1)
           