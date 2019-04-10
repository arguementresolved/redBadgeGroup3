
import { Injectable } from '@angular/core';
import { RegisterUser } from '../models/register';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { MyToken } from '../models/token';
import { Router } from '@angular/router';
import { Observable, Subject } from 'rxjs';

const apiUrl = 'http://127.0.0.1:5000';

@Injectable()

export class AuthService {
  userInfo: MyToken;
  isLoggedIn = new Subject<boolean>();


  constructor(private _http: HttpClient, private _router: Router) { }

  register(regUserData: RegisterUser) {
    return this._http.post(`${apiUrl}/api/v1/users`, regUserData);
  }

  login(loginInfo) {
    const str =
      `grant_type=password&username=${encodeURI(loginInfo.email)}&password=${encodeURI(loginInfo.password)}`;

    return this._http.post(`${apiUrl}/api/v1/users/login`, str).subscribe( (token: MyToken) => {
      this.userInfo = token;
      localStorage.setItem('id_token', token.access_token);
      this.isLoggedIn.next(true);
      this._router.navigate(['/']);
    });
  }

  currentUser(): Observable<Object> {
    if (!localStorage.getItem('id_token')) { return new Observable(observer => observer.next(false)); }

    return this._http.get(`${apiUrl}/api/Account/UserInfo`, { headers: this.setHeader() });
  }

  logout() {
    localStorage.clear();
    this.isLoggedIn.next(false);

    this._http.post(`${apiUrl}/api/v1/users/logout`, { headers: this.setHeader() } );
    this._router.navigate(['/login']);
  }

  private setHeader(): HttpHeaders {
    return new HttpHeaders().set('Authorization', `Bearer ${localStorage.getItem('id_token')}`);
  }
}
