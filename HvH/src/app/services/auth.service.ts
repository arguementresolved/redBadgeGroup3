import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

const apiUrl = 'http://127.0.0.1:5000/';

@Injectable()
export class AuthService {

  constructor(private _http: HttpClient) { }

  createComment(comment: Comment) {
    return this._http.post(`${apiUrl}/comment/new`, comment, { headers: this.getHeaders()});
  }

}
export class NotesService {

  constructor(private _http: HttpClient) { };
