const { response } = require('express');
var express = require('express');
var router = express.Router();
const request = require('request')

/* GET users listing. */
router.get('/', function(req, res, next) {
  var param = {'value': 'This is Sample'}
  res.header = ('Content-Type', 'application/json; charset=utf-8')
  res.send(param)
});

// PUI数を加算する
let puiCount = 0
router.post('/', (req, res, next) => {

  // countLimit回ごとにWebAPIに送信する
  const countLimit = 10

  // カウント加算
  puiCount++
  console.log(puiCount)
  if(puiCount === countLimit){
    // APIに送信
    console.log("送信")

    // リクエストを送信時のオプション
    const reqOpt = {
      method: 'POST',
      json: 'true',
      url: 'https://example.com',
      body: JSON.stringify({data: 'value'}),
      headers: {
        'Content-Type': 'application/json'
      }
    }

    // リクエスト送信
    request(reqOpt, (error, response) => {
      console.log('送信したよ')
      console.log(error, response.body)
    })
    puiCount = 0
  }

  // console.log(req.body);
  res.send({'res':'OK'})
});

module.exports = router;
