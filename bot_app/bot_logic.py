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
    elif "contact" in msg:
        contact(chat_id)
    # enquiry/fees_dues
    elif "fees and dues" in msg:
        fees(chat_id)
    # enquiry/fees_dues/hall_fees
    elif "hall fees" in msg:
        fee(chat_id, 'hall')
    # enquiry/fees_dues/jcr_fees
    elif "jcr fees" in msg:
        fee(chat_id, 'jcr')
    # enquiry/fees_dues/fuel_fees
    elif "fuel fees" in msg:
        fee(chat_id, 'fuel')
    # enquiry/fees_dues/other_fees
    elif "other fees" in msg:
        fee(chat_id, 'other')
    # enquiry/jcr/jcr_executives
    elif "jcr executives" in msg:
        jcr_detail(chat_id, 'executives')
    # enquiry/jcr
    elif "jcr" in msg:
        jcr(chat_id)
    # enquiry/hall_accommodation
    elif "hall accommodation" in msg:
        hall_accomodation(chat_id)
    elif "room application" in msg:
        hall(chat_id, 'room')
    # enquiry/facilities
    elif "facilities" in msg:
        facilities(chat_id)
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
    keyboard_markup = {"keyboard": [["Make an Enquiry", "Lodge a complaint"], ["Contact Support"]], "one_time_keyboard": True}
    reply_keyboard_markup = json.dumps(keyboard_markup)    # converts dict to json

    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response_text, "reply_markup": reply_keyboard_markup})


def info(chat_id):
    about_text = """
        Jubilee Hall, located on the southern part of the campus, adjacent to the International Students‘ Hostel, was built to commemorate the University‘s Golden Jubilee celebration in 1998. Modeled after Akuafo Hall, one of the traditional Halls of the University, and funded mainly by alumni of the University, the Hall is a group of 4 (four) multi-purpose blocks containing single study bedrooms, self-contained flats and double rooms. Facilities in the Hall include common rooms, libraries and restaurants. There are rooms suitable for disabled students.
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


# contact
def contact(chat_id):
    response = """Contact us on xxxxxxxxx or send an email to xxxxxx@xxxx.com. We will reply to you shortly."""
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

    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response_text, "parse_mode":"HTML"})


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
    keyboard_markup = {"keyboard": [["Fees and Dues", "JCR",], ["Hall Accommodation", "Facilities"]], "one_time_keyboard": True}
    reply_keyboard_markup = json.dumps(keyboard_markup)
    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response, "reply_markup": reply_keyboard_markup})


# enquiry/fees_and_dues
def fees(chat_id):
    response = """ Hall fees, JCR fees and any subsequent fees or dues are paid at the bank.
                    \n For more info on where and how to make a payment select one of the options below.
                """

    # ReplyKeyboardMarkup Object
    keyboard_markup = {"keyboard": [["Hall Fees", "JCR Fees"], ["Fuel Fees", "Other Fees"]], "one_time_keyboard": True}
    reply_keyboard_markup = json.dumps(keyboard_markup)
    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response, "reply_markup": reply_keyboard_markup})


# enquiry/fees_and_dues/(hall/jcr/fuel)
def fee(chat_id, type):
    response = ""
    if type == "hall":
        response = """ 
            \n The current residential fees per semester for the 2020/2021 Academic year are:
            <table>
                <tr>
                    <th></th>
                    <th>GHC</th>
                </tr>
                <tr>
                    <td><b>Jubilee Hall (Quadruple)</b></td>
                    <td>613.00</td>
                </tr>
                <tr>
                    <td><b>Jubilee Hall (Self-Contained - Double)</b></td>
                    <td>2,056.00</td>
                </tr>
                <tr>
                    <td><b>Jubilee Hall (Flat with Kitchenette- Double)</b></td>
                    <td>2,305.00</td>
                </tr>
            </table>
            \nPayment of hall fees are made at Consolidated Bank Ghana (CBG).
            \n<b>Account Name:</b> Jubilee Hall
            \n<b>Account Number:</b> xxxxxxxxxxx
            \n\n * Room registration must be completed before payment of fees. (online or manual)
        """
    elif type == "jcr":
        response = """ Payment of JCR fees are made at Consolidated Bank Ghana (CBG).
            \n<b>Account Name:</b> JubileeHallJCR
            \n<b>Account Number:</b> 1400000451187
        """
    elif type == "fuel":
        response = """ Fuel fees are used to manage electric generators/power plants when there are electric outages.
        \n Kindly visit the administrative office for more details on payment of fuel fees.
        """
    else:
        response = """No information on this type of fee. Kindly visit the Administrative office or the porters lodge for more information."""

    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response, "parse_mode":"HTML"})

    # ask user if there is another enquiry.
    another_enquiry(chat_id)


# enquiry/hall_accomaodation
def hall_accomodation(chat_id):
    response = """Accommodation at Jubilee Hall is only accessible to students of the University of Ghana. For more information, Choose one of the options below. 
                """

    # ReplyKeyboardMarkup Object
    keyboard_markup = {"keyboard": [["Room Application", "Accommodation FAQ"], ["Rules and Regulations"]], "one_time_keyboard": True}
    reply_keyboard_markup = json.dumps(keyboard_markup)
    r = requests.get(f"{url}/sendMessage",
                     params={"chat_id": chat_id, "text": response, "reply_markup": reply_keyboard_markup})


# enquiry/hall_accomaodation/ (room_application, accomodation_faq, rules and regulations)
def hall(chat_id, type):
    response = ""
    if type == "room":
        response = """ 
            \n The current residential fees per semester for the 2020/2021 Academic year are:
            <b>Jubilee Hall (Quadruple)</b>\t613.00
            <b>Jubilee Hall (Self-Contained - Double)</b>\t2,056.00
            <b>Jubilee Hall (Flat with Kitchenette- Double)</b>\t2,305.00
            \nPayment of hall fees are made at Consolidated Bank Ghana (CBG).
            \n<b>Account Name:</b> Jubilee Hall
            \n<b>Account Number:</b> xxxxxxxxxxx
            \n\n * Room registration must be completed before payment of fees. (online or manual)
        """
    elif type == "faq":
        response = """"""

    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response, "parse_mode":"HTML"})


# enquiry/jcr
def jcr(chat_id):
    response = """The JCR stands for the Junior Common Room. It made up of a board of students who aid in the management of students(residents) of the hall."""

    # ReplyKeyboardMarkup Object
    keyboard_markup = {"keyboard": [["JCR Executives", "Function of JCR"],], "one_time_keyboard": True}
    reply_keyboard_markup = json.dumps(keyboard_markup)
    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response, "reply_markup": reply_keyboard_markup})


# enquiry/jcr/ (executives, function)
def jcr_detail(chat_id, type):
    if type == "executives":
        response = """
            <b> JCR President </b> - Bright Amansiah Twerefour \n<b> JCR Treasurer </b> - Dem Reggah \n<b> JCR General Secretary </b> - Quartey Theresa Naa Kwarkor \n<b> JCR Organizing Secretary</b> - Vincent Aperko Jubilee \n <b> Chegbeleh Arnold Tonne </b> - Dem Reggah
        """
    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response, "parse_mode": "HTML"})

# enquiry/facilities
def facilities(chat_id):
    response = """Select one of the options below to get the location."""

    # ReplyKeyboardMarkup Object
    keyboard_markup = {"keyboard": [["Study Room", "Discussion Room"], ["Shops"]], "one_time_keyboard": True}
    reply_keyboard_markup = json.dumps(keyboard_markup)
    r = requests.get(f"{url}/sendMessage", params={"chat_id": chat_id, "text": response, "reply_markup": reply_keyboard_markup})



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