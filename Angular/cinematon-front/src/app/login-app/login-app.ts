import { Component, inject} from '@angular/core';
import { NgModel } from '@angular/forms';
import { Httpserf } from '../httpserf';

@Component({
  selector: 'app-login-app',
  imports: [NgModel],
  templateUrl: './login-app.html',
  styleUrl: './login-app.css',
})
export class LoginApp {
     http = inject(Httpserf)

     LogIn() {

     }

}
