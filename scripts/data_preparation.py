import pandas as pd
import numpy as np
import os

# Define a raiz do projeto como a pasta AED_netflix_IMDB
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_data(filepath):
    """Carrega um arquivo CSV como um DataFrame do Pandas."""
    full_path = os.path.join(BASE_DIR, filepath)
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {full_path}")
    return pd.read_csv(full_path)

def fill_missing_values(df, strategy='mean'):
    """Preenche valores ausentes em colunas numéricas do DataFrame."""
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    for col in numeric_cols:
        if df[col].isnull().sum() > 0:  # Apenas preenche se houver valores nulos
            if strategy == 'mean':
                df[col] = df[col].transform(lambda x: x.fillna(x.mean()))
            elif strategy == 'median':
                df[col] = df[col].transform(lambda x: x.fillna(x.median()))
            elif strategy == 'mode':
                df[col] = df[col].transform(lambda x: x.fillna(x.mode()[0]))
            else:
                df[col] = df[col].fillna(0)
    
    return df

def remove_duplicates(df):
    """Remove linhas duplicadas do DataFrame."""
    return df.drop_duplicates()

def normalize_column(df, column_name):
    """Normaliza os dados de uma coluna usando Min-Max Scaling."""
    if column_name in df.columns:
        min_val = df[column_name].min()
        max_val = df[column_name].max()
        if min_val != max_val:  # Evita divisão por zero
            df[column_name] = (df[column_name] - min_val) / (max_val - min_val)
    return df

if __name__ == "__main__":
    # Caminho do arquivo de entrada
    raw_filepath = 'data/raw/NetflixTVShowsandMovies.csv'

    # Carregar os dados
    df = load_data(raw_filepath)
    print("Dados carregados com sucesso!")

    # Preencher valores ausentes
    df = fill_missing_values(df, strategy='mean')
    print("Valores ausentes preenchidos!")

    # Remover duplicatas
    df = remove_duplicates(df)
    print("Duplicatas removidas!")

    # Normalizar uma coluna (exemplo)
    if 'imdb_score' in df.columns:
        df = normalize_column(df, 'imdb_score')
        print("Coluna imdb_score normalizada!")

    # Criar diretório de saída se não existir
    processed_dir = os.path.join(BASE_DIR, 'data/processed')
    os.makedirs(processed_dir, exist_ok=True)

    # Salvar o DataFrame limpo
    output_path = os.path.join(processed_dir, 'ProcessedNetflixTVShowsandMovies.csv')
    df.to_csv(output_path, index=False)
    print(f"Arquivo processado salvo em {output_path}")
