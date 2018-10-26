import Vue from 'vue'
import VueAxios from 'vue-axios'
import VueAuth from '@websanova/vue-auth'
import { sync } from 'vuex-router-sync'
import ElementUI from 'element-ui'
import { DataTables, DataTablesServer } from 'vue-data-tables'
import 'element-ui/lib/theme-chalk/index.css'
import 'element-ui/lib/theme-chalk/display.css'
import lang from 'element-ui/lib/locale/lang/en'
import locale from 'element-ui/lib/locale'
import App from './App.vue'
import axios from './axios'
import router from './router'
import store from './store'
import * as filters from './filters'
import Logging from './plugins/logging'
import vueAuthConfig from './vue-auth'
import lodash from 'lodash'
import VueLodash from 'vue-lodash/dist/vue-lodash.min'

locale.use(lang)

Vue.router = router
Vue.use(VueAxios, axios)
Vue.use(VueLodash, lodash)
Vue.use(VueAuth, vueAuthConfig)
Vue.use(ElementUI)
Vue.use(DataTables)
Vue.use(DataTablesServer)
Vue.use(Logging)

sync(store, router)

Vue.config.debug = process.env.DEBUG_MODE
Vue.config.devtools = process.env.DEBUG_MODE

Object.keys(filters).forEach(key => {
  Vue.filter(key, filters[key])
})

const app = new Vue({
  router,
  store,
  ...App
})

export { app, router, store }
