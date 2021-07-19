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
- tqdm

# Content

## Notebooks

- `1.0-movielens-eda` explores the Movie Lens dataset
- `1.1-movielens-memory-based-recsys` demonstrates some examples of memory-based recommender systems using the Movie Lens dataset
- `1.2-movielens-model-based-recsys` shows two model-based recommender system approaches: Matrix Factorization and a back propagation approach
- `2.0-trivago-ranking-in-recsys` illustrates how to approach item ranking in recommender systems
- `2.1-pagerank-dampening` inspects the dampening effect of Google's PageRank algorithm
- `3.0-trivago-node2vec` explores graphs for recommender systems and introduction to node2vec
- `3.1-trivago-vae-for-cf` a PyTorch-adaptive implementation of the Variational Autoencoder for Collaborative Filtering using the Movie Lens dataset

## Data

The data folder stores the two datasets used in the notebooks: Movie Lens (ml-20m) and Trivago.

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
