var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  // res.send('respond with a resource');

  var param = {'value': 'This is Sample'}
  res.header = ('Content-Type', 'application/json; charset=utf-8')
  res.send(param)
});

module.exports = router;
