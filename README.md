# Phishing Email Detection Model

A Machine Learning based phishing email detection system built using Python and Scikit-learn. The model analyzes email content and classifies emails as either **Phishing** or **Legitimate (Safe)**.

## Features

* Email text preprocessing
* Feature extraction using TF-IDF
* Phishing email classification
* Trained model saved using Pickle
* Classification report generation
* Confusion matrix visualization

## Project Structure

```text
Phishing-Email-Detection/
│
├── dataset/
│   └── phishing_email.csv
│
├── models/
│   └── phishing_model.pkl
│
├── outputs/
│   ├── classification_report.txt
│   └── confusion_matrix.png
│
├── src/
│   ├── feature_extraction.py
│   ├── train.py
│   └── predict.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Phishing-Email-Detection.git
cd Phishing-Email-Detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Training

Run the training script:

```bash
python src/train.py
```

The trained model will be saved inside the `models` directory.

## Prediction

Run prediction script:

```bash
python src/predict.py
```

## Output

* Trained Model (`phishing_model.pkl`)
* Classification Report (`classification_report.txt`)
* Confusion Matrix (`confusion_matrix.png`)

## Technologies Used

* Python
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Joblib / Pickle

## Future Improvements

* Real-time phishing detection
* URL reputation analysis
* Email header analysis
* Deep Learning based classification

## License

This project is intended for educational and cybersecurity learning purposes.

