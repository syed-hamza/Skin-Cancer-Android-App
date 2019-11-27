# Skin Cancer Detection Android App(Image Processing)
Here are the Codes, Datasets and the Android App required to create the Skin Cancer Detection App.

## Process
The dataset is orignally availible at https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T .
The given code uses inception_v3 at https://keras.io/applications/#inceptionv3.Inception model gave me a way better result compared to nasnetmobile and training the model was comparitively quick.

### Inception(Validation_Accuracy):
![inception](images/inceptionModelAcc.png)

**validation accuracy:85.76%**

### NasNetMobile(Validation_Accuracy):
![nasnet](images/nasnetModelAcc.png)

**validation accuracy:84.72%**

From this we can conclude that eventhough nasnet fluctuates less than inception inception provides a better accuracy,hance can be used in the app.

## Regards
The following project took me more than a month to make. I hope it is helpful to everyone reading this:).
Suggetions are welcome.
