import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
import os

# Carregar os conjuntos de treino
X_train = pd.read_csv('data/modeling/X_train.csv')
y_train = pd.read_csv('data/modeling/y_train.csv')

# Inicializar o modelo Random Forest
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Treinar o modelo
print("Treinando o modelo...")
model.fit(X_train, y_train.values.ravel())  # y_train precisa estar em formato de array

# Criar diretório de saída se não existir
model_dir = 'models'
os.makedirs(model_dir, exist_ok=True)

# Salvar o modelo treinado
joblib.dump(model, os.path.join(model_dir, 'random_forest_imdb.pkl'))

print("Modelo treinado e salvo em 'models/random_forest_imdb.pkl'.")
