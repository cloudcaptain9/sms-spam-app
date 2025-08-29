# SMS Spam Detection App 🚀

This is a simple **SMS Spam Detection web app**. Users can type a message on the web interface, and the backend will predict whether it is **spam** or **not spam** using a trained machine learning model.

---

## Folder Structure

## 📂 Project Structure

```plaintext
root/
├─ frontend/
│  ├─ index.html        # Webpage for user input
│  └─ script.js         # Frontend JavaScript to call backend `/predict`
│
├─ backend
│├─ app.py            # Flask backend serving API + frontend
│├─ requirements.txt  # Python dependencies
│├─ Dockerfile        # Docker setup for backend + frontend
│└─ models/
│     ├─ model.pkl      # Trained machine learning model
│     └─ vectorizer.pkl # Text vectorizer for preprocessing



---

## Features

- **Frontend**: Simple web interface to type messages and view predictions.
- **Backend**: Flask API exposing `/predict` endpoint.
- **Machine Learning**: Uses pre-trained model (`model.pkl`) + vectorizer (`vectorizer.pkl`) to detect spam.
- **Dockerized**: Ready for Docker builds and deployment.
- **Single service**: Flask serves both frontend and backend — no need for Docker Compose.

#check the model_training script for instruction

## Setup Instructions

### Local Development

##clone the repo
1. **https://github.com/cloudcaptain9/sms-spam-app.git**:

```bash
git clone https://github.com/cloudcaptain9/sms-spam-app.git
cd sms-spam-app/backend

python -m venv venv
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate  # Mac/Linux


pip install -r requirements.txt

python app.py

http://localhost:8000


#how to train your models for sms-spam-app chech model-traning folder

Author

Onyekachi Emmanuel (Kachi)
