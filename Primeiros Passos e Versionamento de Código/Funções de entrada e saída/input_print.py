# =====================================================================
# FUNÇÕES DE ENTRADA E SAÍDA (input / print)
# =====================================================================

# ---------------------------------------------------------------------
# input(): entrada de dados do usuário
# ---------------------------------------------------------------------
# Pausa o programa, mostra a mensagem e aguarda o usuário digitar.
# O valor retornado é SEMPRE uma string (str).
nome = input('Informe seu nome: ')
print(f'Seu nome é {nome}.')

# ---------------------------------------------------------------------
# print(): saída de dados
# ---------------------------------------------------------------------
nome = "Guilherme"
sobrenome = "Silva"

# Vários argumentos são impressos separados por espaço
print(nome, sobrenome)              # Guilherme Silva

# end: define o que vai no FINAL da linha (padrão é \n - quebra de linha)
print(nome, sobrenome, end='...\n') # Guilherme Silva...

# sep: define o separador ENTRE os argumentos (padrão é espaço)
print(nome, sobrenome, sep="#")     # Guilherme#Silva