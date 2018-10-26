let Logging = {}

Logging.install = function (Vue, options) {
  Vue.mixin({
    created: function () {}
  })
  Vue.prototype.$log = function (message, level = 'info') {
    console.log(message)
  }
}

export default Logging
