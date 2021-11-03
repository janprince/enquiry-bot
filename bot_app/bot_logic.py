import requests
import os
import environ
import json

env = environ.Env()
# reads .env file
environ.Env.read_env("../bot/.env")

# telegram bot token
token = os.environ["TOKEN"]

#telegram bot api base_url
url = f"https://api.telegram.org/bot{token}"


#functions

def index(firstname, chat_id):
    response_text = f"""
        Hi {firstname} 👋,
        \n I can provide some assistance and address your concerns and various enquiries on Jubilee Hall.
        \n\n Use /start to start a conversation
        \n Use /menu to get the list of commands.
        \n Use /enquiry if you want to make an enquiry.
        \n\n Use /about or /info to read about Jubilee Hall.
    """

    # ReplyKeyboardMarkup Object
    keyboard_markup = {"keyboard": [["Make an Enquiry", "Lodge a complaint"]], "one_time_keyboard": True}
    reply_keyboard_markup = json.dumps(keyboard_markup)    # converts dict to json

    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response_text, "reply_markup": reply_keyboard_markup})


def info(chat_id):
    about_text = """
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
    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": about_text})


def enquiry(chat_id):
    response = "What is your enquiry about?"

    # ReplyKeyboardMarkup Object
    keyboard_markup = {"keyboard": [["Hall Accommodation", "Services"], ["Fees and Dues", "JCR"], ["Facilities"]], "one_time_keyboard": True}
    reply_keyboard_markup = json.dumps(keyboard_markup)
    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response, "reply_markup": reply_keyboard_markup})


def complaint(chat_id):
    response = "What is your enquiry about?"

    # ReplyKeyboardMarkup Object
    keyboard_markup = {"keyboard": [["qwerty", "qwerty"]], "one_time_keyboard": True}
    reply_keyboard_markup = json.dumps(keyboard_markup)
    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response, "reply_markup": reply_keyboard_markup})


def greet(name, chat_id):
    response = f"Hello, {name}"
    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response})


def exception(chat_id):
    response = "Sorry, I don't quite get that."
    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response})


def exit(chat_id):
    response = "👋 Bye! I hope we can talk again some day."
    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response})


def generate_response(firstname, chat_id, msg):
    msg = msg.lower()

    if "hi" in msg or "hello" in msg or "good" in msg:
        greet(firstname, chat_id)
    elif "/start" in msg:
        index(firstname, chat_id)
    elif "/about" in msg or "/info" in msg:
        info(chat_id)
    elif "/enquiry" in msg or "enquiry" in msg:
        enquiry(chat_id)
    elif "/compliant" in msg or "complaint" in msg:
        complaint(chat_id)
    elif "/cancel" in msg:
        exit(chat_id)
    else:
        exception(chat_id)



# def send_msg(chat_id, response_text):
#     token = os.environ["TOKEN"]
#     url = f"https://api.telegram.org/bot{token}"
#     reply_markup={"keyboard":[["Make an Enquiry","Lodge a complaint"]],"one_time_keyboard":True}
#     x = json.dumps(reply_markup)
#     r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response_text, "reply_markup": x})
