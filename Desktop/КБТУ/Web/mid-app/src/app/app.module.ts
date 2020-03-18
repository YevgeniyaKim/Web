import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FilmsComponent } from './films/films.component';
import { DescriptionComponent } from './description/description.component';
import {Route, RouterModule} from '@angular/router';

const routes: Route[] = [
  {path: 'films', component: FilmsComponent},
  {path: '', redirectTo: '/films', pathMatch: 'full'},
  {path: 'films/:filmId', component: FilmsComponent}
];

@NgModule({
  declarations: [
    AppComponent,
    FilmsComponent,
    DescriptionComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule.forRoot(routes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
