from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Film, Cinema
from ..serializers import FilmSerializer, CinemaSerializer

@api_view(['GET','POST'])
def filmsview(request):
    if request.method == 'GET':
        films = Film.objects.all()
        serializer = FilmSerializer(films, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FilmSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def filmview(request, filme_id):
    try:
        film = Film.objects.get(film_id = filme_id)
    except Film.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FilmSerializer(film)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FilmSerializer(film, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def cinemasview(request):
    if request.method == 'GET':
        cinemas = Cinema.objects.all()
        serializer = CinemaSerializer(cinemas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CinemaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def cinemaview(request, cinemar_id):
    try:
        cinema = Cinema.objects.get(cinemas_id=cinemar_id)
    except Cinema.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CinemaSerializer(cinema)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CinemaSerializer(cinema, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cinema.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
