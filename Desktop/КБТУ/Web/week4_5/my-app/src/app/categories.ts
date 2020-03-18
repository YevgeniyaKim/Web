export interface Category {
  id: number;
  name: string;
  imagesLinks: string;
  productlist: number[];
}

export const categories: Category[] = [
  {
    id: 1,
    name: 'Cosmetics',
    imagesLinks: '//ae01.alicdn.com/kf/HTB1lU_jaEY1gK0jSZFMq6yWcVXa3/Multifunction-travel-Cosmetic-Bag-Neceser-Women-' +
      'Makeup-Bags-Toiletries-Organizer-Waterproof-Female-Storage-Make-up-Cases.jpg_220x220xz.jpg',
    productlist: [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
  },
  {
    id: 2,
    name: 'Bags',
    imagesLinks: 'https://ae01.alicdn.com/kf/HTB18Qe_KhnaK1RjSZFtq6zC2VXao/Cartera-Mujer-Monedero.jpg',
    productlist: [15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
  },
  {
    id: 3,
    name: 'Accessories',
    imagesLinks: 'https://ae01.alicdn.com/kf/H6a356d154b694598935d7525bc68c9fcc/-.jpg',
    productlist: [25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
  },
  {
    id: 4,
    name: 'Clothes',
    imagesLinks: 'https://ae01.alicdn.com/kf/HTB1HYORbcTxK1Rjy0Fgq6yovpXao/-.jpg_640x640.jpg',
    productlist: [35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
  }
];
