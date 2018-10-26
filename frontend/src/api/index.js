import axios from 'axios'
import localAxios from '../axios'

function RetailpiClient (config) {
  let self = this
  config = config || {}
  self.authWord = config.authWord || 'Bearer'
  self.token = config.token || null
  // Set http client
  if (!config.axios) {
    self.baseUrl = config.baseUrl
    self.timeout = config.timeout || 10000
    self.headers = config.headers
    self.http = axios.create({
      baseURL: self.baseUrl,
      timeout: self.timeout,
      headers: {}
    })
  } else {
    self.http = config.axios
  }
  self.getRequestConfig = function (params = null, token = null) {
    let config = {}
    if (params) {
      config['params'] = params
    }
    if (token) {
      config['headers'] = {'Authorization': token}
    }
    return config
  }
  // Auth
  self.resetPassword = function (oldPassword, newPassword, params = null, token = null) {
    return self.http.post('/auth/reset-password', {
      old_password: oldPassword, new_password: newPassword
    }, self.getRequestConfig(params, token))
  }
  // users
  self.getUsers = function (params = null, token = null) {
    return self.http.get('users/', self.getRequestConfig(params, token))
  }
  self.addUser = function (userData, params = null, token = null) {
    return self.http.post('users/', userData, self.getRequestConfig(params, token))
  }
  self.updateUser = function (userId, userData, params = null, token = null) {
    return self.http.put(`users/${userId}/`, userData, self.getRequestConfig(params, token))
  }
  self.deleteUser = function (userId, params = null, token = null) {
    return self.http.delete(`users/${userId}/`, self.getRequestConfig(params, token))
  }
  // purchases
  self.getPurchases = function (params = null, token = null) {
    return self.http.get('purchases/', self.getRequestConfig(params, token))
  }
  self.addPurchase = function (purchaseData, params = null, token = null) {
    return self.http.post('purchases/', purchaseData, self.getRequestConfig(params, token))
  }
  self.updatePurchase = function (purchaseId, purchaseData, params = null, token = null) {
    return self.http.put(`purchases/${purchaseId}/`, purchaseData, self.getRequestConfig(params, token))
  }
  self.deletePurchase = function (purchaseId, params = null, token = null) {
    return self.http.delete(`purchases/${purchaseId}/`, self.getRequestConfig(params, token))
  }
  // goods
  self.getGoods = function (params = null, token = null) {
    return self.http.get('goods/', self.getRequestConfig(params, token))
  }
  self.addGood = function (goodData, params = null, token = null) {
    return self.http.post('goods/', goodData, self.getRequestConfig(params, token))
  }
  self.updateGood = function (goodId, goodData, params = null, token = null) {
    return self.http.put(`goods/${goodId}/`, goodData, self.getRequestConfig(params, token))
  }
  self.deleteGood = function (goodId, params = null, token = null) {
    return self.http.delete(`goods/${goodId}/`, self.getRequestConfig(params, token))
  }
}

const client = new RetailpiClient({axios: localAxios})

export default client
