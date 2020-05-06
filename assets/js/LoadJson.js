function LoadJsonWrite() 
{
    document.write("<br><br>");
    var mydata = JSON.parse(data);
    for (var i = 0; i < mydata.length; i++) {
        if (mydata[i].c == "" && mydata[i].p == "") continue
        document.write(
            '<div class="route_card">\
		     <div class="route_card_top">'+
            mydata[i].y + '.' + mydata[i].m + '.' + mydata[i].d +
            '</div>' +
            '<div class="route_card_content">' +
            mydata[i].c +
            '</div>' +
            '<div class="route_card_bottom"></div>\
             </div>'
        );
    }
}

function LoadJsonFrame()
{
    window.onload = function () {   
        var nav = window.frames["nav"].document.getElementsByClassName('topmeau')[0].innerHTML;
        var topmeau = document.getElementsByClassName('topmeau')[0];
        topmeau.innerHTML = nav;
      }
}