# Variáveis: espaço na memória para armazenar valores
age = 29                    # int
name = "Luiz"               # str
print(f'Meu nome é {name} e tenho {age} anos.')

# Atribuição múltipla: várias variáveis em uma linha
age, name = (29, "Luiz")
print(f'Meu nome é {name} e tenho {age} anos.')

# Reatribuição: variáveis podem mudar de valor
age, name = (27, 'Gabriela')
print(f'Meu nome é {name} e tenho {age} anos.')

# Constantes: por convenção, nomes em MAIÚSCULAS
AMOUNT = 1000
STATES = ['SP', 'RJ', 'MG', 'ES']