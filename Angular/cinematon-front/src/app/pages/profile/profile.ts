import { Component, inject, computed } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';
import { CommonModule } from '@angular/common';
import { User } from '../../models/User.model';
import { Httpserf } from '../../httpserf';

@Component({
  selector: 'app-profile',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './profile.html',
  styleUrl: './profile.css',
})
export class Profile {
  http = inject(Httpserf);
  user = toSignal(this.http.loadUser());

  tickets = toSignal(this.http.getMyTickets());
  sessions = toSignal(this.http.getSessions());
  halls = toSignal(this.http.getHalls());
  cinemas = toSignal(this.http.getCinemas());
  films = toSignal(this.http.getFilms())

  normalTickets = computed(() => {
       const tickets = this.tickets()
       const sessions = this.sessions()
       const halls = this.halls()
       const cinemas = this.cinemas()
       const films = this.films()

       if (!tickets || !halls|| !sessions || !cinemas) return []

       return tickets.map(ticket => {
        const session = sessions.find(s => s.session_id === ticket.session);
        const hall = halls.find(h => h.hall_id === session?.hall); 
        const cinema = cinemas.find(c => c.cinemas_id === hall?.cinema);
        const film = films?.find(f => f.film_id === session?.film)

        return {
          ...ticket,
          cinema: cinema?.name,
          hall: hall?.hall_id,
          session_time: session?.start_time,
          film: film?.title
        }
       } 
      )
       }
  )
  
}
