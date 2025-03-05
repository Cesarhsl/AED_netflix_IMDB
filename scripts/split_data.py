import pandas as pd
from sklearn.model_selection import train_test_split
import os

# Carregar os dados processados
data = pd.read_csv('data/processed/ProcessedNetflixTVShowsandMovies.csv')

# Selecionar as colunas relevantes
features = ['release_year', 'runtime', 'seasons', 'imdb_votes', 'age_certification', 'genres', 'production_countries']
target = 'imdb_score'

# Filtrar apenas colunas que existem no dataset
features = [col for col in features if col in data.columns]

# Separar features e target
X = data[features]
y = data[target]

# Converter variáveis categóricas para números (One-Hot Encoding)
X = pd.get_dummies(X, columns=['age_certification', 'genres', 'production_countries'], drop_first=True)

# Dividir os dados em treino (80%) e teste (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar diretório de saída se não existir
output_dir = 'data/modeling'
os.makedirs(output_dir, exist_ok=True)

# Salvar os conjuntos de treino e teste
X_train.to_csv(os.path.join(output_dir, 'X_train.csv'), index=False)
X_test.to_csv(os.path.join(output_dir, 'X_test.csv'), index=False)
y_train.to_csv(os.path.join(output_dir, 'y_train.csv'), index=False)
y_test.to_csv(os.path.join(output_dir, 'y_test.csv'), index=False)

print("Divisão dos dados concluída e arquivos salvos em 'data/modeling'.")
