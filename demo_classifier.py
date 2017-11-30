from load_sms import load_bag_of_words
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.tree import DecisionTreeClassifier

sms_file = 'smsspamcollection/cleanedcollection'

def classify(fname):
    print('Loading',fname)
    x,y,words = load_bag_of_words(fname)

    print('X Shape:',x.shape,'Y Shape:',y.shape,'Word Count:',len(words))

    print('Fitting Classifier: Random Forest Classifier')
    clf = RFC(n_estimators=128,max_depth=50,random_state=0)
    clf.fit(x,y)
    print('Accuracy:',clf.score(x,y))

    print('Fitting Classifier: Decision Tree Classifier')
    clf = DecisionTreeClassifier(random_state=0)
    clf.fit(x,y)
    print('Accuracy:',clf.score(x,y))

print('Classifying using SMS Spam Collection File')
classify(sms_file)
