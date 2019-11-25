train_datagen = ImageDataGenerator(rescale=1./255)

x_train = train_datagen.flow_from_directory(
    directory=r'../input/datatree/train/',
    batch_size=32,
    target_size=(224,224),
    class_mode="categorical",
    shuffle=True,
    seed=42
)
train_generator = x_train
class_weights = class_weight.compute_class_weight('balanced', np.unique(train_generator.classes), train_generator.classes)
class_weights = dict(enumerate(class_weights))
print("train_generator class_weights =",  class_weights)

validation_datagen = ImageDataGenerator(rescale=1./255)

x_validation = validation_datagen.flow_from_directory(
    directory=r'../input/datatree/validation/',
    batch_size=32,
    target_size=(224,224),
    class_mode="categorical",
    shuffle=True,
    seed=42
)
validation_generator = x_validation
class_weights_val = class_weight.compute_class_weight('balanced', np.unique(validation_generator.classes), validation_generator.classes)
class_weights_val = dict(enumerate(class_weights_val))
class_weights_val
print("val_generator class_weights =",  class_weights_val)

test_datagen = ImageDataGenerator(rescale=1./255)

x_test = test_datagen.flow_from_directory(
    directory=r'../input/datatree/test/',
    batch_size=32,
    target_size=(224,224),
    class_mode="categorical",
    shuffle=False,
    seed=42
)

test_generator = x_test

num_train_samples = train_generator.n
num_val_samples = validation_generator.n
train_batch_size = 256
val_batch_size = 256


train_steps = np.ceil(num_train_samples / train_batch_size)
val_steps = np.ceil(num_val_samples / val_batch_size)
print(train_steps)
print(val_steps)
