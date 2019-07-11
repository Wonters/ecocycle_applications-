function pie(ctx, w, h)
{
  var radius = h/2;
  var centerx = w / 2;
  var centery = h / 2;
  var lastend = 0;

  var offset = Math.PI / 2;
  var labelxy = new Array();

  var fontSize = Math.floor(canvas.height / 33);
  ctx.textAlign = 'center';
  ctx.font = fontSize + "px Arial";
  var total = 0;
  for(x=0; x < datalist.length; x++) { total += datalist[x]; };

  for(x=0; x < datalist.length; x++)
  {
    var thispart = datalist[x];
    ctx.beginPath();
    ctx.fillStyle = colist[x];
    ctx.moveTo(centerx,centery);
    var arcsector = Math.PI * (2 * thispart / total);
    ctx.arc(centerx, centery, radius, lastend - offset, lastend + arcsector - offset, false);
    ctx.lineTo(centerx, centery);
    ctx.fill();
    ctx.closePath();
    if(thispart > (total / 20))
       labelxy.push(lastend + arcsector / 2 + Math.PI + offset);
    lastend += arcsector;
  }

  var lradius = radius * 3 / 4;
  ctx.strokeStyle = "rgb(0,0,0)";
  ctx.fillStyle = "rgb(0,0,0)";
  for(i=0; i < labelxy.length; i++)
  {
    var langle = labelxy[i];
    var dx = centerx + lradius * Math.cos(langle);
    var dy = centery + lradius * Math.sin(langle);
    ctx.fillText(datalist[i], dx, dy);
  }
}

function getWeidthLegum() {
    let list = {list};
}


var datalist= new Array(35, 25, 20, 12, 7, 1);
var colist = new Array('blue', 'red', 'green', 'orange', 'gray', 'yellow');
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext('2d');
pie(ctx, canvas.width, canvas.height);
