from transformers import pipeline
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True,top_k=None)
text=input("How are you feeling today? \n")
results = emotion_classifier(text)
sorted_results = sorted(results[0], key=lambda x: x['score'], reverse=True)
top_emotion = sorted_results[0]
print(f"Detected emotion: {top_emotion['label']} with a score of {round(top_emotion['score']*100,2)}%")
# This code uses the Hugging Face Transformers library to classify emotions from text input.
