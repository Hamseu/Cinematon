import { Component, inject, signal, computed } from '@angular/core';
import { ActivatedRoute, Router, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { Httpserf } from '../httpserf';
import { toSignal } from '@angular/core/rxjs-interop';
import { catchError, of } from 'rxjs';
import { Ticket } from '../models/Ticket.model';
import { App } from '../app';
import { Hall } from '../models/Hall.model';
import { map, switchMap } from 'rxjs';

@Component({
  selector: 'app-hall',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './hall-component.html',
  styleUrl: './hall-component.css',
})
export class HallComponent {
  route = inject(ActivatedRoute);
  http = inject(Httpserf);
  router = inject(Router);

  private params = toSignal(this.route.paramMap);

  hallId = computed(() => {
  const p = this.params();
  return Number(p?.get('id'));
});

sessionId = computed(() => {
  const p = this.params();
  return Number(p?.get('sessionId'));
});


  errorer = signal<String>("");
  roo = inject(App);
  selectedSeats = signal<Set<string>>(new Set());
  tickets = signal<Ticket[]>([]);
  hall = toSignal(
  this.route.paramMap.pipe(
    map(params => Number(params.get('id'))),
    switchMap(id => this.http.getHall(id))
  ),
  { initialValue: null }
);
 
 
  
rows = computed(() => {
  const h = this.hall();
  return Array.from({ length: Number(h?.rows_number ?? 0) }, (_, i) => i);
});

seats = computed(() => {
  const h = this.hall();
  return Array.from({ length: Number(h?.seats_for_row ?? 0) }, (_, i) => i);
});


bookedSeats = toSignal(
  this.route.paramMap.pipe(
    map(params => Number(params.get('sessionId'))),
    switchMap(sessionId => this.http.getTicketsBySession(sessionId))
  ),
  { initialValue: [] }
);

bookedSeatSet = computed(() => {
  const tickets = this.bookedSeats();

  return new Set(
    tickets.map(t => `${t.row - 1}-${t.seat - 1}`)
  );
});

  selectSeat(row: number, seat: number) {
    row += 1;
    seat +=1;
  const userId = this.roo.user().id;

  const exists = this.tickets().some(
    t => t.row === row && t.seat === seat
  );

  if(exists) return;

  const key = `${row - 1}-${seat - 1}`;

   if (this.bookedSeatSet().has(key)) return;

  const updated = new Set(this.selectedSeats());

  if (updated.has(key)) {
    updated.delete(key);
  } else {
    updated.add(key);
  }

  this.selectedSeats.set(updated);

  const newTicket: Ticket = {
    ticket_id: Number(`${userId}${this.sessionId()}${row}${seat}`),
    user: userId,
    session: this.sessionId(),
    seat,
    row,
    payment: 0
  };

  this.tickets.update(t => [...t, newTicket]);
}

reloadHall(){
  const currentUrl = this.router.url;
  this.router.navigateByUrl('/', {skipLocationChange: true}).then (() => {this.router.navigate([currentUrl]);});
}
 buyTicket() {
  for (let ticket of this.tickets()) {
    this.http.createTicket(ticket).subscribe({
      next: () => {
        
        this.selectedSeats.set(new Set());

      },
      error: (err) => alert("Failed"+ err)
    });
    
  }
  alert("Thank you for purschase!");
    this.reloadHall();

  this.tickets.set([]);
}
}