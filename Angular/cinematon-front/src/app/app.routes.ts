import { Routes } from '@angular/router';
import { Home } from './pages/home/home';
import { Ticket } from './pages/ticket/ticket';
import { Profile } from './pages/profile/profile';
import { register } from './pages/register/register.component';
import { LoginApp } from './login-app/login-app';
import { HallComponent } from './hall-component/hall-component';

export const routes: Routes = [
  { 
    path: '', 
    component: Home },
  { 
    path: 'ticket/:id', 
    component: Ticket,
    children: [
      {
      path: 'hall/:id',
      component: HallComponent,
      }
    ]
  },
  { 
    path: 'profile', 
    component: Profile },
  { 
    path: 'register', 
    component: register},
  { 
    path: 'login', 
    component: LoginApp}
];
