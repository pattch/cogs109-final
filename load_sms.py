import numpy as np
from scipy import sparse

def load(fname):
    words = set()
    dat = []
    with open(fname) as f:
        for l in f:
            spam,sms = l.split(':',1)
            dat.append([sms,spam])
            for word in sms.split():
                words.add(word)

    dat = np.array(dat)
    words = list(words)

    return (dat[:,0],dat[:,1],words)

def load_bag_of_words(fname):
    x,y,words = load(fname)

    # Build dict from word -> index
    wd = {}
    num_words = len(words)
    for i in range(num_words):
        word = words[i]
        wd[word] = i

    x_ = sparse.lil_matrix((x.shape[0],num_words),dtype=np.int8)
    print(x.shape,y.shape,x_.shape,num_words)
    for i in range(x.shape[0]):
        sms = x[i]
        row_counts = {}
        for word in sms.split():
            idx = wd[word]
            x_[i,idx] += 1
    # x_ = sparse.csr_matrix(np.array(x_))

    return (x_,y,words)