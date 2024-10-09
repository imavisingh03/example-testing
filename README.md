# Phishing_url_Detector

## Description
Phishing Net Prototype Overview This project focuses on detecting phishing websites and links using Artificial Intelligence (AI) and Machine Learning (ML). Phishing attacks use fake websites or messages to trick users into revealing personal information, such as passwords or financial details. The goal of this project is to build a system that automatically identifies and alerts users about these fake websites and messages in real time.

### Features Phishing Detection via SMS: 
Identifies fake text messages that pretend to be from legitimate sources. Phishing Detection via Email: Detects malicious emails designed to steal sensitive information. Domain Spoofing Detection: Spots websites that imitate legitimate domains. URL Obfuscation Detection: Reveals hidden or misleading URLs that could redirect users to harmful sites.

How It Works The system operates as a browser extension that runs in the background, analyzing website links, SMS, and emails for phishing threats. When a user visits a site or clicks on a link, the extension communicates with the backend (built on Flask) to determine if the content is legitimate or harmful. a threat is detected, the user is immediately alerted.

### Technology Used:
Flask: A tool that helps build the backend of the project, managing the server and testing the system. React: A tool used to create a user-friendly interface for the browser extension. Open Source Intelligence (OSINT): Collecting and analyzing publicly available information to help spot phishing attempts.

## How to run the project
First, run this command on your command prompt or terminal:

Clone this project.

-> pip install virtualenv

Second, do the following:

-> python -m venv “name of virtual environment”

Here you can give a name to the environment. I usually give it a name of venv. It will look like this: venv venv.
After setting up virtual environment, check your project folder. It should look like this. The virtual environment needs to be created in the same directory where your app files are located.

---------------------------------------------------------Activating the virtual environment------------------------------------------------------

Now go to your terminal or command prompt. Go to the directory that contains the file called activate. The file called activate is found inside a folder called Scripts for Windows and bin for OS X and Linux.

#### For OS X and Linux Environment:

-> $ name of virtual environmnet/bin/activate
              or
#### For Windows Environment:

-> name of virtual environment\Scripts\activate

You should see this at beginning of your command prompt line

(virutal)

The next step is to install flask on your virtual environment so that we can run the application inside our environment. Run the command:

-> pip install flask

Run your application and go to http://localhost:5000/
by commanding

-> flask run

## Credits

--END--
