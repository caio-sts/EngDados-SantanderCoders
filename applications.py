# Arquivos

arquivo = open(caminho_para_arquivo, uso da abertura) # ../../arquivo.txt # pasta/arquivo.txt # r para leitura ou w para escrita
linha = arquivo.readline()
print(linha, end=' ')
arquivo.close()

# with code

with open(caminho_arquivo, 'r') as arquivo:
  texto = arquivo.read()
  print(texto)
 
arquivo.read() # aqui dá erro pois arquivo já está fechado

# Write code
with open(caminho_arquivo, 'w') as arquivo:
  arquivo.write("Nova linha")
  
# Append code, escreve ao final
with open(caminho_arquivo, 'a') as arquivo:
  arquivo.write("Nova linha")

# manipular arquivos csv
import csv

# leitura csv
with open(arquivo.csv, 'r') as arquivocsv:
  leitor = csv.reader(arquivocsv)
  header = next(leitor)  # pular o header
  for linha in leitor:
      print(linha) # cada linha é representada como uma lista de elementos

# escrita csv
with open(arquivo.csv, 'w', newline='') as arquivocsv: # newline vazio implica n pular linha
  escritor = csv.writer(arquivocsv)
  header = next(leitor)  # pular o header
  for linha in leitor:
      print(linha) # cada linha é representada como uma lista de elementos

# APIs, basta uma requisição WEB
!pip install requests

import requests

url = 'https://tallink.com'

req = requests.get(url)
print(req.status_code)

dados = req.json()

print(dados)

