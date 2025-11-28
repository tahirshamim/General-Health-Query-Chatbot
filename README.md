
# **Medical Assistant Chatbot (Safe Mode)**

This project is a safety-focused medical assistant chatbot built with **Streamlit** and **Google Gemini API**.
The bot provides **general health information only** and includes strict safety filters to prevent harmful medical advice.

---

## **Features**

* Uses **Gemini 2.5 Flash** via Google’s Generative AI API.
* Built-in **safety rules** preventing:

  * Diagnoses
  * Medication or dosage advice
  * Treatment recommendations
  * Emergency instructions
  * Advice for children, infants, or pregnant women
* Detects unsafe user queries using keyword filtering.
* Clean chat interface with Streamlit.
* Stores and displays chat history.

---

## **How It Works**

1. User submits a question.
2. The app checks for unsafe keywords.
3. If unsafe → returns a safety message.
4. If safe → sends the question to the Gemini model with a strict system prompt.
5. Displays bot response and chat history.

---

## **Tech Used**

* Python
* Streamlit
* Google Generative AI (`google.genai`)
* Safety filtering logic

---

## **Run the App**

```bash
pip install streamlit google-generativeai
streamlit run app.py
```

---

## **Note**

This bot **cannot** provide medical advice.
Always consult a licensed healthcare professional for personal medical concerns.

---

