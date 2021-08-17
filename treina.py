import matplotlib.pyplot as plt
import numpy as np

import pandas as pd 

dados_perfis = pd.read_csv("https://raw.githubusercontent.com/ect-info/ml/master/dados/perfil_notas_sem_identificacao_col_resum.csv") 


print(dados_perfis.head())
print(dados_perfis.describe())

## Dados sobre o Conhecimento Básico de Programação 
# Dados sobre o conhecimento prévio do aluno em relação ao conteúdo de lógica de programação. Assuntos que serão vistos durante a disciplina 
print( dados_perfis.iloc[:,5:10].columns.values )
X_LoP = dados_perfis.iloc[:,5:10].values

print("\nDescrição dos dados: ")
print(dados_perfis.iloc[:,5:10].describe())

print("\nConteúdo de algumas amostras: ")
print(X_LoP[0:3, : ])


# obtem tamanho da base de dados de treinamento 
[row, col] = X_LoP.shape
print (row," ",col)

print(X_LoP[1,:])

# Training the SOM
tamanhoXdaRede = 3; 
tamanhoYdaRede = 3; 

quantidadeCaracteristicas = col
from minisom import MiniSom
som = MiniSom(x = tamanhoXdaRede, y = tamanhoYdaRede, input_len = quantidadeCaracteristicas, sigma = 1.0, learning_rate = 0.4)
som.pca_weights_init(X_LoP)

#som.train_random(data = X_LoP, num_iteration = 80000)

# Obtem o vetor de pesos da rede treinada 
pesos = som.get_weights()

# Mostra todos os pesos 
cont = 1
x = np.arange(quantidadeCaracteristicas)
for row in pesos:
  for elem in row:
    plt.subplot(tamanhoXdaRede,tamanhoYdaRede,cont)
    cont=cont+1
    plt.axis([-1, quantidadeCaracteristicas, 0, 5])
    plt.bar(x, elem)
    #plt.plot([-1,quantidadeCaracteristicas],[5,5],'r')
plt.savefig('./saida/rede_som.png')
# ['op_aritmetico' 'if' 'op_logico' 'while' 'vetor']


## Matriz de Total e Aprovados 
x = X_LoP[1,:]
pos = som.winner(x)


# matriz de zeros para contador de aprovados 
MContAp = np.zeros((tamanhoXdaRede,tamanhoYdaRede))
# matriz de zeros para o contador de reprovados 
MContT = np.zeros((tamanhoXdaRede,tamanhoYdaRede))
cont = 0; 
for x in X_LoP: 
  pos = som.winner(x)
  aprovado =  dados_perfis['Sit.'][cont] == 'APR'  or dados_perfis['Sit.'][cont] == 'APRN'
  if (aprovado): #Aprovado 
    MContAp[pos] += 1
  MContT[pos] += 1
  cont= cont+1


print("Total:")
print(MContT)


print("Aprovados")
print(MContAp)

# matriz de zeros para contador de aprovados 
MProbAp = np.zeros((tamanhoXdaRede,tamanhoYdaRede))
MDistProb = np.zeros((tamanhoXdaRede,tamanhoYdaRede)) 

for i in range(tamanhoXdaRede):
  for j in range(tamanhoXdaRede):
    MProbAp[i][j] = round( MContAp[i][j] /  MContT[i][j],2)
    MDistProb[i][j] = round( MContT[i][j] / 181, 2) 


print("Probabilidades de sucesso") 
print(MProbAp)

print("Distribuição de probabilidades")
print(MDistProb)


import pickle
# Salvando objeto com a rede som treinada 
pickle.dump(som, open("./saida/som.pickle", "wb"))

# Salvando a matriz de probabilidades de aprovação  
pickle.dump(MProbAp, open("./saida/matrizProbAp.pickle", "wb"))
