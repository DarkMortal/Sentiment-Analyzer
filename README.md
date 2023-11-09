# Sentiment Analyzer
## Setting up Virtual Environment in Python
- Install **virtualenv** if not installed already

        pip3 install virtualenv
- Create the **Virtual Environment**

        virtualenv venv
- Activate the **Virtual Environment**

        source venv/bin/activate
## Installing Dependencies
- Get dependencies

        pip3 freeze >> requirements.txt
- Install dependencies

        pip3 install -r requirements.txt
## Launching the application
- To start the application

        streamlit run app.py