import requests
import os
import environ
import json
import time

env = environ.Env()
# reads .env file
environ.Env.read_env("../bot/.env")

# telegram bot token
token = os.environ["TOKEN"]

# telegram bot api base_url
url = f"https://api.telegram.org/bot{token}"


"""-------------------Conditional statements----------------------"""

def generate_response(firstname, chat_id, msg):
    """
    :param firstname: effective_user_name
    :param chat_id: effective_chat_id
    :param msg: message

    checks for patterns in message and calls the appropriate response function.
    """
    msg = msg.lower()

    if "hi" in msg or "hello" in msg or "good" in msg:
        greet(firstname, chat_id)
    elif "/start" in msg:
        index(firstname, chat_id)
    elif "/about" in msg or "/info" in msg:
        info(chat_id)
    elif "/menu" in msg or 'menu' in msg:
        menu(chat_id)
    elif "/enquiry" in msg or "enquiry" in msg:
        enquiry(chat_id)
    elif "/compliant" in msg or "complaint" in msg:
        complaint(chat_id)
    elif "/cancel" in msg or "no, that's it for now" in msg or '/exit' in msg or 'bye' in msg:
        exit(firstname, chat_id)
    elif "fees and dues" in msg:
        fees(chat_id)
    elif "hall fees" in msg:
        fee(chat_id, 'hall')
    elif "jcr fees" in msg:
        fee(chat_id, 'jcr')
    else:
        exception(chat_id)



"""----------------------------------------------- General --------------------------------------------------------"""


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
        Jubilee Hall, located on the southern part of the campus, adjacent to the International Students‘ Hostel,
        was built to commemorate the University‘s Golden Jubilee celebration in 1998. Modeled after Akuafo Hall,
        one of the traditional Halls of the University, and funded mainly by alumni of the University,
        the Hall is a group of 4 (four) multi-purpose blocks containing single study bedrooms, self-contained
        flats and double rooms. Facilities in the Hall include common rooms, libraries and restaurants.
        There are rooms suitable for disabled students.
        \n
        \n GPS Address: John Doe
        \n Contact:     John Doe
        \n
        \n <b>JCR President</b>:    John Doe
        \n <b>Hall Head / Senior Tutor</b>: John Doe
    """
    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": about_text, "parse_mode":"HTML"})


def greet(name, chat_id):
    response = f"Hello, {name}"
    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response})


def menu(chat_id):
    response_text = f"""
        <b>Commands</b>
        \n Use /start to start a conversation
        \n Use /menu to get the list of commands.
        \n Use /enquiry if you want to make an enquiry.
        \n Use /complaint to lodge a complaint
        \n Use /cancel or /exit to cancel a conversation
        \n\n Use /about or /info to read about Jubilee Hall.
    """

    # # ReplyKeyboardMarkup Object
    # keyboard_markup = {"keyboard": [["Make an Enquiry", "Lodge a complaint"]], "one_time_keyboard": True}
    # reply_keyboard_markup = json.dumps(keyboard_markup)    # converts dict to json

    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response_text, "reply_markup": reply_keyboard_markup, "parse_mode":"HTML"})


def exception(chat_id):
    response = "Sorry, I don't quite get that."
    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response})


def exit(name, chat_id):
    response = "👋 Bye {} I hope we can talk again some day.".format(name)
    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response, "remove_keyboard": True})


# def send_msg(chat_id, response_text):
#     token = os.environ["TOKEN"]
#     url = f"https://api.telegram.org/bot{token}"
#     reply_markup={"keyboard":[["Make an Enquiry","Lodge a complaint"]],"one_time_keyboard":True}
#     x = json.dumps(reply_markup)
#     r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response_text, "reply_markup": x})


"""----------------------------------------------- Enquiry --------------------------------------------------------"""


def enquiry(chat_id):
    response = "What is your enquiry about?"

    # ReplyKeyboardMarkup Object
    keyboard_markup = {"keyboard": [["Hall Accommodation", "Services"], ["Fees and Dues", "JCR"], ["Facilities"]], "one_time_keyboard": True}
    reply_keyboard_markup = json.dumps(keyboard_markup)
    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response, "reply_markup": reply_keyboard_markup})


# fees
def fees(chat_id):
    response = """ Hall fees, JCR fees and any subsequent fees or dues are paid at the bank.
                    \n For more info on where and how to make a payment select one of the options below.
                """

    # ReplyKeyboardMarkup Object
    keyboard_markup = {"keyboard": [["Hall Fees", "JCR Fees"], ["Fuel Fees", "Other Fees"]], "one_time_keyboard": True}
    reply_keyboard_markup = json.dumps(keyboard_markup)
    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response, "reply_markup": reply_keyboard_markup})


def fee(chat_id, type):
    response = ""
    if type == "hall":
        response = """ Payment of hall fees are made at Consolidated Bank Ghana (CBG).
            \n<b>Account Name:</b> Jubilee Hall
            \n<b>Account Number:</b> xxxxxxxxxxx
        """
    elif type == "jcr":
        response = """ Payment of JCR fees are made at Consolidated Bank Ghana (CBG).
            \n<b>Account Name:</b> JubileeHallJCR
            \n<b>Account Number:</b> 1400000451187
        """
    elif type == 'fuel':
        response = """"""

    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response, "parse_mode":"HTML"})

    # ask user if there is another enquiry.
    another_enquiry(chat_id)


# hall accomodation

# jcr



"""----------------------------------------------- Complaint --------------------------------------------------------"""


def complaint(chat_id):
    response = "Click on the button below to lodge a complaint."

    # InlineKeyboardMarkup Object
    inline_keyboard = {"inline_keyboard": [[{"text": "Complaint Form", "url": "https://forms.gle/CyxAzJSc2gryPYuN9", "callback_data": "Form Opened"}],]}
    inline_keyboard_markup = json.dumps(inline_keyboard)
    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response, "reply_markup": inline_keyboard_markup})




"""---------------------------------------- User done ------------------------------------------------------"""

def another_enquiry(chat_id):
    """
    this function is run when a user is done with an enquiry.
    """
    time.sleep(3)
    response = "Would you like to make another enquiry ?"

    # ReplyKeyboardMarkup Object
    keyboard_markup = {"keyboard": [["Yes, I would like to make another enquiry ?", "No, that's it for now."]], "one_time_keyboard": True}
    reply_keyboard_markup = json.dumps(keyboard_markup)
    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response, "reply_markup": reply_keyboard_markup})