# **Análise de Dados de Séries e Filmes da Netflix 📊**

## **📌 Descrição**
Este projeto realiza uma **análise exploratória detalhada** do conjunto de dados **"Netflix TV Shows and Movies"**, com o objetivo de identificar **padrões, tendências ao longo do tempo e insights sobre classificações de conteúdo e preferências do público**.

Além disso, o projeto inclui um **modelo preditivo** para estimar a **pontuação IMDB** com base em características dos filmes e séries.

---

## **📂 Estrutura do Projeto**
O projeto está organizado da seguinte forma:

- **`data/`** → Contém os datasets utilizados no projeto:
  - **`raw/`** → Dados brutos extraídos do Kaggle.
  - **`processed/`** → Dados limpos e processados prontos para análise.
- **`scripts/`** → Scripts para limpeza, preparação e análise dos dados:
  - `data_preparation.py` → Script para tratamento e preparação dos dados.
  - `utilities.py` → Funções auxiliares para análise e visualização.
  - `split_data.py` → Divide os dados em treino e teste para Machine Learning.
  - `train_model.py` → Treina o modelo preditivo de pontuação IMDB.
  - `evaluate_model.py` → Avalia o desempenho do modelo preditivo.
- **`figures/`** → Gráficos e figuras gerados durante a análise.
- **`models/`** → Modelos treinados e arquivos de avaliação.
- **`README.md`** → Arquivo de documentação do projeto.

---

## **⚙️ Configuração do Ambiente**
Siga os passos abaixo para configurar o ambiente necessário e executar os scripts do projeto.

### **1️⃣ Instalação dos Requisitos**
Certifique-se de ter o **Python 3.8 ou superior** instalado. Depois, clone o repositório e instale as dependências:

```bash
git clone https://github.com/yourusername/AED_netflix_IMDB.git
cd AED_netflix_IMDB
pip install -r requirements.txt

## Contributing
Contributions to improve the project are welcome. Feel free to fork the repository and submit your suggestions through pull requests.

## License
ISC License

Copyright (c) 2024 César Henrique Sousa Lima

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
