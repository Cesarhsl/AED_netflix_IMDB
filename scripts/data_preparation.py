import pandas as pd
import numpy as np

def load_data(filepath):
    """Carrega um arquivo CSV como um DataFrame do Pandas."""
    return pd.read_csv(filepath)

def fill_missing_values(df, strategy='mean'):
    """Preenche valores ausentes em colunas numéricas do DataFrame."""
    # Identifica colunas numéricas
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    # Aplica a estratégia de preenchimento apenas às colunas numéricas
    for col in numeric_cols:
        if strategy == 'mean':
            df[col] = df[col].fillna(df[col].mean())
        elif strategy == 'median':
            df[col].fillna(df[col].median(), inplace=True)
        elif strategy == 'mode':
            # Note que mode() retorna um DataFrame, então pegamos o valor no índice [0]
            df[col].fillna(df[col].mode()[0], inplace=True)
        else:
            df[col].fillna(0, inplace=True)
    return df


def remove_duplicates(df):
    """Remove linhas duplicadas do DataFrame."""
    return df.drop_duplicates()

def normalize_column(df, column_name):
    """Normaliza os dados de uma coluna usando Min-Max Scaling."""
    df[column_name] = (df[column_name] - df[column_name].min()) / (df[column_name].max() - df[column_name].min())
    return df

if __name__ == "__main__":
    # Caminho para o arquivo de dados
    filepath = 'c:\\Users\\Cesar\\OneDrive\\Área de Trabalho\\CODE\\AED_netflix_IMDB\\data\\raw\\NetflixTVShowsandMovies.csv'


    # Carregar os dados
    df = load_data(filepath)

    # Preencher valores ausentes
    df = fill_missing_values(df, strategy='mean')

    # Remover duplicatas
    df = remove_duplicates(df)

    # Normalizar uma coluna (opcional, dependendo da sua análise)
    # df = normalize_column(df, 'nome_da_coluna')

    # Salvar o DataFrame limpo
    df.to_csv('c:\\Users\\Cesar\\OneDrive\\Área de Trabalho\\CODE\\AED_netflix_IMDB\\data\\processed\\ProcessedNetflixTVShowsandMovies.csv', index=False)
