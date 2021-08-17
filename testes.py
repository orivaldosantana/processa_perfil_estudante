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


mats_conhecimento_previo = dados_conhecimento_previo.iloc[:,0].values 

print(mats_conhecimento_previo[0:5])



# Dados do sigaa
turma_sigaa = pd.read_csv("./dados/turma_02_2021_1.csv")

print( turma_sigaa.iloc[0:5,1] )