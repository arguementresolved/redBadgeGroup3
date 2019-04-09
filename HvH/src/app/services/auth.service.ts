import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

const apiUrl = 'https://kcpelevennote.azurewebsites.net';

@Injectable()
export class AuthService {

  constructor(private _http: HttpClient) { }

  createComment(comment: Comment) {
    return this._http.post(`${apiUrl}/api/Notes`, note, { headers: this.getHeaders()});
  }
}
