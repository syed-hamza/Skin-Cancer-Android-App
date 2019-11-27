## Steps in creating the final Android App

### Setup th android app
1) Download the app from https://github.com/tensorflow/examples
2) Download android if you havent yet at https://developer.android.com/studio/index.html
3) Open AndroidStudio. After it loads select " Open an existing Android Studio project" 
4) In the file selector, choose examples/lite/examples/image_classification/android from your working directory.
5) You will get a "Gradle Sync" popup, the first time you open the project, asking about using gradle wrapper. Click "OK".
6) Test run the app.

### converting the app to run your model:
1) The project is configured to search for a model.tflite, and a labels.txt files in the 

   lite/examples/image_classification/android/app/src/main/assets 

   directory. Replace the existing labels with the labels above and the model with the inception_v3 model you trained.

![model.tflite   labels.txt](https://codelabs.developers.google.com/codelabs/recognize-flowers-with-tensorflow-on-android/img/1c8cdc983073d67b.png)
