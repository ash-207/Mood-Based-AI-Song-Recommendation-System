from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# Load model + tokenizer
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

# Example text input
text = "Only 2 rooms left! Hurry before it’s gone!"

# Run classification
result = classifier(text)

# Print result
print(result)
