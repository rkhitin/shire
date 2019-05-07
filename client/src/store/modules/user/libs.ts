import camelcaseKeys from 'camelcase-keys'

import { User } from 'types'

export function convertRawUser(rawUser: any): User {
  const camelcasedRawUser: any = camelcaseKeys(rawUser, { deep: true })

  return {
    username: rawUser.user.username,
    settings: camelcasedRawUser.settings,
  }
}
