import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  private _registerForm: FormGroup;
  constructor(private _form: FormBuilder) { 
    this.createForm();
  }

  ngOnInit() {
  }
createForm() {
  this._registerForm = this._form.group({
    username: new FormControl,
    email: new FormControl,
    password: new FormControl,
    confirmPassword: new FormControl
  });
}

onSubmit() {
  console.log(this._registerForm.value);
}
}
