var express = require('express');
var router = express.Router();
const request = require('request')
const helpers = require('../helpers/helpers')
const childProcess = require('child_process');
const { json } = require('express');

// 送信先URL
const sendURL = 'http://140.227.239.47/'
// const sendURL = 'http://localhost/'

// 温湿度
let temperature = 25
let humidity = 0

let sendJson = {
  puiCount: -1,
  temperature: -1,
  humidity: -1,
  ipAddr: 'null',
  ssid: 'null',
  time: 'null'
}

// データを取得する
router.get('/getData', function(req, res, next) {
  res.header = ('Content-Type', 'application/json; charset=utf-8')
  res.send(sendJson)
});

// PUI数を加算する
let puiCount = 0
router.post('/', (req, res, next) => {

  // カウント加算
  puiCount++
  sendJson.puiCount = puiCount

  res.send({'res':'success'})
});

// 温湿度を受信する
let reqCount = 0
router.post('/temperature', (req, res, next) => {
  const body = req.body

  // 5回ごとに送信
  const reqCountLimit = 5
  reqCount++

  // 受信したデータを反映
  temperature = body.temperature
  humidity = body.humidity
  sendJson.temperature = temperature
  sendJson.humidity = humidity

  console.log(reqCount)
  console.log(body)

  if(reqCount === reqCountLimit){
    // APIに送信
    console.log("送信")

    // 送信するJSON(PUI数, 温度, 湿度, IPアドレス, SSID, 現在時刻)
    sendJson = {
      puiCount: puiCount,
      temperature: temperature,
      humidity: humidity,
      ipAddr: helpers.getIPaddr(),
      ssid: helpers.getSSID(),
      time: helpers.getTime()
    }

    console.log(sendJson)

    // curl送信するコマンド
    const command = 'curl -X POST -H "Content-Type: application/json" -d \'' + JSON.stringify(sendJson) + '\' ' + sendURL

    // コマンド実行
    childProcess.execSync(command)

    // リセット処理
    puiCount = 0
    reqCount = 0
  }

  res.send({'res': 'success'})
})

module.exports = router;
