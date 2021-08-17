import pandas as pd 

# Lê o forms de perfil do estudante 
caminho_arqs = './dados/'
nome_arq = caminho_arqs +"'"+ 'Compreensão do Perfil da Turma'+"'.csv"
try:
    print(nome_arq)
    df_perfil  = pd.read_csv(nome_arq)
except:
    # tenta ler o próximo arquivo
    print("Falha ao ler arquivo!") 



## Renomear colunas 
df_perfil = df_perfil.rename(columns={'Qual o seu conhecimento nos tópicos abaixo:  [Operadores aritméticos]':'op_aritmetico','Qual o seu conhecimento nos tópicos abaixo:  [Estruturas condicionais (if, else, etc.) ]':'if', 'Qual o seu conhecimento nos tópicos abaixo:  [Operadores lógicos]': 'op_logico', 'Qual o seu conhecimento nos tópicos abaixo:  [Estruturas de repetição (while, for )]':'while', 'Qual o seu conhecimento nos tópicos abaixo:  [Vetores (Arrays) ]': 'vetor' })
   
## Dados sobre o Conhecimento Básico de Programação 
# Dados sobre o conhecimento prévio do aluno em relação ao conteúdo de lógica de programação
print("\nSelecionado os campos sobre conhecimento prévio:")
dados_conhecimento_previo =  df_perfil.iloc[:,[1,8,9,10,11,12]]
print( dados_conhecimento_previo.columns.values )


print("\nConhecimento prévio antes de tranformar os dados: ")
print(dados_conhecimento_previo.iloc[0:5, : ])

dados_conhecimento_previo = dados_conhecimento_previo.replace(['Muito'],5)
dados_conhecimento_previo = dados_conhecimento_previo.replace(['Nenhum'],0)
dados_conhecimento_previo = dados_conhecimento_previo.replace(['Pouco'],1)
dados_conhecimento_previo = dados_conhecimento_previo.replace(['Razoavel'],3)


print("\nConhecimento prévio depois de tranformar os dados: ")
print(dados_conhecimento_previo.iloc[0:5, : ])


dados_conhecimento_previo.to_csv('./saida/dados_conhecimento_previo.csv', index=False)  




