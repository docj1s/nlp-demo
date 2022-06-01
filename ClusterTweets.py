from gensim.test.utils import datapath
from gensim.models.word2vec import Text8Corpus
from gensim.models.phrases import Phrases, Phraser
from gensim.models import Word2Vec
import multiprocessing
from sklearn.cluster import KMeans 

corpus = Text8Corpus(datapath('/home/rjones/twitter/tweets.txt'))

phrases = Phrases(corpus, min_count=30, progress_per=10000, threshold=1)
bigram = Phraser(phrases)

sentences = bigram[corpus]

cores = multiprocessing.cpu_count()

w2v_model = Word2Vec(min_count=20,
                        window=2,
                        sample=6e-5,
                        alpha=0.03,
                        min_alpha=0.0007,
                        negative=20,
                        workers=cores-1)

w2v_model.build_vocab(sentences, progress_per=10000)
w2v_model.train(sentences, total_examples=w2v_model.corpus_count, epochs=30)

word_vectors = w2v_model.wv

kmeans = KMeans(n_clusters=2, max_iter=1000, random_state=True, n_init=50).fit(X=word_vectors.vectors)
positive_cluster_center = kmeans.cluster_centers_[0]
negative_cluster_center = kmeans.cluster_centers_[1]

print(kmeans.cluster_centers_)
print(word_vectors.similar_by_vector(positive_cluster_center, topn=10, restrict_vocab=None))
print(word_vectors.similar_by_vector(negative_cluster_center, topn=10, restrict_vocab=None))
