# Skin Cancer Detection Android App(Image Processing)
Here are the Codes, Datasets and the Android App required to create the Skin Cancer Detection App.

## Process
The dataset is orignally available at https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T .
The given code uses inception_v3 at https://keras.io/applications/#inceptionv3.Inception model gave me a slightly better result than nasnetmobile and training the model was comparitively quick.

### Inception(Validation_Accuracy):
![inception](images/inceptionModelAcc.png)

**validation accuracy:85.76%**

### NasNetMobile(Validation_Accuracy):
![nasnet](images/nasnetModelAcc.png)

**validation accuracy:84.72%**

From this we can conclude that eventhough nasnet fluctuates less than inception inception provides a better accuracy,hence is better suited for the app.

## Regards
I am a student in highschool and this is my first project using Deep Learning.
The following project took me several weekends along 2 months. I hope it is helpful to everyone reading this.
All suggetions are welcome.
