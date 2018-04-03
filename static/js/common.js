
var del_query_variable=function (name) {
    var loca = window.location;
    var baseUrl = loca.origin + loca.pathname + "?";
    var query = loca.search.substr(1);
    if (query.indexOf(name)>-1) {
        var obj = {}
        var arr = query.split("&");
        for (var i = 0; i < arr.length; i++) {
            arr[i] = arr[i].split("=");
            obj[arr[i][0]] = arr[i][1];
        };
        console.log(obj)
        delete obj[name];
        console.log(obj)
        for(var i in obj) {
           baseUrl =baseUrl + i + "=" + obj[i]+"&"
        }
        return baseUrl.substr(0,baseUrl.length-1)
    } else {
        return loca.toString().replace("#","")
    }
}


var get_query_variable=function (name) {
    var query = window.location.search.substring(1);
       var vars = query.split("&");
       for (var i=0;i<vars.length;i++) {
               var pair = vars[i].split("=");
               if(pair[0] == name){return pair[1];}
       }
    return(false);
}

var bind_paginaion=function (type) {
   $("#pagination").find("li").children().each(function () {
        var text=$(this).text();
        if (text == window.page) {
            if (type == 1) {
                $(this).parent().removeAttr("class")
            } else {
                $(this).parent().attr("class","active")
            }
        }
    })
}

$("#pagination").children().children().click(function () {
    bind_paginaion(1)
    $(this).parent().attr("class","active");
    window.page=$(this).text();
    var href=del_query_variable("page")

    if (href.indexOf("&")>-1)
        href=href+"&page="+window.page
    else
        href=href+"?page="+window.page;
    window.location.href=href
})