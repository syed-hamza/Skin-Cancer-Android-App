keras_model1 = "../outputN/SkinCancerI.pb"
keras.models.save_model(model,keras_model1)
keras.backend.clear_session()
converter = tf.lite.TFLiteConverter.from_saved_model(keras_model1)
tflite_model1 = converter.convert()
open("../outputN/model.tflite", "wb").write(tflite_model1)
