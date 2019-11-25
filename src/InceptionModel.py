lr =0.0001
def create_inception_model2(n_classes=8,learning_rate=lr):
    raw_model = keras.applications.inception_v3.InceptionV3(include_top=False, weights='imagenet', input_shape=(224,224,3), classes=n_classes)
# first: train only the top layers (which were randomly initialized)
# i.e. freeze all convolutional InceptionV3 layers
    #for layer in raw_model.layers:
    #    layer.trainable = False
    full_model = Sequential()
    full_model.add(raw_model)
    full_model.add(GlobalAveragePooling2D())
    full_model.add(Dropout(0.2))
    full_model.add(Dense(512,activation='relu'))
    full_model.add(Dropout(0.1))
    full_model.add(Dense(8, activation = 'softmax'))
    full_model.compile(Adam(lr=learning_rate), loss = 'categorical_crossentropy', metrics = ['accuracy'])
    full_model.summary()
    return full_model
