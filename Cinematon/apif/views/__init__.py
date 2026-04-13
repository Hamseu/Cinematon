from .cbv import (
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
   TicketsByUserAPIView
)

from .fbv import (filmsview as FilmsListView,
                  filmview as FilmDetailView,
                  cinemaview as  CinemaDetailView,
                  cinemasview as CinemasDetailView)

from .generic import RegisterAPIView