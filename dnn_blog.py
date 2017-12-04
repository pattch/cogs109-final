from load_blog import load_matrix as load
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD,adam
from sklearn.model_selection import train_test_split

x_,y_ = load('microblogPCU/user_postcleaned')

print(x_.shape,y_.shape)

x,xt,y,yt = train_test_split(x_,y_,test_size=0.8,random_state=0)
num_words = x_.shape[1]

epochs = 20
batch_size = 16

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
print('Train Score',score[0],'Train Accuracy',score[1],'Test Score',scoret[0],'Test Accuracy',scoret[1])
