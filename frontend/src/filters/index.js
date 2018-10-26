import moment from 'moment'

export function truncate (value, maxLength) {
  if (typeof value === 'string') {
    if (value.length > maxLength && value.length > 3) {
      return value.substring(0, maxLength - 3) + '...'
    }
  }
  return value
}

export function datetimeFromString (value, format) {
  return moment(value).format(format)
}
