import numpy as np
tamanhoDaRede = 3
# matriz de zeros para contador de aprovados 
rotulos = np.zeros((tamanhoDaRede,tamanhoDaRede))

# 0 para iniciante 
# 5 para avançado 

rotulos[2][2] = 0
rotulos[2][1] = 1
rotulos[1][2] = 1
rotulos[2][0] = 2
rotulos[1][1] = 2
rotulos[1][0] = 3
rotulos[0][2] = 4
rotulos[0][1] = 5
rotulos[0][0] = 5

print(rotulos) 

import pickle

# Salvando a matriz de rótulos
pickle.dump(rotulos, open("./saida/rotulos.pickle", "wb"))


