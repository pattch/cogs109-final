import numpy as np
from load_sms import load_bag_of_words as load
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier as RFC
import config

x_,y_,words = load(config.sms_file)
x,xt,y,yt = train_test_split(x_,y_,test_size=0.5,random_state=0)

for i in range(1,101):
    clf = RFC(n_estimators=256,max_depth=i,random_state=0)
    clf.fit(x,y)
    print('%d\t%.3f\t%.3f' % (100,clf.score(x,y),clf.score(xt,yt)))
