var add_questions=function () {
   var post_data={
       project:$("#project").children("option:selected").text(),
       question_module:$("#module").children("option:selected").text(),
       question_desc:$("#question_desc").val(),
       question_reason:$("#question_reason").val(),
       question_reporter:$("#question_reporter").val(),
       question_answer:$("#question_answer").val(),
       question_progress:$("#question_progress").children("option:selected").text(),
       question_comments:$("#question_comments").val()
   }

   post_json_data(questionsAdd,post_data)
}

var update_question=function (id) {
     var post_data={
       project:$("#project").children("option:selected").text(),
       question_module:$("#module").children("option:selected").text(),
       question_desc:$("#question_desc").val(),
       question_reason:$("#question_reason").val(),
       question_reporter:$("#question_reporter").val(),
       question_answer:$("#question_answer").val(),
       question_progress:$("#question_progress").children("option:selected").text(),
       question_comments:$("#question_comments").val(),
       question_reason:$("#question_reason").val(),
       is_system_cause:$("#is_system_cause").children("option:selected").text(),
       id:id
   }

   post_json_data(questionsEdit,post_data)
}

var skip_to_questions_detail=function (id) {
     window.location.href=questionsDetail+"/"+id+"/"
}

var serach_questions=function () {
    var project_name=$("#project_search").children("option:selected").val()
    var    module_name=$("#module_search").children("option:selected").val()
    var    progress_name=$("#progress_search").children("option:selected").val()
    var    start_time=$("#start_time_search").val()
    var    end_time=$("#end_time_search").val()


    window.location.href=questionsList+"?project_name="+project_name+"&module_name="+module_name+"&progress_name="+progress_name+"&start_time="+start_time+"&end_time="+end_time;

}

var serach_questions_by_modle_name=function (module_name,now_week) {
    var href=questionsListByModuleName+"?now_week="+now_week
    if (module_name != "总数")
        href += "&module_name="+module_name
    window.location.href=href
}