class questao1:
  def solution():
    print("Ótimo, pode passar para a próxima questão!")
  def hint():
    print("Muito bem, agora teste o método solution()")
    
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
    
q3 = questao3

class questao4:
  def solution():
    print("Solução:\nFaça com que todas as tabelas sejam parte apenas da tabela df\ndf = df_2015.append(df_2016).append(df_2017)")
  def hint():
    print("Utilize o método \033[1mdataFrame.append(dataFrame)\033[0m")
    
q4 = questao4

print("Notebook pronto para uso")
