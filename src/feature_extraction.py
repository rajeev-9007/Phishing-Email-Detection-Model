import re

def extract_features(email):

    features = {}

    urls = re.findall(r'https?://\S+|www\.\S+', email)

    features['url_count'] = len(urls)

    phishing_keywords = [
        'verify',
        'password',
        'bank',
        'urgent',
        'click',
        'winner',
        'account',
        'login'
    ]

    email_lower = email.lower()

    features['keyword_count'] = sum(
        keyword in email_lower
        for keyword in phishing_keywords
    )

    return features


sample = """
Verify your account now.
Click here: https://fake-bank.com
"""

print(extract_features(sample))