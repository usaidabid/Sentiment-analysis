# Sentiment-analysis
 The Approach Used :

 
For sentiment analysis, we followed a structured approach. First, we preprocessed the dataset by converting text to lowercase, tokenizing words, and removing stopwords. Then, we used TF-IDF vectorization to transform the text into numerical features. Next, we split the dataset into training and testing sets and trained a Logistic Regression model. Finally, we evaluated the model’s performance using accuracy, precision, recall, and F1-score to ensure it could correctly classify sentiments as positive or negative.

Challenges Faced:


One major challenge  was selecting the right number of features for TF-IDF vectorization, as too many or too few words affected performance. Additionally deployment using Streamlit and Hugging Face Spaces also posed challenges, especially in managing dependencies and model file compatibility.

Model Performance & Improvements:


The model achieved around 90% accuracy, indicating strong performance in classifying sentiments. The F1-score and precision-recall values also showed a well-balanced value. Future improvements could involve using pre-trained embeddings such as Word2Vec or BERT to enhance contextual understanding and boost accuracy.
