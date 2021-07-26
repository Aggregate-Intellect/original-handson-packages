# Introduction
This module contains notebooks and datasets for the popular **Recommenders - Reverse Engineering Users' Needs and Desires** course at [AISC](https://ai.science/). Original content is developed by these superstars:
- Felipe Perez, Sr. ML Research Scientist
- Ella Chen, Data Scientist
- Serena McDonnell, Sr. Data Scientist
- Werner Chao, Data Scientist

# Dependencies

To successfully run all the notebooks, you need to have the following packages installed:

- NumPy
- SciPy
- pandas
- Matplotlib
- PyTorch

# Content

## Data

Download the datasets used in these notebooks [here](https://drive.google.com/drive/folders/10OGTBbEVyX3YjFPX_kOjWF8FpwqvARr5?usp=sharing).

## Notebooks

- `1.0-movielens-eda` gives a quick introduction to recommender system and explores the Movie Lens dataset to prep for the rest of the notebooks
- `1.1-movielens-memory-based-recsys` demonstrates some examples of memory-based recommender systems using the Movie Lens dataset
- `1.2-movielens-model-based-recsys` shows two model-based recommender system approaches: Matrix Factorization and a back propagation approach
- `2.0-trivago-ranking-in-recsys` illustrates how to approach item ranking and evaluate results in recommender systems
- `2.1-pagerank-dampening` inspects the dampening effect of Google's PageRank algorithm
- `3.0-node2vec` explores graph representation for recommender systems by introducing node2vec
- `4.0-movielens-vae-for-cf` is a PyTorch-adaptive implementation of the Variational Autoencoder for Collaborative Filtering using the Movie Lens dataset

## Slides
These slides were produced as part of the original workshop. They provide additional context to the notebooks and contain more detailed explanations for certain concepts.

- `1-memory-based-vs-model-based-recsys` supports notebooks `1.0` to `1.2`
- `2-ranking-and-evaluation-in-recsys` supports notebooks `2.0` and `2.1`
- `3-graph-representation-for-recsys-node2vec` supports notebook `3.0`
- `4-variational-autoencoder-for-collaborative-filtering` supports notebook `4.0`

# Additional Reading Materials
- Weighted matrix factorization names  
    https://developers.google.com/machine-learning/recommendation/collaborative/matrix
- Large-scale Parallel Collaborative Filtering for the Netflix Prize  
    https://www.researchgate.net/publication/220788980_Large-Scale_Parallel_Collaborative_Filtering_for_the_Netflix_Prize
- PageRank, BPR, and rank metrics  
    https://www.link-assistant.com/news/google-page-rank-2019.html
- Auto-encoders and recommenders  
     https://medium.com/@connectwithghosh/recommender-system-on-the-movielens-using-an-autoencoder-using-tensorflow-in-python-f13d3e8d600d
- Variational Autoencoders for Collaborative Filtering  
    https://arxiv.org/pdf/1802.05814.pdf
- node2vec: Scalable Feature Learning for Networks  
    https://cs.stanford.edu/~jure/pubs/node2vec-kdd16.pdf
- PageRank beyond the web  
    https://arxiv.org/pdf/1407.5107.pdf
