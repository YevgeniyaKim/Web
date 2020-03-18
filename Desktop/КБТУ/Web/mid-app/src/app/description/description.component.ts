import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {Film, films} from '../films';
import {FilmsService} from '../films.service';
import {Description} from '../description';

@Component({
  selector: 'app-description',
  templateUrl: './description.component.html',
  styleUrls: ['./description.component.css']
})
export class DescriptionComponent implements OnInit {
  description: Description;

  constructor(
    public filmsService: FilmsService,
    public route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getDescription();
  }

  public getDescription() {
    const id = +this.route.snapshot.paramMap.get('filmId');
    this.filmsService.getDescriptionByFilmId(id).subscribe(description => this.description = description);
  }
}
