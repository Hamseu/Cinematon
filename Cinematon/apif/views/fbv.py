from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication

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

@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is None:
        return Response({"error": "Invalid credentials"}, status=400)

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    response = Response({"message": "Logged in"})

    response.set_cookie(
        key="access",
        value=access_token,
        httponly=True,
        secure=False,  # True in production
        samesite="Lax"
    )

    return response

@api_view(["POST"])
def logout(request):
    response = Response({"message": "Logged out"})
    response.delete_cookie("access")
    return response

@api_view(['POST'])
def refresh_token(request):
    refresh_token = request.COOKIES.get('refresh')

    if not refresh_token:
        return Response(
            {"detail": "Refresh token missing"},
            status=status.HTTP_401_UNAUTHORIZED
        )

    try:
        refresh = RefreshToken(refresh_token)
        access_token = str(refresh.access_token)

    except Exception:
        return Response(
            {"detail": "Invalid refresh token"},
            status=status.HTTP_401_UNAUTHORIZED
        )

    response = Response({"access": access_token}, status=status.HTTP_200_OK)
    response.set_cookie(
        key="access",
        value=access_token,
        httponly=True,
        secure=False,
        samesite="Lax",
        path="/"
    )

    return response