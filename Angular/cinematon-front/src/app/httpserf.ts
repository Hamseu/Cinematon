import { Injectable, inject, signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { Film } from './models/Film.model';
import { Cinema } from './models/Cinema.model';
import { Hall } from './models/Hall.model';
import { Session } from './models/Session.model';
import { Ticket } from './models/Ticket.model';
import { User } from './models/User.model';

@Injectable({
  providedIn: 'root',
})
export class Httpserf {
  private http = inject(HttpClient);
  private littleURL = 'http://localhost:8000';



  register(data: any): Observable<User> {
    return this.http.post<User>(`${this.littleURL}/register/`, data);
  }
  loadUser(): Observable<User>{
    return this.http.get<User>(`${this.littleURL}/me/`, {withCredentials: true});
  }

  login(data: any): Observable<any> {
    return this.http.post(`${this.littleURL}/login/`, data, {
      withCredentials: true
    });
  }

  refresh(): Observable<any> {
    return this.http.post(`${this.littleURL}/login/refresh/`, {}, {
      withCredentials: true
    });
  }

  logout(): Observable<any> {
    return this.http.post(`${this.littleURL}/logout/`, {}, {
      withCredentials: true
    });
  }


  getFilms(): Observable<Film[]> {
    return this.http.get<Film[]>(`${this.littleURL}/films/`);
  }

  getFilm(id: number): Observable<Film> {
    return this.http.get<Film>(`${this.littleURL}/films/${id}/`);
  }

  getFilmsByGenre(genre: string): Observable<Film[]> {
    return this.http.get<Film[]>(`${this.littleURL}/films/genre/${genre}/`);
  }

  getFilmSessions(filmId: number): Observable<Session[]> {
    return this.http.get<Session[]>(
      `${this.littleURL}/films/${filmId}/sessions/`
    );
  }


  getCinemas(): Observable<Cinema[]> {
    return this.http.get<Cinema[]>(`${this.littleURL}/cinemas/`);
  }

  getCinema(id: number): Observable<Cinema> {
    return this.http.get<Cinema>(`${this.littleURL}/cinemas/${id}/`);
  }

  getCinemaHalls(cinemaId: number): Observable<Hall[]> {
    return this.http.get<Hall[]>(
      `${this.littleURL}/cinemas/${cinemaId}/halls/`
    );
  }


  getHalls(): Observable<Hall[]> {
    return this.http.get<Hall[]>(`${this.littleURL}/halls/`);
  }

  getHall(id: number): Observable<Hall> {
    return this.http.get<Hall>(`${this.littleURL}/halls/${id}/`);
  }

  getHallSessions(hallId: number): Observable<Session[]> {
    return this.http.get<Session[]>(
      `${this.littleURL}/halls/${hallId}/sessions/`
    );
  }


  getSessions(): Observable<Session[]> {
    return this.http.get<Session[]>(`${this.littleURL}/sessions/`);
  }

  getSession(id: number): Observable<Session> {
    return this.http.get<Session>(`${this.littleURL}/sessions/${id}/`);
  }


  getTickets(): Observable<Ticket[]> {
    return this.http.get<Ticket[]>(`${this.littleURL}/tickets/`, {
      withCredentials: true
    });
  }

  getTicketsBySession(id:number): Observable<Ticket[]> {
    return this.http.get<Ticket[]>(`${this.littleURL}/sessions/${id}/tickets/`, {
      withCredentials: true
    });
  }

  getTicket(id: number): Observable<Ticket> {
    return this.http.get<Ticket>(
      `${this.littleURL}/tickets/${id}/`,
      { withCredentials: true }
    );
  }

  getMyTickets(): Observable<Ticket[]> {
    return this.http.get<Ticket[]>(
      `${this.littleURL}/tickets/my/`,
      { withCredentials: true }
    );
  }

  createTicket(data: any): Observable<Ticket> {
    return this.http.post<Ticket>(
      `${this.littleURL}/tickets/`,
      data,
      { withCredentials: true }
    );
  }

  deleteTicket(id: number): Observable<any> {
    return this.http.delete(
      `${this.littleURL}/tickets/${id}/`,
      { withCredentials: true }
    );
  }
}
