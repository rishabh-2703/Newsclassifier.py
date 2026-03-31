# 🧠 News Category Classifier (GUI-Based)

This project is a simple yet practical Machine Learning application that classifies news headlines into different categories such as Politics, Sports, Technology, Business, and more.

It combines Natural Language Processing (NLP) with a user-friendly desktop interface built using Tkinter.

---

## 🚀 Features

- Classify a single news headline instantly
- Upload a CSV dataset (100+ headlines) for bulk prediction
- Automatically generates an output file with predicted categories
- Clean and modern dark-themed GUI
- Uses real-world dataset for training

---

## 🛠️ Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- NLTK  
- Tkinter (for GUI)

---

## 📂 Project Structure
- │── news_classifier_gui.py
- │── News_Category_Dataset_v3.json
- │── test_news.csv
- │── output_predictions.csv (generated after running)


---

## ⚙️ How It Works

1. The dataset is preprocessed (cleaning, removing stopwords)
2. Text is converted into numerical form using TF-IDF
3. A Logistic Regression model is trained
4. User can:
   - Enter a headline manually  
   - OR upload a CSV file  
5. The model predicts the category and displays/saves results

---

## ▶️ How to Run

1. Install required libraries:

pip install pandas numpy scikit-learn nltk

2. Download the dataset from Kaggle:
- News Category Dataset
- Place the dataset file in the same folder as the code
- Run the program:

python news_classifier_gui.py

## 📊 Input Format (CSV)

Make sure your CSV file contains a column named:

headline

Example:

- headline
- Stock market crashes today
- India wins cricket match
- New AI tool launched

## 📈 Output

After uploading a dataset, a file named:

output_predictions.csv

will be generated with predicted categories.

## 🎯 Objective

The goal of this project is to demonstrate how machine learning can be applied to real-world text classification problems and to provide an interactive interface for users.

## 🚀 Future Improvements
- Add accuracy display in GUI
- Show results in table format
- Add confidence score (%)
- Convert into web app (Streamlit)
- Improve UI with advanced design

## 👨‍💻 Author

Rishabh Rai
B.Tech CSE (AI/ML) – 1st Year

## ⭐ If you like this project, feel free to star it!
