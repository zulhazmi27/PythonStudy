import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB #import Naive Baiyes Classifier

class IntentClassifier:
    
    def __init__(self):
        self.data = pd.read_csv("intent_classification/data.csv") #read data from csv file
        self.train() #train the model whenever an instance is made
        
    def train(self):
        X_train, y_train = self.data["text"], self.data["intent"] #assign text and intent to X_train and y_train respectively
        self.count_vect = CountVectorizer() #create an instance of CountVectorizer class
        X_train_counts = self.count_vect.fit_transform(X_train) #count the number of words in each text and transform it to a vector of token counts
        tfidf_transformer = TfidfTransformer() #create an instance of TfidfTransformer class
        X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts) #transform the count to tfidf
        self.clf = MultinomialNB().fit(X_train_tfidf, y_train) #create an instance of MultinomialNB class and train the model with the tfidf and intent as the target variable (y_train) and the text as the feature (X_train_tfidf)
        
    def predict(self, text):
        return self.clf.predict(self.count_vect.transform([text]))[0] #predict the intent of the text and return the intent
    
intent_classifier = IntentClassifier() #create an instance of IntentClassifier class