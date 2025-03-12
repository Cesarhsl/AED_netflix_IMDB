import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
import os

# Define a raiz do projeto como a pasta AED_netflix_IMDB
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Caminho dos conjuntos de treino
X_train_path = os.path.join(BASE_DIR, 'data/modeling/X_train.csv')
y_train_path = os.path.join(BASE_DIR, 'data/modeling/y_train.csv')

# Carregar os conjuntos de treino
X_train = pd.read_csv(X_train_path)
y_train = pd.read_csv(y_train_path)

# Inicializar o modelo Random Forest
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Treinar o modelo
print("Treinando o modelo...")
model.fit(X_train, y_train.values.ravel())  # y_train precisa estar em formato de array

# Criar diretório de saída se não existir
model_dir = os.path.join(BASE_DIR, 'models')
os.makedirs(model_dir, exist_ok=True)

# Caminho do modelo salvo
model_path = os.path.join(model_dir, 'random_forest_imdb.pkl')

# Salvar o modelo treinado
joblib.dump(model, model_path)

print(f"Modelo treinado e salvo em '{model_path}'.")
