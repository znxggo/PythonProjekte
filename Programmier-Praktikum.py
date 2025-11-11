import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Liste erstellen mit 10 Gliedern von 0 bis 10
#x= np.array([0,1,2,3,4,5,6,7,8,9])
#print(x)

#Zweite, schneller Methode, um die gleiche Liste zu erstellen
x = np.arange(10)
print(x)

#Reshape
X = x.reshape(2,5)
print(X)
print(X.shape)

#Aufgabe 3
data = {
    'name': ['Julian','Lukas','Constantin','Johannes','Anna'],
    'alter': [42, 12, 33, 88, 20],
    'note': [1.7, 2.3, 3.1, 2.6, 1.0]
}
df = pd.DataFrame(data)
print(df)

df_note_besser_als_2 = df[df['note'] < 2.0]
print(df_note_besser_als_2)