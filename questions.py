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

df_2016 = pd.read_csv('https://dadosabertos.camara.leg.br/arquivos/proposicoesAutores/csv/proposicoesAutores-2016.csv', sep=';', index_col='idProposicao')
df_2015 = pd.read_csv('https://dadosabertos.camara.leg.br/arquivos/proposicoesAutores/csv/proposicoesAutores-2015.csv', sep=';', index_col='idProposicao')

# Imprima as 4 primeiras linhas de cada tabela

print(df_2016.head(4))
df_2015.head(4)""")
  def hint():
    print("Importe o pandas como pd, depois utilize os métodos \033[1mpandas.read_cs()\033[0m e \033[1mdataFrame.head()\033[0m")
  def check():
    try:
      df7 = pd.read_csv('https://dadosabertos.camara.leg.br/arquivos/proposicoesAutores/csv/proposicoesAutores-2017.csv', sep=';', index_col='idProposicao')
      df6 = pd.read_csv('https://dadosabertos.camara.leg.br/arquivos/proposicoesAutores/csv/proposicoesAutores-2016.csv', sep=';', index_col='idProposicao')
      df5 = pd.read_csv('https://dadosabertos.camara.leg.br/arquivos/proposicoesAutores/csv/proposicoesAutores-2015.csv', sep=';', index_col='idProposicao')
      if (str(df_2017) != str(df7)):
        print("\033[91mErrado\033[0m: a variável df_2017 não foi criada corretamente, certifique-se de utilizar o separador ';' e o index a coluna 'idProposicao'")
        return None
      if (str(df_2016) != str(df6)):
        print("\033[91mErrado\033[0m: a variável df_2016 não foi criada corretamente, certifique-se de utilizar o separador ';' e o index a coluna 'idProposicao'")
        return None
      if (str(df_2015) != str(df5)):
        print("\033[91mErrado\033[0m: a variável df_2015 não foi criada corretamente, certifique-se de utilizar o separador ';' e o index a coluna 'idProposicao'")
        return None
      print("\033[92mCorreto\033[0m: DataFrames criados corretamente")
    except:
      print("\033[91mErrado\033[0m: as variável não foram criadas corretamente, certifique-se de utilizar o separador ';' e o index a coluna 'idProposicao'")

    
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
    try:
      if( str(df) == str(dfg11) or str(df) == str(dfg12) or str(df) == str(dfg21) or str(df) == str(dfg22) or str(df) == str(dfg31) or str(df) == str(dfg32) ):
        print("\033[92mCorreto\033[0m: DataFrame df criado corretamente")
      else:
        print("\033[91mErrado\033[0m: a variável df não foi criada corretamente, certifique-se de juntar todos os 3 dataFrames (lembre-se de seguir a ordem 2015, 2016, 2017) )!")
    except:
      print("\033[91mErrado\033[0m: a variável df não foi criada corretamente, certifique-se de juntar todos os 3 dataFrames (lembre-se de seguir a ordem 2015, 2016, 2017) )!")

    
q4 = questao4

df_rn_teste = dfg11[dfg11['siglaUFAutor'] == 'RN']
class questao5:
  def solution():
    print("df_rn = df[df['siglaUFAutor'] == 'RN']\ndf_rn.head(3)")
  def hint():
    print("Você pode tentar utilizar a seguinte sintaxe: novo_df = nome_df[nome_df['coluna'] == 'opção']")
  def check():
    try:
      if (str(df_rn_teste) == str(df_rn)):
        print("\033[92mCorreto\033[0m: DataFrame df_rn criado corretamente")
      else:
        print("\033[91mErrado\033[0m: a variável df_rn não foi criada corretamente (verifique os nomes das colunas para identificar a correta e selecionar 'RN').")
    except:
      print("\033[91mErrado\033[0m: a variável df_rn não foi criada corretamente (verifique os nomes das colunas para identificar a correta e selecionar 'RN').")


q5 = questao5

prop_number_teste = df_rn_teste['nomeAutor'].value_counts()
class questao6:
  def solution():
    print("prop_number = df_rn['nomeAutor'].value_counts()\nprint(prop_number)")
  def hint():
    print("O método df.value_counts pode ser útil!")
  def check():
    try:
      if (str(prop_number_teste) == str(prop_number)):
        print("\033[92mCorreto\033[0m: DataFrame df_rn criado corretamente!")
      else:
        print("\033[91mErrado\033[0m: df_rn não foi criado corretamente!")
    except:
      print("\033[91mErrado\033[0m: df_rn não foi criado corretamente!")


q6 = questao6

df_brasil_teste = dfg11.count()
porcen_rn_teste = (prop_number_teste[0] / df_brasil_teste['uriProposicao'])*100

prop_number_brasil_teste = dfg11['nomeAutor'].value_counts()
porcen_br_teste = (prop_number_brasil_teste[0] / df_brasil_teste['uriProposicao'])*100

class questao7:
  def solution():
    print("""df_brasil = df.count()
qnt = (prop_number[0] / df_brasil['uriProposicao'])*100
print(qnt)

prop_number_brasil = df['nomeAutor'].value_counts()
qnt_brasil = (prop_number_brasil[0] / df_brasil['uriProposicao'])*100
print(qnt_brasil)""")
  def hint():
    print("O método dataFame.count() mostra quantos elementos possui em uma determinada coluna, com isso, basta dividir\no primeiro elemento de series.value_counts() pela quantidade de elementros na coluna 'uriProposicao'")
  def check():
    try:
      if (porcen_rn_teste != porcen_rn):
        print("\033[91mErrado\033[0m: porcen_rn não foi criado corretamente!")
      elif (porcen_br_teste != porcen_br):
        print("\033[91mErrado\033[0m: porcen_br não foi criado corretamente!")
      else:
        print("\033[92mCorreto\033[0m: Valores calculados de forma correta!")
    except:
      print("\033[91mErrado\033[0m: As variáveis não foram criadas corretamente!")

q7 = questao7

media_prop_teste = dfg11['nomeAutor'].value_counts().mean()

class questao8:
  def solution():
    print("""media_prop = df['nomeAutor'].value_counts().mean()
print(media_prop)
print(prop_number[ prop_number > media_prop ] )""")
  def hint():
    print("Utilize o método mean() em dataFrame.value_counts()")
  def check():
    try:
      if(media_prop_teste == media_prop):
        print("\033[92mCorreto\033[0m: Valor calculado de forma correta!")
      else:
        print("\033[91mErrado\033[0m: media_prop não foi criado corretamente!")
    except:
      print("\033[91mErrado\033[0m: media_prop não foi criado corretamente!")


q8 = questao8

class questao9:
  def solution():
    print("""print(df['tipoAutor'].value_counts()[:4])""")
  def hint():
    print("Utilize o método series.value_count() em 'tipoAutor'.")
  def check():
    print("Nada à checkar!")
    
q9 = questao9

max_partidos_teste = dfg11['siglaPartidoAutor'].value_counts()[:10]

class questao10:
  def solution():
    print("""max_partido = df['siglaPartidoAutor'].value_counts()[:10]
print(max_partido)""")
  def hint():
    print("Selecione os 10 primeiros itens do método series.value_count() da coluna 'siglaPartidoAutor'.")
  def check():
    try:
      if(str(max_partidos_teste) == str(max_partidos)):
        print("\033[92mCorreto\033[0m: Parabéns, você finalizou o notebook!")
      else:
        print("\033[91mErrado\033[0m: max_partidos não foi criado corretamente!")
    except:
      print("\033[91mErrado\033[0m: max_partidos não foi criado corretamente!")
      
q10 = questao10

print("\033[1mNotebook pronto para uso\033[0m")
