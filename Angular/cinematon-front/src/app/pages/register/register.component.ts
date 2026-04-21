import { Component, inject, signal } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { Route, Router, RouterLink } from "@angular/router";
import { CommonModule } from "@angular/common";
import { Httpserf } from "../../httpserf";
import { toSignal } from "@angular/core/rxjs-interop";
@Component({
  selector: 'app-root',
  imports: [FormsModule, CommonModule, RouterLink],
  templateUrl: './register.html',
  styleUrl: './register.css'
})
export class register {
     http = inject(Httpserf)
     username = signal<string>("")
     email = signal<string>("")
     password = signal<string>("")
     route = inject(Router)


     Register(){
      this.http.register({
        "username": this.username(),
        "email": this.email(),
        "password": this.password()
      }).subscribe((res: any) => {
             if (res.error) {
   
              alert("Registration failed:" + res.error);
              return;
             }
             this.route.navigate(['/login']);
        }

      );
     }
}