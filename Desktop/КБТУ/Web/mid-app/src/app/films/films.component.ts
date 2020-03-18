import { Component, OnInit } from '@angular/core';
import {films} from '../films';

@Component({
  selector: 'app-films',
  templateUrl: './films.component.html',
  styleUrls: ['./films.component.css']
})
export class FilmsComponent implements OnInit {
  films = films;
  constructor() { }

  ngOnInit(): void {
  }

}
