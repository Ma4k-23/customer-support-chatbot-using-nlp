# 🧠 Customer Support Chatbot using NLP (Flask + ML)

This is a professional AI-powered **Customer Support Chatbot** built using rule-based **Natural Language Processing (NLP)** techniques. The bot is designed to handle frequently asked questions such as order status, refund requests, shipping policy, technical issues, and more.

> 📁 Internship Project for Snestron Internships – Task: *AI-Based Chatbot for Customer Support Using NLP*

---

## 🚀 Features

- ✅ Rule-based intent classification using `intents.json`
- 💬 Interactive chat UI built with **Flask + HTML/CSS**
- 🧠 Uses `scikit-learn` (Naive Bayes) for intent classification
- 📦 Handles queries like:
  - Refunds
  - Order tracking
  - Cancellations
  - Product info
  - Shipping policies
  - Feedback & more
- 🎯 Lightweight and easy to customize

---

## 🛠️ Tech Stack

| Technology       | Purpose                         |
|------------------|----------------------------------|
| Python           | Core programming language        |
| Flask            | Web framework                    |
| HTML + CSS       | Frontend UI                      |
| scikit-learn     | Intent classification            |
| CountVectorizer  | Text vectorization (Bag of Words)|
| JSON             | Intent storage and responses     |

---

## 🧠 NLP Approach

- Predefined intents stored in `intents.json`
- Bag-of-Words using `CountVectorizer`
- Multi-class classification using `Multinomial Naive Bayes`
- Static responses selected based on predicted intent

---

## 💻 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/Ma4k-23/customer-support-chatbot-using-nlp.git
cd customer-support-chatbot-using-nlp

# 2. (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python app.py

