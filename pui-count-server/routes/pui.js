var express = require('express');
var router = express.Router();

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
    puiCount = 0
  }

  // console.log(req.body);
  res.send({'res':'OK'})
});

module.exports = router;
