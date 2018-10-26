import Vue from 'vue'
import * as types from '../mutation-types'

import apiClient from '../../api'

const state = {
  users: []
}

const mutations = {
  [types.ADD_USER] (state, userData) {
    state.users.push(userData)
  },
  [types.UPDATE_USER] (state, userData) {
    let user = state.users.find(u => u.id === userData.id)
    let userIndex = state.users.indexOf(user)
    Vue.set(state.users, userIndex, userData)
  },
  [types.DELETE_USER] (state, id) {
    let user = state.users.find(u => u.id === id)
    let userIndex = state.users.indexOf(user)
    Vue.delete(state.users, userIndex)
  },
  [types.FETCH_USERS] (state, newUsers) {
    state.users = newUsers
  }
}

const actions = {
  addUser ({commit, state}, {userData, params = null}) {
    let promise = apiClient.addUser(userData, params)
    promise.then(function (response) {
      commit(types.ADD_USER, response.data)
    })
    .catch(function (error) {
      console.log(error)
    })
    return promise
  },
  updateUser ({commit, state}, { userData, params = null }) {
    let promise = apiClient.updateUser(userData.id, userData, params)
    promise.then(function (response) {
      commit(types.UPDATE_USER, response.data)
    })
    .catch(function (error) {
      console.log(error)
    })
    return promise
  },
  deleteUser ({commit, state}, { userId, params = null }) {
    let promise = apiClient.deleteUser(userId, params)
    promise.then(function (response) {
      commit(types.DELETE_USER, userId)
    })
    .catch(function (error) {
      console.log(error)
    })
    return promise
  },
  fetchUsers ({commit}, { params = null }) {
    let promise = apiClient.getUsers(params)
    promise.then(function (response) {
      commit(types.FETCH_USERS, response.data.results)
    })
    .catch(function (error) {
      console.log(error)
    })
    return promise
  }
}

const getters = {
  getUserById: (state, getters) => (id) => {
    return state.users.find(u => u.id === id)
  },
  getUserFullName: (state, getters) => (userId) => {
    let user = getters.getUserById(userId)
    return user ? `${user.first_name} ${user.last_name}` : 'Unknown'
  }
}

const users = {
  namespaced: false,
  state,
  mutations,
  actions,
  getters
}

export default users
