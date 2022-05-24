


/////////


function Password(){
    var password= $("#psw_customer").val();
    if(password.length == '' || password.length == null) {
        $("#psw_customer").removeClass("has-success");
        $("#psw_customer").addClass("has-error");
        $("#password_label").text("This Field is required");
        return false;
    }
    else{
            $("#psw_customer").addClass("has-success");
            $("#password_label").text("");
            return true;
            }
    }
$("#psw_customer").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})








//////////////
function Otp_check(){
    var legal =$("#otp_field").val();
    var letterNumber = /^[+0-9 ]*$/;
    if(legal.length == '' || legal.length == null) {
        $("#otp_field").removeClass("has-success");
        $("#otp_field").addClass("has-error");
        $("#otp_label_text").text("This Field is required");
        return false;
    }
    else{

        if(legal.length > 4 || legal.length < 4){
            $("#otp_field").removeClass("has-success");
            $("#otp_field").addClass("has-error");
            $("#otp_label_text").text("It contains only 4 numbers");
            return false;
            }
        else{

            if(legal.match(letterNumber)){
                $("#otp_field").addClass("has-success");
                $("#otp_label_text").text("");
                return true;
            }
            else{
                $("#otp_field").removeClass("has-success");
                $("#otp_field").addClass("has-error");
                $("#otp_label_text").text("It contains only numbers");
                return false;
            }

            }
        }

    }

$("#otp_field").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})


///////////
$(document).on('submit', '#forgotSubmit', function() {
    if (Password() && Otp_check()  == true) {
        return true;
    } else {
        Password();
        Otp_check();
        return false;
    }
})
