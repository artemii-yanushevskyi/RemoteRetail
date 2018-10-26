import ax from 'axios'

const axios = ax.create({
  baseURL: process.env.API_ROOT,
  timeout: 15000,
  headers: {}
})

export default axios
