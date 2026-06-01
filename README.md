# 🧠 Project Using OOPS — NLPy

A Python-based Natural Language Processing (NLP) application built using **Object-Oriented Programming (OOP)** concepts. This project demonstrates real-world usage of encapsulation, abstraction, and class design through an interactive terminal app.
## 🚀 Features

| Feature | Description | Status |
|---|---|---|
| 🔐 Register & Login | User authentication system with in-memory database | ✅ Working |
| 🏷️ NER | Named Entity Recognition — extract person, location, organization from text | ✅ Working |
| 🌍 Language Detection | Detect the language of any given text | ⏳ API Key needed |
| 😊 Sentiment Analysis | Detect emotion from text — joy, sadness, anger, fear, love, surprise | ✅ Working |

---
## 🛠️ Tech Stack
- **Language:** Python 3
- **API:** [NLPCloud](https://nlpcloud.com)
- **Models Used:**
  - `distilbert-base-uncased-emotion` — Sentiment Analysis
  - `finetuned-gpt-neox-20b` — Named Entity Recognition
  - `python-langdetect` — Language Detection
- **Concepts:** OOP (Encapsulation, Abstraction, Private Methods, Classes)

---

## 📦 Installation

**Step 1 — Clone the repo:**
```bash
git clone https://github.com/itsriteshx/Project-Using-OOPS-NLPy.git
cd Project-Using-OOPS-NLPy
```

**Step 2 — Install dependencies:**
```bash
pip install nlpcloud
```
**Step 3 — Run the app:**
```bash
python App.py
```
---
## 🎮 How to Use
### Step 1 — Register
```
Hi how would you like to proceed?
1. Not a member? Register      <-- type 1
2. Already a member? Login
3. Galti se aa gaye? Exit
```
Enter your **name, email and password** to create an account.

### Step 2 — Login
```
1. Not a member? Register
2. Already a member? Login     <-- type 2
3. Galti se aa gaye? Exit
```
Enter your **email and password** to login.

### Step 3 — Choose a Feature
```
Hi how would you like to proceed?
1. NER
2. Language Detection
3. Sentiment Analysis
4. Logout
```
---
## 💡 Feature Examples

### 🏷️ NER — Named Entity Recognition
```
Enter the paragraph:
John Doe started learning Javascript at 15. He is now a Go expert at Google in New York.

What would you like to search: location

--- NER Result ---
[location] -> New York
```

### 🌍 Language Detection
```
Enter the paragraph:
Bonjour, comment allez-vous?

--- Language Detection Result ---
Detected Language : FRENCH
Confidence        : 99.5%
```

### 😊 Sentiment Analysis
```
Enter the paragraph:
I just got promoted at work and I am so excited about my future!

--- Sentiment Result ---
Emotion     : JOY
Confidence  : 99.87%
```
---

## 🏗️ OOP Concepts Used

| Concept | Where Used |
|---|---|
| **Class** | `NLPApp` class |
| **Constructor** | `__init__` — database initialize karna |
| **Encapsulation** | Private attributes `__database`, `__SENTIMENT_KEY` etc. |
| **Abstraction** | Private methods `__ner()`, `__login()`, `__register()` etc. |
| **Data Hiding** | User data aur API keys private rakhe hain |

---

## 📁 Project Structure

```
Project-Using-OOPS-NLPy/
│
├── App.py        # Main application file
└── README.md     # Project documentation
```
---

## ⚠️ Note

- This app uses **NLPCloud Free Plan** — rate limits apply (limited requests per hour)
- For higher usage, upgrade to NLPCloud Pay-as-you-go plan
- Language Detection needs a separate API key from NLPCloud
---

## 👨‍💻 Author

**Ritesh Kumar**
- GitHub: [@itsriteshx](https://github.com/itsriteshx)

---

## ⭐ If you found this helpful, give it a star!
