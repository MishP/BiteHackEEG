/*
var io = require('socket.io')(80);
var cfg = require('./config.json');
var tw = require('node-tweet-stream')(cfg);
tw.track('socket.io');
tw.track('javascript');
tw.on('tweet', function(tweet){
  io.emit('tweet', tweet);
});
*/




$('.hidden').hide();

$('.hidden-teaser').click(function(){
	var id = $(this).data('target');
	$('#'+id).toggle(1000);
	$(this).toggleClass('open');
});