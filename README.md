<h1>Industry Classification</h1>

### Dataset Used
The Dataset that has two variables (Job title & Industry) in a csv format of more than 8,500 samples.
The dataset is imbalanced (Imbalance means that the number of data points available for different classes is different).
Dataset link: https://drive.google.com/file/d/1W_MO19MlDDUn0qCfxEaVxGKKlKHsFFly/view

### Which techniques did I use while cleaning the data:
- Removed the duplicates in the data.(prevents false accuracy and overfitting).
- Removed unwanted stop words like(the,a,an,..) **but keeping the important ones like (it, computer)**.
- Removed numbers. 
- Used lower case for all the text.

### How did I deal with (Imbalance learning):
- Droping duplicated reduced the imbalance of the data (as a lot of dublicates belongs to the 'IT' class).
- I have used 'SMOTE' -an oversampling method- with SGDClassifier and MultinomialNB.
- I have used add sample weights with LogisticRegression.
- I have made stratify splliting by the target to keep the distripution of the data the same.

### How can you extend the model to have better performance?
- the model can be further improved if it has more data specially for the "Accountancy" class it well not only will handle the imbalance of the data but the 'MLPClassifier' will perform much better if there was more data. 

### How did you evaluate the models?
**classification_report and LearningCurve:** This classification model suffers from shortage of the data and unbalnced data, so i take f1 score as main evaluation metric and multible evaluatiion approaches as  satisfying metrics:

### What are the limitations of your methodology or Where does your approach fail?
- I have tried to avoid the limitation of each algorthm by using the 'VotingClassifier' but the shortage and unbalnce of the data still has effect specially over the **precision of the 'IT' Class**.
