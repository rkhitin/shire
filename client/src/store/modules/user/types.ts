import { User } from 'types'

export enum ActionTypes {
  request = '@user/get',
  success = '@user/success',
  failure = '@user/failure',
}

interface Request {
  type: typeof ActionTypes.request
}

interface Success {
  type: typeof ActionTypes.success
  payload: User
}

interface Failure {
  type: typeof ActionTypes.failure
  payload: Error
}

export type Action = Request | Success | Failure

export interface UserState {
  user: User | null
  error: Error | null
  loading: boolean
}
