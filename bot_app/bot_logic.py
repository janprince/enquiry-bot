import requests
import os
import environ
env = environ.Env()
# reads .env file
environ.Env.read_env("../bot/.env")

token = os.environ["TOKEN"]

def index(name):
    text = f"""
        Hi {name} 👋, 
        \n I can provide some assistance and address your concerns and various enquiries on Jubilee Hall. 
        \n\n Use /start to start a conversation
        \n Use /menu to return to this menu.
        \n Use /help to get the available commands
        \n Use /enquiry if you want to make an enquiry.
        \n\n Use /about or /info to read about Jubilee Hall.
    """
    return text

about = """
    Jubilee Hall, located on the southern part of the campus, adjacent to the
International Students‘ Hostel, was built to commemorate the University‘s Golden Jubilee
celebration in 1998. Modeled after Akuafo Hall, one of the traditional Halls of the University,
and funded mainly by alumni of the University, the Hall is a group of 4 (four) multi-purpose
blocks containing single study bedrooms, self-contained flats and double rooms. Facilities in
the Hall include common rooms, libraries and restaurants. There are rooms suitable for
disabled students.
\n
\n GPS Address: 
\n Contact: 
\n
\n <b>JCR President</b>: 
\n Hall Head / Senior Tutor: 
"""


def generate_response(firstname, chat_id, msg):
    msg = msg.lower()
    response = ""

    if "hi" in msg or "hello" in msg or "good" in msg:
        response = f"Hello {firstname}"
    elif "/start" in msg:
        response = index(firstname)
    elif "/about" in msg or "/info" in msg:
        response = about

    send_msg(chat_id, response)


def send_msg(chat_id, response_text):
    token = os.environ["TOKEN"]
    url = f"https://api.telegram.org/bot{token}"
    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response_text})
    r = requests.get(f"{url}/ReplyKeyboardMarkup", params={"keyboard": [['/start', '/info']]})
