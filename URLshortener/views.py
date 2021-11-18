from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Shortener
from .serializers import ShortenerSerializer


# Function for creating new instance of Shortener
@api_view(['POST'])
def create_short_URL(request):
    serializer = ShortenerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    return Response('http://localhost:8000/s/{0}'.format(serializer.data['short_url']), status=status.HTTP_201_CREATED)


# Function for incrementing "hit_counter" field and redirecting from short to long URL
@api_view(['GET'])
def redirect_from_short_to_long_URL(request, short_url):
    try:
        shortener = Shortener.objects.get(short_url=short_url)
        shortener.hit_counter += 1
        shortener.save()

        return HttpResponseRedirect(shortener.url)
    except:
        return Response('No matches found!', status=status.HTTP_404_NOT_FOUND)
