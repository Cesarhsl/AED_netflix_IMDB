import pandas as pd
import numpy as np
import os

def load_data(filepath):
    """Carrega um arquivo CSV como um DataFrame do Pandas."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")
    return pd.read_csv(filepath)

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
    filepath = 'data/raw/NetflixTVShowsandMovies.csv'

    # Carregar os dados
    df = load_data(filepath)
    print("Dados carregados com sucesso!")

    # Preencher valores ausentes
    df = fill_missing_values(df, strategy='mean')
    print("Valores ausentes preenchidos!")

    # Remover duplicatas (corrigido)
    df = remove_duplicates(df)
    print("Duplicatas removidas!")

    # Normalizar uma coluna (exemplo)
    if 'imdb_score' in df.columns:
        df = normalize_column(df, 'imdb_score')
        print("Coluna imdb_score normalizada!")

    # Criar diretório de saída se não existir
    output_dir = 'data/processed'
    os.makedirs(output_dir, exist_ok=True)

    # Salvar o DataFrame limpo
    output_path = os.path.join(output_dir, 'ProcessedNetflixTVShowsandMovies.csv')
    df.to_csv(output_path, index=False)
    print(f"Arquivo processado salvo em {output_path}")
