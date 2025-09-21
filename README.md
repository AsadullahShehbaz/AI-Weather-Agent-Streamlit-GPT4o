# 🌦️ AI Weather Agent (Streamlit + Gemini)

This is an **AI Weather Assistant** built with **Streamlit** that uses  
**Gemini model API** to understand user queries,  
plan reasoning steps, and fetch real-time weather data through external tools.  

🚀 Deployed as a chat-style agent with chain-of-thought reasoning and tool calling.

---

## ✨ Features
- 🤖 Powered by **Gemini** (via [Gemini]([Gemini](https://gemini.google.com/app)))  
- 🌐 Fetches real-time weather using [wttr.in](https://wttr.in) API  
- 🧠 Uses **chain-of-thought planning**: START → PLAN → TOOL → OBSERVE → OUTPUT  
- 💬 Interactive **Streamlit chat interface** with conversation history  
- 🔑 Secure API key handling using `.env` or `st.secrets`  

---

## 🛠️ Tech Stack
- [Streamlit](https://streamlit.io/) – UI & deployment  
- [GEmini]([https://platform.openai.com/](https://gemini.google.com/app)) – reasoning & tool calling  
- [Pydantic](https://docs.pydantic.dev/) – structured response parsing  
- [wttr.in](https://wttr.in) – real-time weather data  

---

## 📂 Project Structure
AI-Weather-Agent-Streamlit-GPT4o/
│── app.py # Main Streamlit app
│── requirements.txt # Dependencies
│── .env.example # Example for API key storage
│── README.md # Project documentation


---

## ⚙️ Setup & Installation

1. **Clone the repo**  
```bash
git clone https://github.com/asadullahshehbaz/AI-Weather-Agent-Streamlit-GPT4o.git
cd AI-Weather-Agent-Streamlit-GPT4o
```
2.Create & activate virtual environment (optional but recommended)
```python
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
```
3.Install Dependencies
```python
pip install -r requirements.txt
```

## 🧑‍💻 Author

<h3 align="center">Hi 👋, I'm Asadullah Shehbaz</h3>
<h4 align="center">🚀 Data Scientist | 🤖 ML Engineer | 📊 AI Enthusiast</h4>

- 🔭 I’m working on real-world AI projects to solve problems with data  
- 🌱 Currently exploring: **Deep Learning** & **Time Series Forecasting**  
- 💬 Ask me about: `Python`, `Machine Learning`, `Deep Learning`, `EDA`  
- 📫 Reach me at: **asadullahcreative@gmail.com**  
- ⚡ Fun fact: I turn coffee ☕ into code  

### 🔗 Connect With Me

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/asadullah-shehbaz-18172a2bb/) 
[![Facebook](https://img.shields.io/badge/-Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://web.facebook.com/profile.php?id=61576230402114) 
[![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/asad_ullahshehbaz/) 
[![Kaggle](https://img.shields.io/badge/-Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/asadullahcreative) 

