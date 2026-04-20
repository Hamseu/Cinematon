import { Component, signal } from '@angular/core';
import { Httpserf } from './httpserf';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, RouterLink, RouterLinkActive],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('cinematon-front');
  user = signal<any>(null);

  constructor(private http: Httpserf) {
    this.loadUser();
  }

  loadUser() {
    this.http.loadUser().subscribe({
      next: (res) => this.user.set(res),
      error: () => this.user.set(null)
    });
  }
  logoutF(){
     this.http.logout().subscribe(() => {
    this.user.set(null);
  });
  }
}
