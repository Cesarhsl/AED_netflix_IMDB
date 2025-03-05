import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Carregar os conjuntos de teste
X_test = pd.read_csv('data/modeling/X_test.csv')
y_test = pd.read_csv('data/modeling/y_test.csv')

# Carregar o modelo treinado
model = joblib.load('models/random_forest_imdb.pkl')

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

# Salvar resultados em um arquivo
results = pd.DataFrame({'MAE': [mae], 'MSE': [mse], 'R2': [r2]})
results.to_csv('models/evaluation_metrics.csv', index=False)

print("Métricas de avaliação salvas em 'models/evaluation_metrics.csv'.")
