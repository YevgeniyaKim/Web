import {Component, OnInit} from '@angular/core';
import {products, Product} from '../products';
import {CategoriesService} from '../categories.service';
import {ActivatedRoute} from '@angular/router' ;

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent {
  products: Product[];

  constructor(
    public categoriesService: CategoriesService,
    public route: ActivatedRoute
  ) {
  }

  // tslint:disable-next-line:use-lifecycle-interface
  ngOnInit(): void {
    this.getProducts();
  }


  public getProducts() {
    const id = +this.route.snapshot.paramMap.get('categoryId');
    this.categoriesService.getProductsByCategoryId(id).subscribe(prd => this.products = prd);
  }
}
