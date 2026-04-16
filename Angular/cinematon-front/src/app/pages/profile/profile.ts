import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { User } from '../../models/User.model';

@Component({
  selector: 'app-profile',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './profile.html',
  styleUrl: './profile.css',
})
export class Profile {
  user: User = {
    id: 1,
    username: 'user123',
    email: 'user@mail.com'
  };

  // имитация купленных билетов
  tickets = [
    { filmTitle: 'Interstellar', seat: 'A1' },
    { filmTitle: 'Batman', seat: 'B2' }
  ];
}
