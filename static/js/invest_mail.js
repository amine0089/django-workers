function Investment_check_Mail(){
    var email=$("#investment_amount_mail").val();
    if(email.length == '' || email.length == null) {
        $("#investment_amount_mail").removeClass("has-success");
        $("#investment_amount_mail").addClass("has-error");
        $("#mail_label_edit_login").text("This Field is required");
        return false;
    }
        else{
            $("#investment_amount_mail").addClass("has-success");
            $("#mail_label_edit_login").text("");
            return true;
        }
    }

$("#investment_amount_mail").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})

/////////

function Investment_mail_question(){
    var letternumber = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    var email=$("#email_check_mail").val();
    if(email.length == '' || email.length == null) {
        $("#email_check_mail").removeClass("has-success");
        $("#email_check_mail").addClass("has-error");
        $("#mail_label_check_label").text("This Field is required");
        return false;
    }
    else{
        if(email.match(letternumber)){
            $("#email_check_mail").addClass("has-success");
            $("#mail_label_check_label").text("");
            return true;
            }
        else{
            $("#email_check_mail").removeClass("has-success");
            $("#email_check_mail").addClass("has-error");
            $("#mail_label_check_label").text("please enter a valid email address");
            return false;
            }
        }
    }

$("#email_check_mail").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})






///////////
$(document).on('submit', '#investoment_question_form', function(){
    if(Investment_mail_question() && Investment_check_Mail() == true){
        return true ;
    }
    else{
        Investment_mail_question();
        Investment_check_Mail();
        return false ;
    }
})