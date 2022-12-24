from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import authenticate
from django.http import HttpResponse

from html2image import Html2Image
hti = Html2Image()

@api_view(['POST'])
def html_to_image(request):
    body = request.data
    
    hti.screenshot(html_str=body["html"],
                   css_str=body["css"], save_as=body["filename"], size=(body["width"], body["height"]))
    
    file = open(body["filename"], 'rb')
    
    response = HttpResponse(file, content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename=NameOfFile'
    return response