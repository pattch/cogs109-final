import numpy as np
import config
from keras.preprocessing.text import Tokenizer
from nltk.util import ngrams

def load(fname):
    words = set()
    dat = []
    with open(fname,'r',encoding='latin-1') as f:
        for l in f:
            spam,post = l.split(':',1)
            dat.append([post,spam])
            for c in post:
                words.add(c)

    dat = np.array(dat)
    words = list(words)

    return (dat[:,0],dat[:,1],words)

def word_grams(words, min=1, max=5):
    s = []
    for n in range(min, max):
        for ngram in ngrams(words, n):
            s.append(' '.join(str(i) for i in ngram))
    return s

def load_matrix(fname):
    x,y,words = load(fname)

    x_ = []
    for post in x:
        grams = ' '.join(word_grams(post,max=config.blog_grams))
        x_.append(grams)

    t = Tokenizer(lower=False)
    t.fit_on_texts(x_)
    x_ = t.texts_to_matrix(x_)

    return (x_,y)