from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    HallListAPIView,
    HallDetailAPIView,
    SessionListAPIView,
    SessionDetailAPIView,
    SessionsByFilm,
    SessionsByHall,
    HallsByCinema,
    FilmByGenre,
    BookedTicketListAPIView,
    BookedTicketDetailAPIView,
    TicketsByUserAPIView,
    FilmsListView,
    FilmDetailView,
    CinemaDetailView,
    CinemasDetailView,
    RegisterAPIView,
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='refresh'),

    path('films/', FilmsListView),
    path('films/<int:filme_id>/', FilmDetailView),
    path('films/genre/<str:genre>/', FilmByGenre.as_view()),

    path('cinemas/', CinemasDetailView),
    path('cinemas/<int:cinemar_id>/', CinemaDetailView),
    path('cinemas/<int:cinema_id>/halls/', HallsByCinema.as_view()),

    path('halls/', HallListAPIView.as_view()),
    path('halls/<int:pk>/', HallDetailAPIView.as_view()),
    path('halls/<int:hall_id>/sessions/', SessionsByHall.as_view()),

    path('sessions/', SessionListAPIView.as_view()),
    path('sessions/<int:pk>/', SessionDetailAPIView.as_view()),
    path('films/<int:film_id>/sessions/', SessionsByFilm.as_view()),

    path('tickets/', BookedTicketListAPIView.as_view()),
    path('tickets/<int:pk>/', BookedTicketDetailAPIView.as_view()),
    path('tickets/my/', TicketsByUserAPIView.as_view()),
]