import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {ProductListComponent} from './product-list/product-list.component';
import {HeaderComponent} from './header/header.component';
import {Route, RouterModule} from '@angular/router';
import {CategoriesComponent} from './categories/categories.component';

const routes: Route[] = [
  {path: 'categories', component: CategoriesComponent},
  {path: '', redirectTo: '/categories', pathMatch: 'full'},
  {path: 'categories/:categoryId/products', component: ProductListComponent}
];


@NgModule({
  declarations: [
    AppComponent,
    ProductListComponent,
    HeaderComponent,
    CategoriesComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule.forRoot(routes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
