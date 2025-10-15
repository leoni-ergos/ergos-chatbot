from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ergos_assistant.UserIntent import process
from .data_fetcher import process_request
from .process_config import *


class ProcessUserInputView(APIView):
    def post(self, request):
        try:
            userRequest = request.data
            print(userRequest)
            if 'Env' not in userRequest:
                return Response({"error": "Required 'Env'"}, status=status.HTTP_400_BAD_REQUEST)
            elif 'text' not in userRequest:
                return Response({"error": "Required 'text'"}, status=status.HTTP_400_BAD_REQUEST)
            if 'userId' not in userRequest:
                return Response({"error": "Required 'userId'"}, status=status.HTTP_400_BAD_REQUEST)
            processed, lang = process(text=userRequest['text'])
            if lang in codes_lang:
                langCode = codes_lang[lang]
                if processed == "out_of_scope":
                    return Response(
                        {"code": 200, "status": "success",
                         "data": {"message": error_message[langCode], "langCode": langCode}
                         },
                        status=status.HTTP_200_OK)
                message, readableMessage, metaData, redirect = process_request(processed, userRequest, langCode)
                return Response(
                    {"code": 200, "status": "success",
                     "data": {"message": message, "readableMessage": readableMessage, "langCode": langCode,
                              "metaData": metaData, "redirectionCode": redirect}},
                    status=status.HTTP_200_OK)

            else:
                return Response(
                    {"code": 200, "status": "success",
                     "data": {"message": "Apologies, I'm unable to process your request", "langCode": 1}
                     },
                    status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error": "Internal server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProcessUserInput(APIView):
    def post(self, request):
        print("Entered")
        response = {"code": 200, "status": "success"}
        userRequest = request.data
        if userRequest["langId"] == 3:
            response["data"] = "धान हाइब्रिड"
        return Response(response, status.HTTP_200_OK)
