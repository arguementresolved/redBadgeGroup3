import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';


const apiUrl = 'http://127.0.0.1:5000/';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor() { }

  createNote(note: Note) {
    return this._http.post(`${apiUrl}/api/Notes`, note, { headers: this.getHeaders()});
  }

}
export class NotesService {

  constructor(private _http: HttpClient) { };