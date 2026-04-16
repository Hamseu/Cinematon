import { Component } from '@angular/core';
import { Film } from '../../models/Film.model';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { MovieCardComponent } from '../../components/movie-card/movie-card';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, RouterModule, MovieCardComponent],
  templateUrl: './home.html',
  styleUrl: './home.css',
})
export class Home {
  films: Film[] = [
    {
      id: 1,
      title: 'Interstellar',
      genre: 'Sci-Fi',
      description: 'Space travel and black holes',
      release_year: 2014,
      length: 169,
    },
    {
      id: 2,
      title: 'Batman',
      genre: 'Action',
      description: 'Dark knight story',
      release_year: 2022,
      length: 140,
    },
  ];
}
