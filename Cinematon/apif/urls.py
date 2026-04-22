from django.urls import path



from .views import (
    HallListAPIView,
    HallDetailAPIView,
    SessionListAPIView,
    TokenRefreshView,
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
    LoginView,
    LogoutView,
    MeAPIView,
    TicketBySessionAPIView
)
urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginView, name='login'),
    path('login/refresh/', TokenRefreshView, name='refresh'),
    path('logout/', LogoutView, name = 'logout'),
    path('me/', MeAPIView.as_view(), name = 'current_user'),

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
    path("sessions/<int:session_id>/tickets/", TicketBySessionAPIView.as_view()),
    ]