import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from wordcloud import WordCloud

# Configurações de estilo do Seaborn para gráficos mais claros
sns.set(style="whitegrid")

def load_data(filepath):
    """Carrega dados de um arquivo CSV."""
    return pd.read_csv(filepath)

def ensure_dir(directory):
    """Assegura que o diretório exista. Se não existir, cria o diretório."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def plot_histogram(data, column, bins=30, title=None, xlabel=None, ylabel='Frequência', save_path=None):
    """Gera um histograma para uma coluna específica de um DataFrame e salva a figura."""
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], bins=bins, kde=True)
    plt.title(title or f'Histograma de {column}')
    plt.xlabel(xlabel or column)
    plt.ylabel(ylabel)
    
    if save_path:
        ensure_dir(os.path.dirname(save_path))
        plt.savefig(save_path)
    plt.close()

def plot_correlation_matrix(data, title='Matriz de Correlação', save_path=None):
    """Gera a matriz de correlação para um DataFrame e salva a figura."""
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, fmt='.2f', cmap='coolwarm')
    plt.title(title)
    
    if save_path:
        ensure_dir(os.path.dirname(save_path))
        plt.savefig(save_path)
    plt.close()

def calculate_missing_values(data):
    """Calcula a porcentagem de valores ausentes para cada coluna em um DataFrame."""
    missing_values = data.isnull().sum()
    missing_percentage = (missing_values / len(data)) * 100
    return pd.DataFrame({'Número de Valores Ausentes': missing_values, 'Porcentagem': missing_percentage})

def downsample_dataframe(data, n_samples):
    """Reduz o tamanho de um DataFrame para um número especificado de amostras."""
    if len(data) > n_samples:
        return data.sample(n=n_samples)
    return data

def analyze_content_type(data, save_path=None):
    """Analisa o número e a distribuição de tipos de conteúdo (MOVIE/SHOW) e salva a figura."""
    content_counts = data['type'].value_counts()
    print(content_counts)
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='type', y='imdb_score', data=data)
    plt.title('Distribuição de IMDB Score por Tipo de Conteúdo')
    
    if save_path:
        ensure_dir(os.path.dirname(save_path))
        plt.savefig(save_path)
    plt.close()

def trend_analysis_by_year(data, save_path=None):
    """Analisa tendências ao longo do tempo, como quantidade de conteúdo e pontuação média do IMDB por ano, e salva a figura."""
    yearly_content = data.groupby('release_year').size()
    yearly_imdb_score = data.groupby('release_year')['imdb_score'].mean()
    
    fig, ax1 = plt.subplots(figsize=(14, 8))

    color = 'tab:blue'
    ax1.set_xlabel('Ano de Lançamento')
    ax1.set_ylabel('Quantidade de Conteúdo', color=color)
    ax1.plot(yearly_content.index, yearly_content, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('Pontuação Média do IMDB', color=color)
    ax2.plot(yearly_imdb_score.index, yearly_imdb_score, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title('Tendências de Conteúdo e Pontuação do IMDB por Ano')
    
    if save_path:
        ensure_dir(os.path.dirname(save_path))
        plt.savefig(save_path)
    plt.close()

def plot_description_wordcloud(data, save_path=None):
    """Gera uma nuvem de palavras a partir das descrições dos filmes e séries."""
    all_descriptions = ' '.join(data['description'].dropna().values)
    wordcloud = WordCloud(width=800, height=400, background_color ='white').generate(all_descriptions)
    
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Nuvem de Palavras das Descrições')
    
    if save_path:
        ensure_dir(os.path.dirname(save_path))
        plt.savefig(save_path)
    plt.close()

# Caminho base para salvar as figuras
figures_path = 'C:\\Users\\Cesar\\OneDrive\\Área de Trabalho\\CODE\\AED_netflix_IMDB\\figures\\'

# Carregando o DataFrame
data = load_data('c:\\Users\\Cesar\\OneDrive\\Área de Trabalho\\CODE\\AED_netflix_IMDB\\data\\processed\\ProcessedNetflixTVShowsandMovies.csv')

# Exemplo de chamada de função com caminho completo para salvar as figuras
plot_histogram(data, 'imdb_score', bins=20, title='Distribuição de Pontuações IMDB', save_path=figures_path + 'imdb_score_histogram.png')
analyze_content_type(data, save_path=figures_path + 'content_type_distribution.png')
trend_analysis_by_year(data, save_path=figures_path + 'imdb_score_trend_by_year.png')
plot_description_wordcloud(data, save_path=figures_path + 'description_wordcloud.png')
