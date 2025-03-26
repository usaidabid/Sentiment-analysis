import streamlit as st
import joblib
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
st.title("Sentiment Analysis App 😊😠")
user_input = st.text_area("Enter your text:")
if st.button("Analyze Sentiment"):
    if user_input:
        transformed_text = vectorizer.transform([user_input])
        prediction = model.predict(transformed_text)
        sentiment = "Positive 😃" if prediction[0] == "positive" else "Negative 😠"
        st.write("Sentiment:", sentiment)
    else:
        st.warning("⚠️ Please enter some text!")
