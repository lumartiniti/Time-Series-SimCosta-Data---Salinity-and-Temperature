# Mini curso - Análise de dados meteoceanográficos

arquivo = 'C:/Users/lmart/Downloads/SIMCOSTA_RS-4_OCEAN_2024-01-01_2024-12-31.csv'

import pandas as pd   # Trabalha com dataframe 
                      # Vamos chamar uma biblioteca que lida com o excel

abrir_arquivo = pd.read_csv(arquivo, header=33)   # Abrindo o arquivo .csv
print(abrir_arquivo)

print(abrir_arquivo.info())
print(abrir_arquivo.head())
print(abrir_arquivo.columns.tolist())


sal = abrir_arquivo['Avg_Sal']
temperatura = abrir_arquivo['Avg_W_Tmp1']
temperatura2 = abrir_arquivo['Avg_W_Tmp2']
print(temperatura2)

temperatura2 = temperatura-0.6

tempo = abrir_arquivo[['YEAR','MONTH','DAY','HOUR']]

abrir_arquivo['TEMPO'] = pd.to_datetime(tempo)    # Converte dados em formato de texto ou numero para formato de data e hora.
print(abrir_arquivo['TEMPO'])

tempo2 = abrir_arquivo['TEMPO']


### PLOTANDO

import matplotlib.pyplot as plt

#TABELA DE CORES: https://matplotlib.org/stable/gallery/color/named_colors.html

plt.figure(figsize=(10,4))   # Aqui faz a figura ficar em um tamanho específico
plt.plot(tempo2, sal,color='gold')

plt.title('SÉRIE TEMPORAL DE SALINIDADE, FONTE: SimCosta')
plt.xlabel('Tempo')
plt.ylabel('Salinidade (PSU)')
plt.grid() #plota uma grade na st

tempo2 = abrir_arquivo['TEMPO']


# O TEMPO ESTÁ EM FORMATO AMERICANO, VAMOS COLOCAR O BRASILZAOOO
import matplotlib.dates as mdates   #ELA FORMATA AS DATAS PRA GENTE, NO CASO
#TA NO FORMATO AMERICANO YYYY-MM-DD E QUEREMOS ENTÃO DD-MM-YYYY


#PLOTANDO A ST DE TEMPERATURA
plt.figure(figsize=(10,4)) #AQUI ELE FAZ A FIGURA FICAR EM UM TAMANHO ESPECÍFICO QUE QUEREMOS
plt.plot(tempo2, temperatura,color='red',label='Sensor 1')
plt.plot(tempo2,temperatura2,color='green',label='Sensor 2')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y'))
#plt.gca = ele mexe nos axis=eixo; xaxis.set_major...=Força o eixo x
#MEXENDO NOS EIXOS
plt.title('SÉRIE TEMPORAL DE TEMPERATURA, FONTE:SimCosta')
plt.xlabel('Tempo')
plt.ylabel('Temperatura (ªC)')
plt.grid() #plota uma grade na st
plt.legend()




