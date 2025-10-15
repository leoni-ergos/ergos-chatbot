process_config = {
    "ledger_balance": 1,
    "purchasing_power": 2,
    "financial_statement": 3,
    "total_credits": 4,
    "total_debits": 5,
    "purchase_stock": 7,
    "create_sale_request": 8,
    "create_loan_request": 9,
    "create_spot_purchase": 10,
    "create_stock_release": 11
}

error_message = {
    1: "Apologies, I'm unable to process your request",
    3: "क्षमा करें, मैं आपके अनुरोध को संसाधित करने में असमर्थ हूं",
    10: "ಕ್ಷಮಿಸಿ, ನಿಮ್ಮ ವಿನಂತಿಯನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಲು ನನಗೆ ಸಾಧ್ಯವಾಗುತ್ತಿಲ್ಲ.",
    9: "माफ करा, मी तुमच्या विनंतीवर प्रक्रिया करू शकत नाही."
}

message_config = {
    1: "Your ledger balance is {0} Rupees.",
    2: "Your purchasing power is {0} Rupees.",
    3: "Your ledger balance is {0} Rupees and Your purchasing power is {1} Rupees.",
    4: "Your total credit is {0} Rupees.",
    5: "Your total debit is {0} Rupees.",
    7: "Sure, we'll be redirecting you to the purchase screen and guide you from there.",
    8: "Sure, we'll be redirecting you to the sale request creation form.",
    9: "Sure, we'll be redirecting you to the loan request creation form.",
    10: "Sure, we'll be redirecting you to the spot purchase creation form.",
    11: "Sure, we'll be redirecting you to the stock release creation form."
}

lang_codes = {
    1: 'en',
    3: 'hi',
    9: 'mr',
    10: 'kn'
}

codes_lang = {
    'en': 1,
    'hi': 3,
    'mr': 3,
    'kn': 10
}
