function CreditCardNumber(){
    var email=$("#creditcardnumber_number").val();
    var length = document.getElementById("creditcardnumber_number").value.length
    if (length == 4){
        $("#creditcardnumber_number").val($("#creditcardnumber_number").val() + " ");
    }
    if (length == 9){
        $("#creditcardnumber_number").val($("#creditcardnumber_number").val() + " ");
    }
    if (length == 14){
        $("#creditcardnumber_number").val($("#creditcardnumber_number").val() + " ");
    }
    if(email.length == '' || email.length == null) {
        $("#creditcardnumber_number").addClass("has-error");
        return false;
    }
    else{
        if(email.length > 19 || password.length < 19){
            $("#creditcardnumber_number").addClass("has-error");
            return false;
            }
        else{
            $("#creditcardnumber_number").removeClass("has-error");
            return true;
            }
        
        }
    }

$("#creditcardnumber_number").focusout(function () {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");

})

///////////

function ExpiaryDateCheck(){
    var email=$("#checkexpiry").val();
    var length = document.getElementById("checkexpiry").value.length
    if (length == 2){
        $("#checkexpiry").val($("#checkexpiry").val() + "/");
    }

    if(email.length == '' || email.length == null) {
        $("#checkexpiry").addClass("has-error");
        return false;
    }

    else{
        if(email.length > 5 || password.length < 5){
            $("#checkexpiry").addClass("has-error");
            return false;
            }
        else{
            $("#checkexpiry").removeClass("has-error");
            return true;
            }
        }
    }

$("#checkexpiry").focusout(function () {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    })


////////////////

function CvvCheck(){
    var email=$("#cardcode").val();
    if(email.length == '' || email.length == null) {
        $("#cardcode").addClass("has-error");
        return false;
    }
    else{
        if(email.length > 3 || password.length < 3){
            $("#cardcode").addClass("has-error");
            return false;
            }
        else{
            $("#cardcode").removeClass("has-error");
            return true;
            }
        }
    }

$("#cardcode").focusout(function () {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    })


////////////



function iCheck_Amount(){
    var email=$("#inveted_Amount").val();
    var letterNumber = /^[+0-9 ]*$/;
    if(email.length == '' || email.length == null) {
        $("#inveted_Amount").addClass("has-error");
        return false;
    }
    else{
        if(email.match(letterNumber)){
            $("#inveted_Amount").removeClass("has-error");
            return true;
        }
        else{
            $("#inveted_Amount").addClass("has-error");
            return false;
        }
    }
}

$("#cardcode").focusout(function () {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    })


//

$(document).on('submit', '#credit_card_form', function(){
    if(CreditCardNumber() && iCheck_Amount() &&
     ExpiaryDateCheck() && CvvCheck() == true){
            return true ;
        }
    else{
        CreditCardNumber();
        ExpiaryDateCheck();
        CvvCheck();
        iCheck_Amount();

        return false ;
    }
})