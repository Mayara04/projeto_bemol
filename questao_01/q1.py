# Leitura e organização de dados
with open("dataset\pib_municipio_2010_a_2018.txt", encoding='latin-1') as f:   
  colunas = f.readline().strip('\n').split(';')     
  dados = f.readlines()            

# Conversão de String em lista
for linha in range(len(dados)): 
  dados[linha] = dados[linha].strip('\n').split(';')

# Criando uma lista contendo somente os dados referentes ao ano de 2018
def dados_por_ano(ano):
  """
  Método utilizado para buscar os dados da base referentes à um ano passado como parametro 
  
  Args:
    ano(string): ano a ser buscado na base
  Retorno: 
    dados_ano(lista): lista contendo elementos da base de dados
  """
  dados_ano = []
  for linha in dados:
    if linha[0] == ano:
      dados_ano.append(linha)
  return dados_ano

dados_2018 = dados_por_ano('2018')

# Criando uma lista com os nomes dos estados presentes na base de dados
def nomes_estados():
  """
  Método utilizado para buscar a lista de estados presente na base de dados
  Retorno: 
    lista_estados(lista): lista contendo os nomes dos estados presente na base de dados
 
  """
  lista_estados = []
  
  for linha in dados:
    if linha[2] not in lista_estados:
      lista_estados.append(linha[2])

  return lista_estados

lista_estados = sorted(nomes_estados())

# Criando um dicionário com base na lista de estados gerada anteriormente
estados_dict = dict.fromkeys(lista_estados, '')

# Preenchendo o dicionário estados_dict com listas por estado, compostas por pares de cidade/PIB
def pib_cidades_por_estado():
  """
  Método utilizado para buscar o pib das cidades por estado
  """
  for estado in estados_dict.keys():
    cidades_estado = []
    for linha in dados_2018:
      if linha[2] == estado:
        cidades_estado.append([linha[3], float(linha[9])])
    estados_dict[estado] = cidades_estado                          

pib_cidades_por_estado()

# Com o uso do dicionário estados_dict, criando uma lista contendo as cidades com maior PIB per capita por estado
def maior_pib_por_cidade():
  """
  Método utilizado para buscar a cidade, por estado, que apresente o maior PIB per capita 
  
  Args:
  Retorno: 
    pib_cidade_estado(lista): lista contendo as cidades que apresentam o maior PIB por estado
  """
  pib_cidade_estado = []
  for estado in estados_dict.keys():
    maior_cidade_pib = sorted(estados_dict[estado], key=lambda x: x[1], reverse=True)[0]
    pib_cidade_estado.append([estado, maior_cidade_pib[0], maior_cidade_pib[1]])
  return pib_cidade_estado

pib_lista = maior_pib_por_cidade()

# Ordenando pib_lista, em ordem alfabética, com base no nome da cidade
pib_lista = sorted(pib_lista, key=lambda x: x[1])

# Imprimindo os resultados no arquivo q1_saida.txt
with open('questao_01\q1_saida.txt', mode="a") as f:
  print("Cidade | Estado | PIB", file=f)
  for linha in pib_lista:
    print(f'{linha[1]} | {linha[0]} | {linha[2]}', file=f)