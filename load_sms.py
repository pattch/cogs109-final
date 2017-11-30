import numpy as np

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

    x_ = []
    for i in range(len(x)):
        sms = x[i]
        l = [0] * len(words)
        for word in sms.split():
            l[wd[word]] += 1
        x_.append(l)

    x_ = np.array(x_)
    return (x_,y,words)