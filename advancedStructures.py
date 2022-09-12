# Conseguem juntar variáveis de tipos diferentes
# Analogia com vagão

# Lista
nomes_paises = ['Brasil', 'Argentina', 'China', 'Japão']

# Indices negativos retornam na lista na direção reversa à usual

print(nomes_paises[-1]
      
# Slicing, acessar múltiplos elementos 
      
print(nomes_paises[1:3]) # segundo e terceiro elementos, o elemento no índice 3 não é acessado
      
print(nomes_paises[1:]) # do segundo elemento até o final

print(nomes_paises[:3]) # do primeiro elemento até o anterior ao índice 3
      
print(nomes_paises[::2] # acessa os elementos e salta 2 índices
      
print(nomes_paises[::-1] # inverte a lista
      
print("Brasil" in nomes_paises) # checar se algum elemento está na lista
      
# Outra lista
      
lista_capitais = []

lista_capitais.append("Fortaleza") # Adicionar elemento ao final da lista

lista_capitais.insert(indice, "elemento") # Insere elemento em determinada posição na lista
      
lista_capitais.remove("Fortaleza") # remove o elemento do parâmetro
      
lista_capitais.pop(indice) # remove o elemento na posição indice e retorna esse elemento

# Tupla não pode ser alterada após definida
# É menor em relação ao armazenamento

nomes_paises = ("Brazil", "Argentina", "Itália", "Canadá") # ou nomes_paises = "Brazil", "Argentina", "Itália", "Canadá"

a, b, c, d = nomes_paises # unpacking
      
print(*nomes_paises) # printar de forma separada
      
      
# Strings
      
frase = "O professor disse: \"Hoje vai ter pizza.\"" # \ cancela o delimitador " " e outros
      
# Slicing também funciona para strings
      
# Métodos retornam os valores do que foi alterado
      
nomes_cidades = "São Paulo, Belo Horizonte, Rio de Janeiro, Brasília"

nomes_cidades.split(", ") # separar as substrings de acordo com o delimitador ", "
      
frase2 = "        Menu Principal         "
print(cabecalho.strip()) # Retorna "Menu Principal"

print(nomes_cidades.title()) # primeiras letras de cada palavra em maiúsculo
print(nomes_cidades.capitalize()) # primeira letra da string em maiúsculo


# Operador in
      
mensagem = 'Você viu o que o Pietro disse na sala de aula ontem?'
fui_citado = 'Pietro' in mensagem

      
# Strings II

cumprimento = 'Olá, '
nome = 'Felipe'
print(cumprimento+nome) # Concatenação

print(nome*5) # Replicação

# Format String
print('{} tem {} anos e {} filhos'.format(nome, idade, n_filhos))

preco_gasolina = 3.456
print('O preço da gasolina hoje está em {:.2f}'.format(preco_gasolina)) # Arredondando e acertando as casas decimais

# Atalho para o format, f antes das aspas

print(f'...')

# Dicionário

dados_cidade = {
  'nome': 'São Paulo',
  'população': 1521,
}

# Método copy

dados_cidade2 = dados_cidade # dessa forma, o que eu faço em uma variável ocorre na outra

dados_cidade2 = dados_cidade.copy() # variáveis independentes

dados_cidade.get('Prefeito') # procura os valores da chave  Prefeito no dicionário
      
dados_cidade.keys() # retorna uma lista de chaves de um dicionário

dados_cidade.values() # retorna uma lista de valores do dicionário

dados_cidade.items() # retorna uma lista de tuplas (chave, valor) de um dicionário
      

# FOR-Loop, iterar um certo número de vezes

for nome in nomes_cidades:
  print(nomes)

# for in dicionario
      
cidade = {
  'nome': 'São Paulo',
  'populacao': 14512,
}

for chave in cidades:
   print(f'{chave}: {cidades[chave]})
   
# Funções
         
print("Olá", end=' ') # não vai pular linha de um print pro outro, vai dar apenas espaço ao fnal

# args

def calcula_media(*args):
    print(args) # args são mapeados por uma tupla
    soma = sum(args)
    media = soma/len(args)
    return media

# keywords args, kwargs

def print_info(**kwargs):
    print(kwargs) # mapeado para um dicionário, mais usado em ciência de dados

print_info(Nome='Pietro', Sobrenome='Rabelo')


