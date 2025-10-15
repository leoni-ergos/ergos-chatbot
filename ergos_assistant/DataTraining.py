import pickle
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

model = Pipeline([
    ('tfidf', TfidfVectorizer(analyzer='char', ngram_range=(2, 4))),
    ('clf', MultinomialNB())
])

texts = []
labels = []

excel_file = "train_data.xlsx"
all_sheets = pd.read_excel(excel_file, sheet_name=None, engine="openpyxl")

for sheet_name, sheet_data in all_sheets.items():
    for index, row in sheet_data.iterrows():
        for column_name, cell_value in row.items():
            if pd.notna(cell_value):
                texts.append(str(cell_value))
                labels.append(sheet_name)

model.fit(texts, labels)

with open('intent_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved successfully.")
