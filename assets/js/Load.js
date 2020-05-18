function LoadFile(filename)
{
    var file = new XMLHttpRequest();
    file.open("GET",filename,false);
    file.send();
    return file.responseText;
}

function LoadJsonWrite(filename) 
{
    document.write("<br><br><br>");
    var mydata = JSON.parse(LoadFile(filename));
    for (var i = 0; i < mydata.length; i++) {
        var pics ="";
        if (mydata[i].p != ""){pics="<img src ="+'https://atarsei.gitee.io/assets/images/'+mydata[i].p.split(',')[0]+"></img>"};
        if (mydata[i].c == "" && mydata[i].p == "") continue
        document.write(
            '<div class="route_card">\
		     <div class="route_card_top">'+
            mydata[i].y + '.' + mydata[i].m + '.' + mydata[i].d +
            '</div>' +
            '<div class="route_card_content">' +
            mydata[i].c +pics+
            '</div>' +
            '<div class="route_card_bottom"></div>\
             </div>'
        );
    }
    
}

function LoadHtmlWrite(filename,classname)
{
    var outside = LoadFile(filename);
    var outside_div =document.createElement('div');
    outside_div.innerHTML =outside;
    outside = outside_div.getElementsByClassName(classname)[0].outerHTML;
    var inside = document.getElementsByClassName(classname)[0];
    inside.outerHTML = outside;
    var web=location.protocol+"//"+location.hostname;
    var childname=["about","article","route","coverpage"];
    document.getElementById("home").href=web;
    for (i in childname)
    {document.getElementById(childname[i]).href=web+"/"+childname[i]};
}
function LoadFrame()/* Out Of Time   <iframe name="nav" src="../assets/Module/nav.html" style="display: none"></iframe>*/
{
    window.onload = function () {   
        var nav = window.frames["nav"].document.getElementsByClassName('topmeau')[0].innerHTML;
        var topmeau = document.getElementsByClassName('topmeau')[0];
        topmeau.innerHTML = nav;
      }
}

function PhotoStatus()
{
    var imgs=document.getElementsByTagName('img');
    imgs[0].onerror=function()
    {   
        for (i in imgs)
        {imgs[i].src=imgs[i].src.replace("gitee","github")}
    }
    imgs[0].onerror=null
}

/* οnerrο */