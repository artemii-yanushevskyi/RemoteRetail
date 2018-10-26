import Vue from 'vue'
import * as types from '../mutation-types'

// import apiClient from '../../api'

const state = {
  goods: [],
  goodsCount: 0,
  purchases: [],
  purchasesCount: 0
}

const mutations = {
  // Goods
  [types.ADD_GOOD] (state, goodData) {
    state.goods.push(goodData)
  },
  [types.UPDATE_GOOD] (state, goodData) {
    let good = state.goods.find(d => d.id === goodData.id)
    let goodIndex = state.goods.indexOf(good)
    Vue.set(state.goods, goodIndex, goodData)
  },
  [types.DELETE_GOOD] (state, id) {
    let good = state.goods.find(d => d.id === id)
    let goodIndex = state.goods.indexOf(good)
    Vue.delete(state.goods, goodIndex)
  },
  [types.FETCH_GOODS] (state, newDomains) {
    state.goods = newDomains
  },
  [types.SET_GOODS_COUNT] (state, goodsCount) {
    state.goodsCount = goodsCount
  },
  // Purchases
  [types.ADD_PURCHASE] (state, purchaseData) {
    state.purchases.push(purchaseData)
  },
  [types.UPDATE_PURCHASE] (state, purchaseData) {
    let purchase = state.purchases.find(d => d.id === purchaseData.id)
    let purchaseIndex = state.purchases.indexOf(purchase)
    Vue.set(state.purchases, purchaseIndex, purchaseData)
  },
  [types.DELETE_PURCHASE] (state, id) {
    let purchase = state.purchases.find(d => d.id === id)
    let purchaseIndex = state.purchases.indexOf(purchase)
    Vue.delete(state.purchases, purchaseIndex)
  },
  [types.FETCH_PURCHASES] (state, newDomains) {
    state.purchases = newDomains
  },
  [types.SET_PURCHASES_COUNT] (state, purchasesCount) {
    state.purchasesCount = purchasesCount
  }
}

const retail = {
  namespaced: false,
  state,
  mutations
}

export default retail
