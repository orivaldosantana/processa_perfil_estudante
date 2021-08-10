
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
df = pd.DataFrame(columns=['Compreensão do Perfil da Turma','nivel'], index=mats_sigaa )
dados_perfil = df.fillna(0) 
# Lê todos os csvs dos forms de aula  

caminho_arqs = './dados/'
nome_arq = caminho_arqs +"'"+ 'Compreensão do Perfil da Turma'+"'.csv"
try:
    print(nome_arq)
    dados_temp  = pd.read_csv(nome_arq)
except:
    # tenta ler o próximo arquivo
    print("Falha ao ler arquivo!") 









# Torna campos vazios em 0
dados_temp.iloc[:,1] = dados_temp.iloc[:,1].fillna(0)
# Transforma o tipo do campo matricula em inteiro 
# Para ficar compativel com o uso de indeces mais a frente 
dados_temp.iloc[:,1] = dados_temp.iloc[:,1].astype(int) 

#mats_temp = dados_temp.iloc[:,1].values
mats_temp = dados_temp.iloc[:,1].values    


for i in range(mats_sigaa.size):
    for j in range(mats_temp.size):
        if  (mats_sigaa[i]==mats_temp[j]):
            dados_perfil['nivel' ][mats_sigaa[i]] = 1
            #print(". "+colunas_u_1[n])
print("Leitura realizada com sucesso!\n")

dados_perfil.to_csv("./saida/dados_perfil.csv", index=False)

