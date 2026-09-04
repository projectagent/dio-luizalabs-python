# =====================================================================
# CONVERSÃO DE TIPOS (CASTING)
# =====================================================================

# ---------------------------------------------------------------------
# int -> float
# ---------------------------------------------------------------------
preco = 10 
print(preco)            # int
preco = float(preco)    # converte int para float
print(preco)            # 10.0

# Divisão sempre resulta em float
preco = 10/2
print(preco)            # 5.0

# ---------------------------------------------------------------------
# float -> int
# ---------------------------------------------------------------------
preco = 10.30
print(preco)            # float
preco = int(preco)      # converte float para int (trunca as casas decimais)
print(preco)            # 10

# ---------------------------------------------------------------------
# Divisão comum vs divisão inteira
# ---------------------------------------------------------------------
preco = 10
print(preco)            # int
print(preco / 2)        # 5.0 -> float (divisão comum)
print(preco // 2)       # 5   -> int (divisão inteira)

# ---------------------------------------------------------------------
# Números -> str
# ---------------------------------------------------------------------
preco = 10.50
idade = 28
print(str(preco))       # converte float para str
print(str(idade))       # converte int para str

# f-string: formata os valores como texto automaticamente
texto = f"idade: {idade} preço: {preco}"
print(texto)            # str

# ---------------------------------------------------------------------
# str -> int / float
# ---------------------------------------------------------------------
preco = "10.50"
idade = "28"
print(float(preco))     # converte str para float -> 10.5
print(int(idade))       # converte str para int -> 28

# Atenção: a conversão só funciona se o texto for numérico.
# Textos como "python" geram erro (ValueError).
preco = "python" 
print(float(preco))     # erro: não é possível converter str para float 