import Vue from 'vue'
import Vuex from 'vuex'

import users from './modules/users'
import retail from './modules/retail'

Vue.use(Vuex)

const store = new Vuex.Store({
  strict: true,
  modules: {
    users,
    retail
  }
})

export default store
