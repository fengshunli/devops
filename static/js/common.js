/**
 * Created by yunan.zhang on 2017/10/12.
 */
$(document).on("click", "button.add_micro_server", function(){
    if(this.dataset.show == 0) {
        $("#add_micro_project_dialog").show();
        this.dataset.show = 1;
    } else {
        $("#add_micro_project_dialog").hide();
        document.getElementById("m_projectName").value = "";
        document.getElementById("m_projectURL").value = "";
        document.getElementById("m_manager").value = "";
        document.getElementById("m_email").value = "";
        this.dataset.show = 0;
    }
});

$(".tpl-left-nav-list a[data-route]").click(function () {
    $("#selection_right_zyndev").load(this.dataset.route);
});

$(document).on("click", "#m_add_micro_server_confirm", function(){
     let m_projectName_obj = $("#m_projectName");
     if(m_projectName_obj.val() == "" || m_projectName_obj.val().length < 4) {
         m_projectName_obj.parent().parent().addClass("am-form-error");
         m_projectName_obj.addClass("am-form-field");
     } else {
         m_projectName_obj.parent().parent().removeClass("am-form-error");
         m_projectName_obj.removeClass("am-form-field");
     }


     let m_projectURL_obj = $("#m_projectURL");
     if(m_projectURL_obj.val() == "" || m_projectURL_obj.val().length < 4) {
         m_projectURL_obj.parent().parent().addClass("am-form-error");
         m_projectURL_obj.addClass("am-form-field");
     } else {
         m_projectURL_obj.parent().parent().removeClass("am-form-error");
         m_projectURL_obj.removeClass("am-form-field");
     }

     let m_manager_obj = $("#m_manager");
     if(m_manager_obj.val() == "" || m_manager_obj.val().length < 4) {
         m_manager_obj.parent().parent().addClass("am-form-error");
         m_manager_obj.addClass("am-form-field");
     } else {
         m_manager_obj.parent().parent().removeClass("am-form-error");
         m_manager_obj.removeClass("am-form-field");
     }

     let m_email_obj = $("#m_email");
     if(m_email_obj.val() == "" || m_email_obj.val().length < 4) {
         m_email_obj.parent().parent().addClass("am-form-error");
         m_email_obj.addClass("am-form-field");
     } else {
         m_email_obj.parent().parent().removeClass("am-form-error");
         m_email_obj.removeClass("am-form-field");
     }

     $.ajax({
         url: "microservice/add",
         data:{
             "csrfmiddlewaretoken": $("input[name='csrfmiddlewaretoken']").val(),
             "projectName": m_projectName_obj.val(),
             "projectURL": m_projectURL_obj.val(),
             "manager": m_manager_obj.val(),
             "email": m_email_obj.val()
         },
         type:'POST',
         success: function (data) {
             if (data.code == 200) {
                 $("button.add_micro_server:first").click();
                 alert("添加成功... 马上进行拉取数据测试");
             } else {
                 alert("添加失败... " + data.msg);
             }
         },
         error: function () {
             alert("添加失败... ");
         }
     })

});
