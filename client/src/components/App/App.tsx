import React from 'react'
// @ts-ignore
import { useDispatch } from 'react-redux'

import { request } from 'store/modules/user'

const App: React.FC = () => {
  const dispatch = useDispatch()

  dispatch(request())

  return <div>hello</div>
}

export default App
