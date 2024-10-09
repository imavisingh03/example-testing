from flask import Flask, request, render_template
import requests
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup
    
def is_phishing_url(url):
    try:
        # Step 1: Check URL format
        if not re.match(r"^https?://", url, re.IGNORECASE):
            return True
            
        # Step 2: Fetch webpage content
        response = requests.get(url)
        if response.status_code != 200:
            return False
            
        # Step 3: Analyze HTML content for phishing indicators
        soup = BeautifulSoup(response.text, 'html.parser')
            
        # Look for suspicious keywords in the HTML content
        suspicious_keywords = ['login', 'password', 'credit', 'bank', 'secure']
        for keyword in suspicious_keywords:
            if keyword in soup.get_text().lower():
                return True
            
        # Step 4: Check the URL against known phishing databases (you can extend this list)
        known_phishing_domains = [
            "example-phishing.com",
            "phishingsite.org",
            #  Add more known phishing domains here
        ]
        domain = urlparse(url).netloc
        if domain in known_phishing_domains:
            return True
        
        file29 = open('phishing_urls.txt','r')
        file29_contents = file29.read()

        if domain in file29_contents:
            return True


        # Step 5: Additional checks (you can add more checks as needed)
        # Example: Checking if the URL redirects to a different domain
            
        # Step 6: If none of the checks above indicate phishing, return False
            return False
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
    


# ______WEB FRAMEWORK_______


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=["POST"])
def submit():
    
    if request.method == "POST":
        user_input = request.form.get("URL")
        print(user_input)
        
        # Do something with user_input, e.g., process it or return a response
        result = f"You entered: {user_input}"
        # print(result)
        url_to_check = user_input  # Replace with the URL you want to check
    
    if is_phishing_url(url_to_check):
        verdict = f"The URL {url_to_check} is likely a phishing URL."
    else:
        verdict = f"The URL {url_to_check} appears to be safe."

    return verdict

if __name__ == '__main__':
    app.debug = True
    app.run()