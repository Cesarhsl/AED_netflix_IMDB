import pandas as pd
from sklearn.model_selection import train_test_split
import os

# Define a raiz do projeto como a pasta AED_netflix_IMDB
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Caminho do arquivo processado
processed_filepath = os.path.join(BASE_DIR, 'data/processed/ProcessedNetflixTVShowsandMovies.csv')

# Carregar os dados processados
data = pd.read_csv(processed_filepath)

# Selecionar as colunas relevantes
features = ['release_year', 'runtime', 'seasons', 'imdb_votes', 'age_certification', 'genres', 'production_countries']
target = 'imdb_score'

# Filtrar apenas colunas que existem no dataset
features = [col for col in features if col in data.columns]

# Separar features e target
X = data[features]
y = data[target]

# Filtrar apenas as colunas categóricas que existem no DataFrame
categorical_cols = ['age_certification', 'genres', 'production_countries']
existing_categorical_cols = [col for col in categorical_cols if col in X.columns]

# Aplicar One-Hot Encoding apenas nas colunas que existem
if existing_categorical_cols:
    X = pd.get_dummies(X, columns=existing_categorical_cols, drop_first=True)

# Dividir os dados em treino (80%) e teste (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar diretório de saída se não existir
modeling_dir = os.path.join(BASE_DIR, 'data/modeling')
os.makedirs(modeling_dir, exist_ok=True)

# Salvar os conjuntos de treino e teste
X_train.to_csv(os.path.join(modeling_dir, 'X_train.csv'), index=False)
X_test.to_csv(os.path.join(modeling_dir, 'X_test.csv'), index=False)
y_train.to_csv(os.path.join(modeling_dir, 'y_train.csv'), index=False)
y_test.to_csv(os.path.join(modeling_dir, 'y_test.csv'), index=False)

print(f"Divisão dos dados concluída e arquivos salvos em {modeling_dir}.")
