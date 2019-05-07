import { ActionTypes, Action, UserState } from './types'

const initState: UserState = {
  user: null,
  error: null,
  loading: true,
}

export function reducer(state: UserState = initState, action: Action) {
  switch (action.type) {
    case ActionTypes.request:
      return { ...state, loading: true }

    case ActionTypes.success:
      return { ...state, user: action.payload, loading: false }

    case ActionTypes.failure:
      return { ...state, error: action.payload, loading: false }

    default:
      return state
  }
}
