from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.authentication import authenticate
from django.http import HttpResponse
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
import base64
from .process import process_image
from PIL import Image
import os

from html2image import Html2Image
hti = Html2Image()

@api_view(['POST'])
def process(request):
    body = request.data
    file_base64 = body["file"]
    file = base64.b64decode(file_base64)
    with open("file.png", "wb") as f:
        f.write(file)
    
    file = Image.open("file.png", 'r')
    
    image = process_image(file, body["processes"])
    
    image.save("file.png")
    
    file = open("file.png", 'rb')



    # Return the processed file
    response = HttpResponse(file, content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename=NameOfFile'
    file.close()    
    # os.remove("file.png")
    return response