import pandas as pd
import re
import nltk
import tkinter as tk
from tkinter import filedialog

from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

nltk.download('stopwords')

# Load dataset
df = pd.read_json(r"/Users/rishabhrai/Downloads/News_Category_Dataset_v3.json", lines=True)
df = df[['headline', 'category']].sample(20000, random_state=42)

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    words = text.split()
    return " ".join(word for word in words if word not in stop_words)

df['headline'] = df['headline'].apply(clean_text)

# Train model
X = df['headline']
y = df['category']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
X_train_vec = vectorizer.fit_transform(X_train)

model = LogisticRegression(max_iter=200)
model.fit(X_train_vec, y_train)

# Predict single headline
def predict_single():
    text = entry.get().strip()

    if not text:
        result_label.config(text="Please enter a headline")
        return

    cleaned = clean_text(text)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]

    result_label.config(text=f"Category: {prediction}")

# Process CSV dataset
def load_dataset():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not file_path:
        return

    df_test = pd.read_csv(file_path)

    if 'headline' not in df_test.columns:
        result_label.config(text="CSV must contain 'headline' column")
        return

    predictions = []

    for text in df_test['headline']:
        cleaned = clean_text(str(text))
        vector = vectorizer.transform([cleaned])
        predictions.append(model.predict(vector)[0])

    df_test['Predicted_Category'] = predictions
    df_test.to_csv("output_predictions.csv", index=False)

    result_label.config(text="Predictions saved as output_predictions.csv")

# UI
root = tk.Tk()
root.title("News Category Classifier")
root.geometry("600x400")
root.configure(bg="#121212")

title = tk.Label(
    root,
    text="News Category Classifier",
    font=("Segoe UI", 18, "bold"),
    bg="#121212",
    fg="white"
)
title.pack(pady=15)

entry = tk.Entry(
    root,
    width=60,
    font=("Segoe UI", 11),
    bg="#1e1e1e",
    fg="white",
    insertbackground="white",
    relief="flat"
)
entry.pack(pady=10, ipady=6)

predict_btn = tk.Button(
    root,
    text="Predict",
    command=predict_single,
    bg="#00adb5",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    padx=10,
    pady=5
)
predict_btn.pack(pady=10)

upload_btn = tk.Button(
    root,
    text="Upload CSV",
    command=load_dataset,
    bg="#393e46",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    padx=10,
    pady=5
)
upload_btn.pack(pady=10)

result_label = tk.Label(
    root,
    text="Result will appear here",
    font=("Segoe UI", 13),
    bg="#121212",
    fg="#eeeeee"
)
result_label.pack(pady=20)

root.mainloop()
