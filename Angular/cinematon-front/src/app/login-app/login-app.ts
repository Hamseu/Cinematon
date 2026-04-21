import { Component, inject, signal} from '@angular/core';
import { Router, RouterLink } from '@angular/router'; 
import { FormsModule } from '@angular/forms';
import { Httpserf } from '../httpserf';
import { App } from '../app';

@Component({
  selector: 'app-login-app',
  imports: [FormsModule, RouterLink],
  templateUrl: './login-app.html',
  styleUrl: './login-app.css',
})
export class LoginApp {
     http = inject(Httpserf);
     username = signal<string>("");
     password = signal<string>("");
     router = inject(Router);
     app = inject(App);

     LogIn() {
        this.http.login(
          {
            "username": this.username(),
            "password": this.password()
          }
        ).subscribe((res: any) => {
             if (res.error) {
   
              alert("Login failed:" + res.error);
              return;
             } 
             alert("Success:" + res.message);
             this.app.loadUser();

             setTimeout(() => {
             this.router.navigate(['']);}, 1500);
        })
      }

}
