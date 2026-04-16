import { Routes } from '@angular/router';
import { Home } from './pages/home/home';
import { TicketComponent } from './pages/ticket/ticket';
import { Profile } from './pages/profile/profile';

export const routes: Routes = [
  { path: '', component: Home },
  { path: 'ticket/:id', component: TicketComponent },
  { path: 'profile', component: Profile },
];
