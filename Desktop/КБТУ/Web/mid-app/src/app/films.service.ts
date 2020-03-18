import { Injectable } from '@angular/core';
import {Film, films} from './films';
import { Observable, of } from 'rxjs';
import {Description} from './description';


@Injectable({
  providedIn: 'root'
})
export class FilmsService {
  films = films;
  constructor() { }

  public getDescriptionByFilmId(filmId): Observable<Description> {
    return of(films.find(f => f.id === filmId));
  }
}
