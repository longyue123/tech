var post_json_data=function(url,data) {
    $("#load").show();
    $.ajax({
        type:"POST",
        url: url,
        contentType : "application/json",
        data:  JSON.stringify(data),
        complete:function(msg) {
            $("#load").hide();
            response_text=msg.responseText
            alert(JSON.stringify(response_text));
        }

    })
}
