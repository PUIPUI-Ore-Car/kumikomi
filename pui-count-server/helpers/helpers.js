const ip = require('ip')
const wifiName = require('wifi-name')
require('date-utils')

// IPアドレスの取得
exports.getIPaddr = () => {
    return ip.address()
}

// SSIDの取得
exports.getSSID = () => {
    return wifiName.sync()
}

exports.getTime = () => {
    const dt = new Date()
    const formatted = dt.toFormat('YYYY-MM-DD HH24:MI:SS')
    return formatted
}