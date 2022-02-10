#### Lucas Bergonsi
# Mestrando em Física-Universidade Federal de Pelotas

import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

df = pd.read_csv('TiO2.csv') #Lê o arquivo CSV, df=DataFrame
print("Descrição do arquivo:")
print(df)
################## Plotando o gráfico ############################
plt.figure(figsize=(15, 10))  # dimensiona a figura
plt.text(50, 1000, 'TiO2', fontsize='xx-large') # Dimensiona em espaço e tamanho o texto
plt.xlim(10, 90) #limites do eixo x
plt.ylabel('Intensidade(u.a.)') #Nomeia eixo y
plt.xlabel(r"2$\dot{\Theta}$[Graus]")  #Nomeia eixo x
# plt.annotate(u'máximo local', xy=(25, 100), xytext=(3, 1.5), arrowprops=dict(facecolor='black',shrink=0.05)) #faz uma anotação local no grafico
plt.plot(df['twotheta'], df[' yobs'], color='red', label='Yobs')
plt.plot(df['twotheta'], df[' bkg'], color='black', label='bkg')
# plt.plot(df['#twotheta'], df['diff'],color = 'green',label='diff')
plt.plot(df['twotheta'], df[' ycal'], color='blue', label='Ycal')

############################################################################
# print("Descrição dos dados:")
# print(df.describe())
print("O maior para a intensidade é:")
print(df.nlargest(1, columns=df.columns[1])) # Procura o maior valor para o coluna'yobs',bats trocar a coluna para saber outros
angulo= df.nlargest(1, columns=df.columns[1]) #Transforma em uma nova variável
print("No ângulo correspondente a:")
Imax=angulo.twotheta # Use essa variável caso queira colocar isso no gráfico
print(angulo.twotheta) # Mostra o Angula de maior intensidade
plt.legend(framealpha=1, frameon=True) ## Necessário para a legenda relativa aos dados(nomes da colunas)
############################################################################
############# Encontrar os máximos relativos aos angulos #################
df2=pd.read_csv("TiO2.csv",header=0,delimiter=',')
df3=df2.columns[1] # Anexa a coluna em uma variável
x=df2.columns[0] # Define a colunas de angulo como sendo eixo X, relacionando oa máximos
y=df[df3] # Define a coluna de interesse como sendo a variável que procura os máximos
x1=df[x]
peaks,_= find_peaks(y, height=0,prominence=110,distance=10) #Calcula o máximos
plt.plot(x1[peaks], y[peaks], "x",label='Peaks') # Plota os máximos em conformidade com a colunas relacionada
plt.legend(framealpha=1, frameon=True)
for a,b in zip(x1[peaks], y[peaks]): #plota os valores obtidos direto no gráfico
    plt.text(a, b, str(a)+'°')
plt.yticks([]) #omite os valores do eixo y
plt.show()
##############################################################################
############################################################################

