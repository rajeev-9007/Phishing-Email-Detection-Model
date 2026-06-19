import joblib

model = joblib.load("models/phishing_model.pkl")

email = input("Enter email text:\n")

prediction = model.predict([email])[0]

if prediction == 1:
    print("\nPrediction: PHISHING EMAIL")
else:
    print("\nPrediction: SAFE EMAIL")

