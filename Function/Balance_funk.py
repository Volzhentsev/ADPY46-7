from Class.Stack_class import Stack
def balance_brakets(data: list):
    s = Stack()
    balance = True
    if len(data) % 2 != 1:
        for el in data:
            if el in'([{':
                s.push(el)
            elif el in ')]}':
                if s.size() == None:
                    balance = False
                    break
                open_char = s.pop()
                if open_char == '(' and el == ')':
                    continue
                if open_char == '[' and el == ']':
                    continue
                if open_char == '{' and el == '}':
                    continue
                balance = False
                break
        if balance and s.size() == None:
            print('Сбалансированно')
        else:
            print('Несбалансированно')
    else:
        print('Несбалансированно')