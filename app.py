import streamlit as st
from openai import OpenAI
import os
import json
import requests
from pydantic import BaseModel, Field
from typing import Optional

# -------------------
# Load environment
# -------------------

api_key= st.secrets["GEMINI_API_KEY"]


client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# -------------------
# Tool: Weather Fetcher
# -------------------
def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    else:
        return f"⚠️ Something went wrong while fetching weather for {city}"

available_tools = {
    "get_weather": get_weather,
    "Get_current_weather": get_weather,
    "get_current_weather" : get_weather,# alias
    "weather": get_weather,              # alias
}
# -------------------
# System Prompt
# -------------------
SYSTEM_PROMPT = """
You're an expert AI Assistant in resolving user queries using chain of thought.
(omitted here for brevity – keep your original SYSTEM_PROMPT text)
"""

# -------------------
# Pydantic Schema
# -------------------
class MyOutputFormat(BaseModel):
    step: str = Field(..., description="START | PLAN | OUTPUT | TOOL | OBSERVE")
    content: Optional[str] = None
    tool: Optional[str] = None
    input: Optional[str] = None

# -------------------
# Streamlit App
# -------------------
st.set_page_config(page_title="ChatGPT-Style AI Agent", page_icon="🤖", layout="centered")

st.markdown(
    "<h1 style='text-align: center; color: #FFD700;'>🌤️ AI Weather Agent 🌩️</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; color: #CCCCCC; font-size:16px;'>Chat with a smart AI assistant to get real-time weather updates (Gemini + Streamlit) 🌦️</p>",
    unsafe_allow_html=True
)


# Clear chat button
if st.button("🧹 Clear Chat"):
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    st.session_state.chat_history = []
    st.rerun()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input (chat box style)
user_query = st.chat_input("Type your message...")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.session_state.chat_history.append(("user", user_query))

    while True:
        response = client.chat.completions.parse(
            model='gemini-2.5-flash',
            response_format=MyOutputFormat,
            messages=st.session_state.messages
        )

        raw_result = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": raw_result})

        parsed = response.choices[0].message.parsed

        # Handle steps
        if parsed.step == "START":
            st.session_state.chat_history.append(("assistant", f"🔥 {parsed.content}"))
            continue

        elif parsed.step == "PLAN":
            st.session_state.chat_history.append(("assistant", f"🧠 {parsed.content}"))
            continue

        elif parsed.step == "TOOL":
            tool_name = parsed.tool
            tool_input = parsed.input
            tool_response = available_tools[tool_name](tool_input)

            st.session_state.chat_history.append(("assistant", f"🛠️ Using {tool_name}({tool_input})"))
            st.session_state.messages.append({
                "role": "developer",
                "content": json.dumps({
                    "step": "OBSERVE",
                    "tool": tool_name,
                    "input": tool_input,
                    "output": tool_response
                })
            })
            continue

        elif parsed.step == "OUTPUT":
            st.session_state.chat_history.append(("assistant", f"🤖 {parsed.content}"))
            break

# -------------------
# Display chat history (ChatGPT UI style)
# -------------------
for role, msg in st.session_state.chat_history:
    if role == "user":
        # Right-aligned bubble (user)
        st.markdown(
            f"""
            <div style="display: flex; justify-content: flex-end; margin: 5px;">
                <div style="background-color: #056162; color: #E1F5F4; padding: 10px 15px; border-radius: 12px; max-width: 70%; text-align: left;">
                    <b>👤 You:</b> {msg}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        # Left-aligned bubble (bot)
        st.markdown(
            f"""
            <div style="display: flex; justify-content: flex-start; margin: 5px;">
                <div style="background-color: #2B2B2B; color: #F0F0F0; padding: 10px 15px; border-radius: 12px; max-width: 70%; text-align: left;">
                    {msg}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )





