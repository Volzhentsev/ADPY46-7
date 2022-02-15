from Function.Balance_funk import balance_brakets

str_1 = '(((([{}]))))'
str_2 = '[([])((([[[]]])))]{()}'
str_3 = '{{[()]}}'
str_4 = '}{}'
str_5 = '{{[(])]}}'
str_6 = '[[{())}]'

if __name__ == '__main__':

    balance_brakets(str_1)
    balance_brakets(str_2)
    balance_brakets(str_3)
    balance_brakets(str_4)
    balance_brakets(str_5)
    balance_brakets(str_6)
