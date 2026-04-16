import { Component } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-ticket',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './ticket.html'
})
export class TicketComponent {

  filmId!: number;

  constructor(private route: ActivatedRoute) {
    this.filmId = Number(this.route.snapshot.paramMap.get('id'));
  }

  buyTicket() {
    alert('Ticket successfully purchased!');
  }
}