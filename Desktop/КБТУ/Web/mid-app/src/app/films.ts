export interface Film {
  id: number;
  title: string;
  description: string;
  view_count: 0;
}

export const films: Film[] = [
  {
    id: 1,
    title: 'Мстители',
    description: 'Танос: /щелчок пальцами/',
    view_count: 0
  },
  {
    id: 2,
    title: 'Черная Пантера',
    description: 'Этот фильм не о кошках',
    view_count: 0
  },
  {
    id: 3,
    title: 'Армагеддон',
    description: 'Брюс Уиллис спасает мир',
    view_count: 0
  },
  {
    id: 4,
    title: 'В метре друг от друга',
    description: 'Истерика тебе обеспечена',
    view_count: 0
  }
];
