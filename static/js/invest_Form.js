

////////////


/////////////
function Investment_check(){
    var email=$("#investment_amount").val();
    if(email.length == '' || email.length == null) {
        $("#investment_amount").removeClass("has-success");
        $("#investment_amount").addClass("has-error");
        $("#email_label_edit_login").text("This Field is required");
        return false;
    }
        else{
            $("#investment_amount").addClass("has-success");
            $("#email_label_edit_login").text("");
            return true;
        }
    }

$("#investment_amount").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})

/////////


///////////




////////////



$(document).on('submit', '#investment_amount_form', function(){
    if(Investment_check()  == true){
            if ($("#checked_true").prop('checked') == true){
            $("#checked_label").text("");
            return true ;
        }
        else{
            $("#checked_true").removeClass("has-success");
            $("#checked_true").addClass("has-error");
            $("#checked_label").text("This Field is required");
            return false ;
        }
    }
    else{
        Investment_check();
        return false ;
    }
})