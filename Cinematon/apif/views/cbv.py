from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ..models import Hall, Session, Film, BookedTicket
from ..serializers import UserSerializer, HallSerializer, SessionSerializer, FilmSerializer, TicketSerializer

class HallListAPIView(APIView):

    def get(self, request):
        halls = Hall.objects.all()
        serializer = HallSerializer(halls, many= True)
        return Response(serializer.data)
    def post(self, request):
        serializer = HallSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)

class HallDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Hall.objects.get(pk=pk)
        except Hall.DoesNotExist:
            return None

    def get(self, request, pk):
        hall = self.get_object(pk)
        if not hall:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = HallSerializer(hall)
        return Response(serializer.data)

    def put(self, request, pk):
        hall = self.get_object(pk)
        if not hall:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = HallSerializer(hall, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        hall = self.get_object(pk)
        if not hall:
            return Response(status=status.HTTP_404_NOT_FOUND)

        hall.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SessionListAPIView(APIView):

    def get(self, request):
        sessions = Session.objects.all()
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SessionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SessionDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Session.objects.get(pk=pk)
        except Session.DoesNotExist:
            return None

    def get(self, request, pk):
        session = self.get_object(pk)
        if not session:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SessionSerializer(session)
        return Response(serializer.data)

    def put(self, request, pk):
        session = self.get_object(pk)
        if not session:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SessionSerializer(session, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        session = self.get_object(pk)
        if not session:
            return Response(status=status.HTTP_404_NOT_FOUND)

        session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HallsByCinema(APIView):
    def get(self, request, cinema_id):
        halls = Hall.objects.filter(cinema = cinema_id)
        serializer = HallSerializer(halls, many = True)
        return Response(serializer.data)

class SessionsByHall(APIView):
    def get(self, request, hall_id):
        sessions = Session.objects.filter(hall = hall_id)
        serializer = SessionSerializer(sessions, many = True)
        return Response(serializer.data)
    def delete(self, request, hall_id):
        sessions = Session.objects.filter(hall = hall_id)
        if not sessions.exists():
            return Response(status = status.HTTP_404_NOT_FOUND)
        sessions.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)

class SessionsByFilm(APIView):
    def get(self, request, film_id):
        sessions = Session.objects.filter(film = film_id)
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)

    def post(self, request, film_id):
        if not Film.objects.filter(pk=film_id).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SessionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(film_id=film_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FilmByGenre(APIView):
    def get(self, request, genre):
        films = Film.objects.filter(genre = genre)
        serializer = FilmSerializer(films, many = True)
        return Response(serializer.data)

class BookedTicketListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tickets = BookedTicket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TicketSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TicketsByUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tickets = BookedTicket.objects.filter(user=request.user)
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

class BookedTicketDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return BookedTicket.objects.get(pk=pk)
        except BookedTicket.DoesNotExist:
            return None

    def delete(self, request, pk):
        ticket = self.get_object(pk)

        if not ticket:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if ticket.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)