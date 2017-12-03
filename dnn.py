from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
from load_sms import load_bag_of_words as load
from sklearn.model_selection import train_test_split
import config

x_,y_,words = load(config.sms_file)
x,xt,y,yt = train_test_split(x_.toarray(),y_,test_size=0.8,random_state=0)
num_words = len(words)

print(x.shape,y.shape,num_words)

epochs = 10
batch_size = 1

model = Sequential()
model.add(Dense(32,input_shape=(num_words,),kernel_initializer='he_uniform',activation='tanh'))
model.add(Dense(16))
model.add(Dropout(0.3))
model.add(Dense(1,activation='sigmoid'))

opt = SGD(lr=0.1)
model.compile(loss='binary_crossentropy',
                optimizer=opt,
                metrics=['accuracy'])

model.fit(x,y,
    batch_size=batch_size,
    epochs=epochs,
    verbose=1)

score,scoret = model.evaluate(x,y,batch_size=batch_size),model.evaluate(xt,yt,batch_size=batch_size)
print('Train Score',score[0],'Train Accuracy',score[1],'Test Score',score[1],'Test Accuracy',score[1])