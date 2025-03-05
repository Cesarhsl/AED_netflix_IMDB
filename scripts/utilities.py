import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from wordcloud import WordCloud

sns.set(style="whitegrid")

def load_data(filepath):
    """Carrega dados de um arquivo CSV."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")
    return pd.read_csv(filepath)

def ensure_dir(directory):
    """Assegura que o diretório exista. Se não existir, cria o diretório."""
    os.makedirs(directory, exist_ok=True)

def plot_histogram(data, column, bins=30, title=None, xlabel=None, ylabel='Frequência', save_path=None):
    """Gera um histograma para uma coluna específica de um DataFrame e salva a figura."""
    if column not in data.columns:
        print(f"Aviso: Coluna {column} não encontrada!")
        return
    
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], bins=bins, kde=True)
    plt.title(title or f'Histograma de {column}')
    plt.xlabel(xlabel or column)
    plt.ylabel(ylabel)
    
    if save_path:
        ensure_dir(os.path.dirname(save_path))
        plt.savefig(save_path)
    
    plt.show()

def plot_top_imdb_titles(data, save_path=None, top_n=50):
    """Gera um gráfico com os Top N títulos mais bem avaliados no IMDB."""
    if 'title' not in data.columns or 'imdb_score' not in data.columns:
        print("Erro: Colunas necessárias ('title', 'imdb_score') não encontradas.")
        return

    top_movies = data[['title', 'imdb_score']].dropna().sort_values(by='imdb_score', ascending=False).head(top_n)

    plt.figure(figsize=(12, 8))
    sns.barplot(x=top_movies['imdb_score'], y=top_movies['title'], palette="viridis")
    plt.xlabel("IMDB Score")
    plt.ylabel("Título")
    plt.title(f"Top {top_n} Títulos com Maiores Notas no IMDB")
    plt.gca().invert_yaxis()

    if save_path:
        ensure_dir(os.path.dirname(save_path))
        plt.savefig(save_path)
    
    plt.show()

def plot_worst_imdb_titles(data, save_path=None, bottom_n=50):
    """Gera um gráfico com os Bottom N títulos com as menores notas no IMDB."""
    if 'title' not in data.columns or 'imdb_score' not in data.columns:
        print("Erro: Colunas necessárias ('title', 'imdb_score') não encontradas.")
        return

    worst_movies = data[['title', 'imdb_score']].dropna().sort_values(by='imdb_score', ascending=True).head(bottom_n)

    plt.figure(figsize=(12, 8))
    sns.barplot(x=worst_movies['imdb_score'], y=worst_movies['title'], palette="Reds_r")
    plt.xlabel("IMDB Score")
    plt.ylabel("Título")
    plt.title(f"Top {bottom_n} Títulos com Menores Notas no IMDB")
    plt.gca().invert_yaxis()

    if save_path:
        ensure_dir(os.path.dirname(save_path))
        plt.savefig(save_path)
    
    plt.show()

def plot_most_voted_movies(data, save_path=None, top_n=50):
    """Gera um gráfico dos filmes/séries mais votados no IMDB."""
    if 'title' not in data.columns or 'imdb_votes' not in data.columns:
        print("Erro: Colunas necessárias ('title', 'imdb_votes') não encontradas.")
        return

    most_voted = data[['title', 'imdb_votes']].dropna().sort_values(by='imdb_votes', ascending=False).head(top_n)

    plt.figure(figsize=(12, 8))
    sns.barplot(x=most_voted['imdb_votes'], y=most_voted['title'], palette="Blues_d")
    plt.xlabel("Quantidade de Votos no IMDB")
    plt.ylabel("Título")
    plt.title(f"Top {top_n} Filmes/Séries com Maior Quantidade de Votos no IMDB")
    plt.gca().invert_yaxis()

    if save_path:
        ensure_dir(os.path.dirname(save_path))
        plt.savefig(save_path)
    
    plt.show()

def plot_description_wordcloud(data, save_path=None):
    """Gera uma nuvem de palavras a partir das descrições dos filmes e séries."""
    if 'description' not in data.columns:
        print("Aviso: Coluna 'description' não encontrada.")
        return

    descriptions = data['description'].dropna()
    if descriptions.empty:
        print("Aviso: Nenhuma descrição disponível para a nuvem de palavras.")
        return

    all_descriptions = ' '.join(descriptions.values)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_descriptions)

    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Nuvem de Palavras das Descrições')

    if save_path:
        ensure_dir(os.path.dirname(save_path))
        plt.savefig(save_path)
    
    plt.show()

# Caminho base para salvar as figuras
figures_path = 'figures/'

# Carregando o DataFrame
try:
    data = load_data('data/processed/ProcessedNetflixTVShowsandMovies.csv')

    # Gerar apenas os gráficos relevantes
    plot_histogram(data, 'imdb_score', bins=20, title='Distribuição de Pontuações IMDB', save_path=figures_path + 'imdb_score_histogram.png')
    plot_top_imdb_titles(data, save_path=figures_path + 'top_50_imdb_titles.png', top_n=50)
    plot_worst_imdb_titles(data, save_path=figures_path + 'worst_50_imdb_titles.png', bottom_n=50)
    plot_most_voted_movies(data, save_path=figures_path + 'most_voted_movies.png', top_n=50)
    plot_description_wordcloud(data, save_path=figures_path + 'description_wordcloud.png')

except FileNotFoundError as e:
    print(f"Erro ao carregar os dados: {e}")
