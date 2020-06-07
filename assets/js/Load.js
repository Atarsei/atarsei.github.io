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
        if (mydata[i].c == "" && mydata[i].p == "") {continue};
/*         var pics ="";
        if (mydata[i].p != ""){pics="<br><img src =\""+'https://atarsei.gitee.io/assets/images/'+mydata[i].p.split(',')[0]+"\"></img>"}; */
        document.write(
            '<div class="route_card">\
		     <div class="route_card_top">'+
            mydata[i].y + '.' + mydata[i].d +
            '</div>' +
            '<div class="route_card_content">' +
            mydata[i].c +pics(mydata,i)+
            '</div>' +
            '<div class="route_card_bottom"></div>\
             </div>'
        );
    }   
}
function pics(mydata,i)/* 附属于上个函数 ，处理图片*/
{
    if (mydata[i].p != "")
    {
        var pics="";
        if (mydata[i].p.split(',').length==1)
        {
            return "<br><img class=\"pic1\" src =\""+'https://atarsei.gitee.io/assets/images/'+mydata[i].p.split(',')[0]+"\"></img>"
        }
        else if(mydata[i].p.split(',').length==2)
        {
            for(var x=0;x<2;x++)
            {
                pics=pics+"<div class=\"pic2\"><img src =\""+'https://atarsei.gitee.io/assets/images/'+mydata[i].p.split(',')[x]+"\"></img></div>"
            }
            return "<br><div class=\"pic2_con\">"+pics+"</div>"
        }
        else
        {
            for(var x=0;x<mydata[i].p.split(',').length;x++)
            {
                pics=pics+"<div class=\"pic9\"><img src =\""+'https://atarsei.gitee.io/assets/images/'+mydata[i].p.split(',')[x]+"\"></img></div>"
            }
            return "<br><div class=\"pic9_con\">"+pics+"</div>"
        }
    }
    else{return ""}
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

function PhotoStatus(tagname='img')
{

    var imgs=document.getElementsByTagName(tagname);  
    for (var i=0;i<imgs.length;i++)
    {
        imgs[i].setAttribute('onerror','PhotoStatusII(this)')
    }
}
function PhotoStatusII(object)
{
    object.src=object.src.replace("https://atarsei.gitee.io","");
    object.onerror=null;
};

function LoadXml(filename)
{
    var file = new XMLHttpRequest();
    file.open("GET",filename,false);
    file.send();
    return file.responseXML;
}
function LoadXmlForPage()
{
    var filename=location.pathname.replace(/.*\//i,"").replace(/\..*/i,"");
    var xml = LoadXml("../index.xml").getElementById(filename);
    function xmlchild(name)
    {return xml.getElementsByTagName(name)[0].innerHTML};
    document.getElementsByClassName("side")[0].innerHTML=xmlchild('label');
}
function LoadXmlForIndex()
{
    var xmls=LoadXml("index.xml").getElementsByTagName("article");
    function xmlchild(name)
    {return xml.getElementsByTagName(name)[0].innerHTML}
    var text='';
    for (var i=0;i<xmls.length;i++)
    {
        var xml=xmls[i];
        text=text+`<a href="/article/page/${xmlchild('title')}.html">${xmlchild('title')}</a><br>`;        
    }
    document.getElementsByClassName('main')[0].innerHTML=text
}