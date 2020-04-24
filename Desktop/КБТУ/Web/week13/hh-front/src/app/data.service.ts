import { Injectable } from '@angular/core';
import {Company, LoginResponse} from './models';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  link = 'http://127.0.0.1:8000';
  constructor(private http: HttpClient) {}

  getCompanies(): Observable<Company[]> {
    return this.http.get<Company[]>(this.link + '/api/companies/');
  }

  getCompany(id): Observable<Company> {
    return this.http.get<Company>(this.link + '/api/companies/' + id);
  }

  login(username, password): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(this.link + '/api/login/', {
      username,
      password
    });
  }
}
