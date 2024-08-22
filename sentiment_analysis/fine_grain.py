import re
import pickle
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Load the saved model and vectorizer
with open('fine_grained_sentiment_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('tfidf_vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

def preprocess_text(text):
    """Process text for sentiment analysis."""
    # Convert text to lowercase
    text = text.lower()
    # Tokenize text
    tokens = word_tokenize(text)
    # Remove non-alphanumeric characters
    tokens = [re.sub(r'[^a-zA-Z0-9]', '', token) for token in tokens if token.isalnum()]
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    # Apply stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]
    # Join tokens back to string
    processed_text = ' '.join(tokens)
    return processed_text

def predict_fine_grained_sentiment(text):
    """Predict fine-grained sentiment from text using the loaded model and vectorizer."""
    # Preprocess the text
    processed_text = preprocess_text(text)
    # Transform the text to tf-idf vector
    text_tfidf = vectorizer.transform([processed_text])
    # Predict the sentiment using the trained model
    predicted_sentiment = model.predict(text_tfidf)
    return predicted_sentiment[0]

# Example usage
if __name__ == "__main__":
    input_text = input("Enter the text: ")
    predicted_sentiment = predict_fine_grained_sentiment(input_text)
    print("Predicted Fine-Grained Sentiment:", predicted_sentiment)
