import pandas as pd

df7 = pd.read_csv('https://dadosabertos.camara.leg.br/arquivos/proposicoesAutores/csv/proposicoesAutores-2017.csv', sep=';', index_col='idProposicao')
df6 = pd.read_csv('https://dadosabertos.camara.leg.br/arquivos/proposicoesAutores/csv/proposicoesAutores-2016.csv', sep=';', index_col='idProposicao')
df5 = pd.read_csv('https://dadosabertos.camara.leg.br/arquivos/proposicoesAutores/csv/proposicoesAutores-2015.csv', sep=';', index_col='idProposicao')
dfg11 = df5.append(df6).append(df7)
dfg12 = df5.append(df7).append(df6)
dfg21 = df7.append(df6).append(df5)
dfg22 = df7.append(df5).append(df6)
dfg31 = df6.append(df5).append(df7)
dfg32 = df6.append(df7).append(df5)

class questao1:
  def solution():
    print("Ótimo, pode passar para a próxima questão!")
  def hint():
    print("Muito bem, agora teste o método solution()")
  def check():
    print("Nada a checkar!")
    
q1 = questao1

class questao2:
  def solution():
    print("""Solução:
# Importando os módulos
import pandas as pd

# Leia os databases por ano
df_2017 = pd.read_csv('https://dadosabertos.camara.leg.br/arquivos/proposicoesAutores/csv/proposicoesAutores-2017.csv', sep=';', index_col='idProposicao')
df_2016 = pd.read_csv('https://dadosabertos.camara.leg.br/arquivos/proposicoesAutores/csv/proposicoesAutores-2016.csv', sep=';', index_col='idProposicao')
df_2015 = pd.read_csv('https://dadosabertos.camara.leg.br/arquivos/proposicoesAutores/csv/proposicoesAutores-2015.csv', sep=';', index_col='idProposicao')

# Imprima as 4 primeiras linhas de cada tabela
print(df_2017.head(4))
print(df_2016.head(4))
df_2015.head(4)""")
  def hint():
    print("Importe o pandas como pd, depois utilize os métodos \033[1mpandas.read_cs()\033[0m e \033[1mdataFrame.head()\033[0m")
  def check():
    if (str(df_2017) != str(df7)):
      print("\033[91mErrado\033[0m: a variável df_2017 não foi criada corretamente, certifique-se de utilizar o separado ';' e o index a coluna 'idProposicao'")
      return None
    if (str(df_2016) != str(df6)):
      print("\033[91mErrado\033[0m: a variável df_2016 não foi criada corretamente, certifique-se de utilizar o separado ';' e o index a coluna 'idProposicao'")
      return None
    if (str(df_2015) != str(df5)):
      print("\033[91mErrado\033[0m: a variável df_2015 não foi criada corretamente, certifique-se de utilizar o separado ';' e o index a coluna 'idProposicao'")
      return None
    print("\033[92mCorreto\033[0m: DataFrames criados corretamente")
    
q2 = questao2

class questao3:
  def solution():
    print(""" Solução:
# Imprima a quantidade de linhas e colunas de cada dataset do dataset df_2016
df_2016.shape
# Imprima como está organizado os tipos das colunas do dataset df_2016
df_2016.info()""")
  def hint():
    print("\033[1mdataFame.shape \033[0me \033[1mdataFrame.info()\033[0m podem ser úteis")
  def check():
    print("Nada a checkar!")
    
q3 = questao3
class questao4:
  def solution():
    print("Solução:\nFaça com que todas as tabelas sejam parte apenas da tabela df\ndf = df_2015.append(df_2016).append(df_2017)")
  def hint():
    print("Utilize o método \033[1mdataFrame.append(dataFrame)\033[0m")
  def check():
    if( str(df) == str(dfg11) or str(df) == str(dfg12) or str(df) == str(dfg21) or str(df) == str(dfg22) or str(df) == str(dfg31) or str(df) == str(dfg32) ):
      print("\033[92mCorreto\033[0m: DataFrames  df criado corretamente")
    else:
      print("\033[91mErrado\033[0m: a variável df não foi criada corretamente, certifique-se de juntar todos os 3 dataFrames")
    
q4 = questao4

print("\033[1mNotebook pronto para uso\033[0m")
