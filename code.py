import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
netflix =pd.read_csv("ViewingActivity.csv")
netflix = netflix.drop(['Attributes','Supplemental Video Type','Bookmark','Latest Bookmark'], axis=1)

#Transformar o Start Time de string pra datetime
netflix['Start Time'] = pd.to_datetime(netflix['Start Time'],utc=True)

#Colocar a coluna Start Time como índice do data frame, para conseguir definir a tz
netflix = netflix.set_index('Start Time')

#Conversão para fuso horário do Brasil
netflix.index = netflix.index.tz_convert('America/Sao_Paulo')

#Tirar Start Time do índice
netflix = netflix.reset_index()

#Mudar duração para variação de tempo
netflix['Duration'] = pd.to_timedelta(netflix['Duration'])
soma = netflix['Duration'].sum()

netflix['Weekday'] = netflix['Start Time'].dt.weekday
netflix['Hour'] = netflix['Start Time'].dt.hour
#Por dia da semana
valores = [0,1,2,3,4,5,6]
netflix['Weekday'] = pd.Categorical(netflix['Weekday'], categories=valores,ordered=True)
net_por_dia = netflix['Weekday'].value_counts()
net_por_dia = net_por_dia.sort_index()
dias_da_semana = ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo']

matplotlib.RcParams.update({'font.size':30})
net_por_dia.plot(kind='bar',figsize=(20,10),title='Episódios por dias')
plt.xlabel('Dias da Semana')
plt.ylabel('Episódios')
plt.xticks(ticks=valores,labels=dias_da_semana,rotation=0)
plt.show()
plt.clf()
#Por hora do dia
netflix['Hour'] = pd.Categorical(netflix['Hour'],categories=range(0,24),ordered=True)
net_por_hora = netflix['Hour'].value_counts()
net_por_hora = net_por_hora.sort_index()


net_por_hora.plot(kind='bar',figsize=(20,10),title = 'Episódios por hora do dia')
plt.xlabel('Hora de início')
plt.ylabel('Episódios')
plt.xticks(rotation=0)
plt.show()
