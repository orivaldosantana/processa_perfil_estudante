
import pandas as pd 

import pickle
# Carregando objetos 
rotulos = pickle.load(open("./treinamentos/rotulos.pickle", "rb"))

som = pickle.load(open("./treinamentos/som.pickle", "rb"))

MProbAp = pickle.load(open("./treinamentos/matrizProbAp.pickle", "rb"))
 


# Dados do sigaa
turma_sigaa = pd.read_csv("./dados/turma_02_2021_1.csv")

mats_sigaa = turma_sigaa.iloc[:,0].values

# cria o data frame de saída 
df = pd.DataFrame(columns=['nome', 'nivel','prob_sucesso'], index=mats_sigaa )
dados_perfil = df.fillna(0) 


# Lê os os dados do csv de conhecimento prévio 
import pandas as pd 
try:
    dados_conhecimento_previo =  pd.read_csv('./dados/dados_conhecimento_previo.csv') 
except:
    print("\nFalha ao ler arquivo(dados_conhecimento_previo.csv)!") 
# Torna campos vazios em 0
dados_conhecimento_previo.iloc[:,0] = dados_conhecimento_previo.iloc[:,0].fillna(0)
# Transforma o tipo do campo matricula em inteiro 
# Para ficar compativel com o uso de indeces mais a frente 
dados_conhecimento_previo = dados_conhecimento_previo.astype(int) 
# Vetor de matrículas 
mats_conhecimento_previo = dados_conhecimento_previo.iloc[:,0].values 

print(mats_conhecimento_previo[0:5])

## Dados sobre o Conhecimento Básico de Programação 
# Dados sobre o conhecimento prévio do aluno em relação ao conteúdo de lógica de programação
print("\nSelecionado os campos sobre conhecimento prévio:")
valores_conhecimento_previo = dados_conhecimento_previo.iloc[:,1:].values
print(valores_conhecimento_previo[0:5,:]) 


for i in range(mats_sigaa.size):
    for j in range(mats_conhecimento_previo.size):
        if  (mats_sigaa[i]==mats_conhecimento_previo[j]):
            x = valores_conhecimento_previo[j,:]
            print(x)
            pos = som.winner(x)
            dados_perfil['nivel'][mats_sigaa[i]] = rotulos[pos] 
            dados_perfil['prob_sucesso'][mats_sigaa[i]] = MProbAp[pos]*100 # valor inteiro 
            #print(". "+colunas_u_1[n])
print("Leitura realizada com sucesso!\n")

dados_perfil['nome'] = turma_sigaa.iloc[:,1].values

dados_perfil.to_csv("./saida/dados_perfil.csv")

