from .process_config import *
from .sale_request.sale_request_processor import *
import requests
from num2words import num2words
from googletrans import Translator

UAT_API = "https://uatapi.grainbank.in/api/util/v1/getBuyerBalance"
PROD_API = "https://prodapi.grainbank.in/api/util/v1/getBuyerBalance"


def call_api(request_type, user_request):
    try:
        if user_request["Env"] == "uat":
            endpoint = UAT_API + "?userId=" + str(user_request["userId"]) + "&typeCode=" + str(request_type)
        else:
            endpoint = PROD_API + "?userId=" + str(user_request["userId"]) + "&typeCode=" + str(request_type)
        response = requests.get(endpoint, headers={
            "x-api-key": "A12JKL12890uihBCLP",
            "Content-Type": "application/json"
        })
        print(response.json())
        if response.status_code == 200:
            return response.json()
        else:
            return ""

    except Exception as e:
        print(e)
        return ""


def process_request(text, user_request, lang):
    try:
        intent_type = process_config[text]
        response = call_api(intent_type, user_request)
        if response == "":
            print("Error at the API side")
            return error_message[lang]
        message = message_config[intent_type]
        meta_data = {}
        readableMessage = ""
        redirect = ""
        if intent_type == 1:
            readableMessage = message.replace("{0}", "₹ {:,}".format(response["LedgerBalance"]))
            message = message.replace("{0}",
                                      num2words(response["LedgerBalance"]))
            readableMessage = readableMessage.replace("Rupees", "")
        elif intent_type == 2:
            readableMessage = message.replace("{0}", "₹ {:,}".format(response["PurchaseBalance"]))
            message = message.replace("{0}",
                                      num2words(response["PurchaseBalance"]))
            readableMessage = readableMessage.replace("Rupees", "")
        elif intent_type == 3:
            readableMessage = message.replace("{0}", "₹ {:,}".format(response["LedgerBalance"]))
            readableMessage = readableMessage.replace("{1}", "₹ {:,}".format(response["PurchaseBalance"]))
            message = message.replace("{0}",
                                      num2words(response["LedgerBalance"]))
            message = message.replace("{1}",
                                      num2words(response["PurchaseBalance"]))
            readableMessage = readableMessage.replace("Rupees", "")
        elif intent_type == 4:
            readableMessage = message.replace("{0}", "₹ {:,}".format(response["TotalCredit"]))
            message = message.replace("{0}",
                                      num2words(response["TotalCredit"]))
            readableMessage = readableMessage.replace("Rupees", "")
        elif intent_type == 5:
            readableMessage = message.replace("{0}", "₹ {:,}".format(response["TotalDebit"]))
            message = message.replace("{0}",
                                      num2words(response["TotalDebit"]))
            readableMessage = readableMessage.replace("Rupees", "")
        elif intent_type == 7:
            readableMessage = message
            redirect = "PURCHASE_STOCK"
        elif intent_type == 8:
            readableMessage = message
            redirect = "SALE_REQUEST"
        elif intent_type == 9:
            readableMessage = message
            redirect = "ADVANCE_PAYMENT"
        elif intent_type == 10:
            readableMessage = message
            redirect = "SPOT_PURCHASE"
        elif intent_type == 11:
            readableMessage = message
            redirect = "STOCK_RELEASE"
        translator = Translator()
        message = translator.translate(message, src='en', dest=lang_codes[lang]).text
        readableMessage = translator.translate(readableMessage, src='en', dest=lang_codes[lang]).text
        return message, readableMessage, meta_data, redirect
    except Exception as e:
        print(e)
        return error_message[lang]
