import { ThunkAction, ThunkDispatch } from 'redux-thunk'

import { User } from 'types'

import { getUser } from './requests'
import { convertRawUser } from './libs'
import { Action, ActionTypes } from './types'

function _request(): Action {
  return {
    type: ActionTypes.request,
  }
}

function success(user: User): Action {
  return {
    type: ActionTypes.success,
    payload: user,
  }
}

export function request(): ThunkAction<Promise<void>, {}, {}, Action> {
  return async (dispatch: ThunkDispatch<{}, {}, Action>) => {
    dispatch(_request())

    const response = await getUser()
    const user = convertRawUser(response.data[0])

    dispatch(success(user))
  }
}
