export enum PrivacyLevel {
  PR = 'private',
  PB = 'public',
}

interface Category {
  pk: number
  name: string
  color: string
  iconName: string
}

interface Obstacle {
  pk: number
  name: string
}

export interface User {
  username: string
  settings: {
    privacyLevel: PrivacyLevel
  }
}

interface Habbit {
  pk: number
  title: string
  wish: string
  outcome: string
  category: Category
  obstacles: Obstacle[]
}
