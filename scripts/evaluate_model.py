import pandas as pd
import joblib
import os
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Define a raiz do projeto como a pasta AED_netflix_IMDB
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Caminho dos conjuntos de teste
X_test_path = os.path.join(BASE_DIR, 'data/modeling/X_test.csv')
y_test_path = os.path.join(BASE_DIR, 'data/modeling/y_test.csv')

# Caminho do modelo treinado
model_path = os.path.join(BASE_DIR, 'models/random_forest_imdb.pkl')

# Carregar os conjuntos de teste
X_test = pd.read_csv(X_test_path)
y_test = pd.read_csv(y_test_path)

# Carregar o modelo treinado
model = joblib.load(model_path)

# Fazer previsões
y_pred = model.predict(X_test)

# Calcular métricas de avaliação
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Exibir os resultados
print(f"📊 Avaliação do Modelo:")
print(f"MAE (Erro Absoluto Médio): {mae:.4f}")
print(f"MSE (Erro Quadrático Médio): {mse:.4f}")
print(f"R² Score: {r2:.4f}")

# Criar diretório models se não existir
model_dir = os.path.join(BASE_DIR, 'models')
os.makedirs(model_dir, exist_ok=True)

# Caminho para salvar os resultados
results_path = os.path.join(model_dir, 'evaluation_metrics.csv')

# Salvar resultados em um arquivo
results = pd.DataFrame({'MAE': [mae], 'MSE': [mse], 'R2': [r2]})
results.to_csv(results_path, index=False)

print(f"Métricas de avaliação salvas em '{results_path}'.")
