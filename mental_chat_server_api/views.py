from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from google import genai
import environ
import os


env = environ.Env()
env.read_env(env.str('ENV_PATH', '.env'))
goolge_key = env("GOOGLE_KEY", default="Key not found")


# Create your views here.
class GoogleAPIView(APIView):
    def post(self, request, format=None):
        response = self._get_google_response(request.data.get("message"))

        return Response({
            "message": response
        })

    def _get_google_response(self, message):
        client = genai.Client(api_key=goolge_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=message
        )
        return response.text

