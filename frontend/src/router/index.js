import Vue from 'vue'
import Router from 'vue-router'

// import Layout from '../components/Layout'
import Login from '../views/auth/Login'
import Goods from '../views/retail/Goods'
import Purchases from '../views/retail/Purchases'
import ResetPassword from '../views/auth/ResetPassword'
import Dashboard from '../views/dashboard/Dashboard'

Vue.use(Router)

export default new Router({
  mode: 'history',
  linkActiveClass: 'is-active',
  scrollBehavior: () => ({ y: 0 }),
  routes: [
    {
      path: '/',
      name: 'dashboard',
      component: Dashboard,
      hidden: false,
      meta: {auth: true}
    },
    {
      path: '/purchases',
      name: 'purchases',
      component: Purchases,
      hidden: false,
      meta: {auth: true}
    },
    {
      path: '/goods',
      name: 'goods',
      component: Goods,
      hidden: false,
      meta: {auth: true}
    },
    {
      name: 'login',
      path: '/login',
      component: Login,
      meta: {auth: false}
    },
    {
      name: 'reset-password',
      path: '/reset-password',
      component: ResetPassword,
      meta: {auth: true}
    }
  ]
})
