import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def load_and_preprocess(csv_path, text_column):
    df = pd.read_csv(csv_path)
    df[text_column] = df[text_column].astype(str).apply(clean_text)
    return df

if __name__ == "__main__":
    # Example usage
    df = load_and_preprocess("sample_reviews.csv", "review")
    print(df.head())
