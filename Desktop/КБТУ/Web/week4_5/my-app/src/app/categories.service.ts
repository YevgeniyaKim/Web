import { Injectable } from '@angular/core';
import { categories } from './categories';
import { Observable, of } from 'rxjs';
import {Product, products} from './products';


@Injectable({
  providedIn: 'root'
})

export class CategoriesService {
  categories = categories;
  constructor() { }

  public getProductsByCategoryId(categoryId: number): Observable<Product[]> {
    return of(products.filter(prd => this.categories.find(c => c.id === categoryId).productlist.includes(prd.id)));
  }
}
