# Leitura e organização de dados
with open("dataset\pib_municipio_2010_a_2018.txt", encoding='latin-1') as f:                         # abre arquivo
  colunas = f.readline().strip('\n').split(';')                      # lista nome das colunas
  dados = f.readlines()                                               # organiza dados em uma lista

# Conversão de String em lista
for linha in range(len(dados)):                                    # transforma cada linha dos dados em uma lista de elementos
  dados[linha] = dados[linha].strip('\n').split(';')

# Criando uma lista contendo todas as entradas referentes à cidade de Manaus
def dados_cidade_total(cidade):
  """
  Método utilizado para buscar todos os registros correspondentes à uma cidade passada como parâmetro

  Args:
    cidade(string): Nome da cidade a ser utilizada como filtro
  Retorno:
    dados_cidade(lista): Lista contendo todas as entradas referentes ao argumento de entrada
  """
  dados_cidade = []
  for linha in dados:
    if linha[3] == cidade:
      dados_cidade.append(linha)
  return dados_cidade

dados_manaus = dados_cidade_total("Manaus")

# Calculando o PIB médio para a cidade de Manaus com base na lista dados_manaus
def pib_medio_manaus():
  """
  Método utilizado para calcular o PIB médio da cidade de Manaus

  Retorno:
    pib_medio(float): Valor referente ao PIB médio da cidade de Manaus

  """
  pib_total = 0
  for linha in dados_manaus:
    pib_anual = int(linha[4]) + int(linha[5]) + int(linha[6]) + int(linha[7]) + int(linha[8])
    pib_total = pib_total + pib_anual
  pib_medio = pib_total/len(dados_manaus)
  return pib_medio

# Imprimindo os resultados no arquivo q2_saida.txt 
with open('questao_02\q2_saida.txt', mode="a") as f:
  print("PIB Médio de Manaus: R$ {0:.2f}".format(pib_medio_manaus()), file=f)