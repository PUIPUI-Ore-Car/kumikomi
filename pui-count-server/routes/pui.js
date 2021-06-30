var express = require('express');
var router = express.Router();
const fs = require("fs")

/* GET users listing. */
router.get('/', function(req, res, next) {
  var param = {'value': 'This is Sample'}
  res.header = ('Content-Type', 'application/json; charset=utf-8')
  res.send(param)
});

// PUI数を加算する
router.post('/', (req, res, next) => {
  console.log(req.body);
  res.send({'res':'OK'})
});

module.exports = router;
