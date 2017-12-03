import numpy as np
from load_sms import load_bag_of_words as load
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as KNN
from math import log
import config

x_,y_,words = load(config.sms_file)
x,xt,y,yt = train_test_split(x_.toarray(),y_,test_size=0.5,random_state=0)

for i in range(0,int(log(x.shape[0],2))):
    n = 2**i
    clf = KNN(n_neighbors=n)
    clf.fit(x,y)
    print('%d\t%.3f\t%.3f' % (n,clf.score(x,y),clf.score(xt,yt)))
