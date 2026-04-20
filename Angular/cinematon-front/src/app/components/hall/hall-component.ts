import { Component } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { Httpserf } from '../../httpserf';

@Component({
  selector: 'app-hall',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './hall.html',
  styleUrl: './hall.css',
})
export class HallComponent {
  constructor(
    private route: ActivatedRoute,
    private api: Httpserf,
  ) {}

  filmId!: number;
  sessions: any[] = [];
  selectedSession: any;
  selectedSeat: string | null = null;

  ngOnInit() {
    this.filmId = this.route.snapshot.params['id'];

    this.api.getSessions(this.filmId).subscribe((data) => (this.sessions = data));
  }

  selectSeat(seat: string) {
    this.selectedSeat = seat;
  }
}
