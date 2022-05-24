function Email_check_login(){
    var letternumber = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    var email=$("#user_name_login").val();
    if(email.length == '' || email.length == null) {
        $("#user_name_login").removeClass("has-success");
        $("#user_name_login").addClass("has-error");
        $("#email_label_edit_login").text("This Field is required");
        return false;
    }
        else{
            $("#user_name_login").addClass("has-success");
            $("#email_label_edit_login").text("");
            return true;
        }
    }

$("#user_name_login").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})




///////////////

$(document).on('submit', '#forgotSubmit', function(){
    if(Email_check_login() == true){
        return true ;
    }
    else{
        Email_check_login();
        return false ;
    }
})
