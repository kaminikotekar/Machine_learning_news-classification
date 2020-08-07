import pickle
import re
from nltk.corpus import stopwords
from News_classification_model import predict, create_test_field
from nltk.stem import WordNetLemmatizer

stop_words=set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    filtered=re.sub('[^a-zA-Z]'," ",text)
    filtered= filtered.lower()
    filtered= filtered.split()
    new_filter=[]
    for word in filtered:
        if word not in stop_words:
            new_filter.append(lemmatizer.lemmatize(word))
    filtered=" ".join(new_filter)
    print(filtered)
    return filtered


def predict_result(text):
    try:
        filtered = clean_text(text)
        with open('data/model_data.pkl', 'rb') as f:
            classifier = pickle.load(f)
        with open('data/cv_data.pkl', 'rb') as f:
            cv = pickle.load(f)
        
        to_predict = []
        to_predict.append(filtered)
        X_data = create_test_field(to_predict, cv)
        y_result = predict(X_data, classifier)
        return y_result[0]
    except Exception as e:
        print(e)
        return 'Something went wrong'