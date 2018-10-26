'use strict'

const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  API_ROOT: process.env.API_ROOT || '"http://127.0.0.1:8000/api/"',
  DEBUG_MODE: true
})
