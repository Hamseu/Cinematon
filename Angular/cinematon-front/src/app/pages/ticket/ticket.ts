import { Component, inject, computed } from '@angular/core';
import { ActivatedRoute, RouterModule , RouterOutlet, RouterLink, RouterLinkActive} from '@angular/router';
import { CommonModule } from '@angular/common';
import { Httpserf } from '../../httpserf';
import { toSignal } from '@angular/core/rxjs-interop';
import { switchMap } from 'rxjs';

@Component({
  selector: 'app-ticket',
  standalone: true,
  imports: [CommonModule, RouterModule, RouterOutlet, RouterLink, RouterLinkActive],
  templateUrl: './ticket.html'
})
export class Ticket {

  selecting_seat = false;
  http = inject(Httpserf);
  route = inject(ActivatedRoute)
  filmId = Number(this.route.snapshot.paramMap.get('id'));

  film = toSignal(
  this.route.paramMap.pipe(
    switchMap(params =>
      this.http.getFilm(Number(params.get('id')))
    )
  ),
  { initialValue: null }
);

  sessions = toSignal(this.http.getFilmSessions(this.filmId))

  cinemas = toSignal(this.http.getCinemas())

  halls = toSignal(this.http.getHalls()) 
  sessionsWithCinema = computed(() => {
    const sessions = this.sessions()
    const halls = this.halls()
    const cinemas = this.cinemas()

    if (!sessions || !halls || !cinemas) return []

    return sessions.map(session => {
       const hall = halls.find(h => h.hall_id === session.hall)
       const cinema = cinemas.find(c => c.cinemas_id === hall?.cinema)

    return {
       ...session,
       cinema_name: cinema?.name
    }
  })
})


  
  buyTicket() {
    alert('Ticket successfully purchased!');
  }
}