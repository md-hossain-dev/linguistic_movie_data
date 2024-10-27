from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import extract_linguistic_data

class ProcessTextView(APIView):
    def post(self, request):
        text = request.data.get('text', None)

        if text is None:
            return Response({"error": "No text provided"}, status=status.HTTP_400_BAD_REQUEST)

        result = extract_linguistic_data(text)

        return Response(result, status=status.HTTP_200_OK)
