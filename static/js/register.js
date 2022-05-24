$(document).on('change', '#entity_Check', function(){
	if ($(this).val() == 'Private_Investor'){
		$("#hide_during_legal_entity").show();
		$("#show_during_both").show();
		$("#show_during_legal_entity").hide();

	}
	else if ($(this).val() == 'Investing_via_entity'){
		$("#hide_during_legal_entity").hide();
		$("#show_during_both").show();
		$("#show_during_legal_entity").show();
	}
	else {
		$("#hide_during_legal_entity").hide();
		$("#show_during_both").hide();
		$("#show_during_legal_entity").hide();

	}
});

////////
$(document).on('change', '#entity_Check', function(){
	if ($(this).val() == 'Please_Select'){
        $("#entity_Check").removeClass("has-success");
        $("#entity_Check").addClass("has-error");
        $("#add_contact_label").text("This Field is required");
        return false ;

	}
	else {
		$("#entity_Check").addClass("has-success");
		$("#add_contact_label").text("");
		return true;
	}
});

/////////////


$(document).on('change', '#entity_type_check', function(){
    if ($(this).val() == 'PleaseSelect'){
        $("#entity_type_check").removeClass("has-success");
        $("#entity_type_check").addClass("has-error");
        $("#typecheck_label_entity").text("This Field is required");
        return false ;

    }
    else {
        $("#entity_type_check").addClass("has-success");
        $("#typecheck_label_entity").text("");
        return true;
    }
});



////////////


function check_entity_type(){
    if ($("#entity_type_check").val() == 'PleaseSelect'){
        $("#entity_type_check").removeClass("has-success");
        $("#entity_type_check").addClass("has-error");
        $("#typecheck_label_entity").text("This Field is required");
        return false ;

    }
    else {
        $("#entity_type_check").addClass("has-success");
        $("#typecheck_label_entity").text("");
        return true;
    }
};








////////////////






function Email_check(){
    var email=$("#user_name").val();
    if(email.length == '' || email.length == null) {
        $("#user_name").removeClass("has-success");
        $("#user_name").addClass("has-error");
        $("#email_label_edit").text("This Field is required");
        return false;
    }
        else{
            $("#user_name").addClass("has-success");
            $("#email_label_edit").text("");
            return true;
        }
    }

$("#user_name").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})

/////////

function Email_valid_check(){
    var letternumber = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    var email=$("#email_user").val();
    if(email.length == '' || email.length == null) {
        $("#email_user").removeClass("has-success");
        $("#email_user").addClass("has-error");
        $("#email_label").text("This Field is required");
        return false;
    }
    else{
        if(email.match(letternumber)){
            $("#email_user").addClass("has-success");
            $("#email_label").text("");
            return true;
            }
        else{
            $("#email_user").removeClass("has-success");
            $("#email_user").addClass("has-error");
            $("#email_label").text("please enter a valid email address");
            return false;
            }
        }
    }

$("#email_user").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})





///////// function for password field validation

function ssn_check_fun(){
    var password= $("#ssn_psw").val();
    if(password.length == '' || password.length == null) {
        $("#ssn_psw").removeClass("has-success");
        $("#ssn_psw").addClass("has-error");
        $("#password_label_ssn").text("This Field is required");
        return false;
    }
    else{
        if(password.length > 99 || password.length < 0){
            $("#ssn_psw").removeClass("has-success");
            $("#ssn_psw").addClass("has-error");
            $("#password_label_ssn").text("This field must contains 6 to 18 characters");
            return false;
            }
        else{
            $("#ssn_psw").addClass("has-success");
            $("#password_label_ssn").text("");
            return true;
            }
        }
    }
$("#ssn_psw").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})


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



////

//////////
function entity_Check(){
    if ($("#entity_Check").val() == 'Please_Select') {
        $("#entity_Check").removeClass("has-success");
        $("#entity_Check").addClass("has-error");
        $("#add_contact_label").text("This Field is required");
        return false;
    }
    else{
        $("#entity_Check").addClass("has-success");
        $("#add_contact_label").text("");
        return true;
    }
}

$("#entity_Check").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})


///////// for legal name
function legal_name_check(){
    var legal =$("#legal_name").val();
    if(legal.length == '' || legal.length == null) {
        $("#legal_name").removeClass("has-success");
        $("#legal_name").addClass("has-error");
        $("#legal_name_id").text("This Field is required");
        return false;
    }
        else{
            $("#legal_name").addClass("has-success");
            $("#legal_name_id").text("");
            return true;
        }
    }

$("#legal_name").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})
//////

function adress_label(){
    var legal =$("#Address").val();
    if(legal.length == '' || legal.length == null) {
        $("#Address").removeClass("has-success");
        $("#Address").addClass("has-error");
        $("#address_name_id").text("This Field is required");
        return false;
    }
    else{
        $("#Address").addClass("has-success");
        $("#address_name_id").text("");
        return true;
    }
    }

$("#Address").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})

////////////

function city_valid(){
	var city = $("#city_psw").val();
    if(city.length == '' || city.length == null) {
        $("#city_psw").removeClass("has-success");
        $("#city_psw").addClass("has-error");
        $("#city_label").text("This Field is required");
        return false;
    }
    else{
        if(city.length > 18 || city.length < 3){
            $("#city_psw").removeClass("has-success");
            $("#city_psw").addClass("has-error");
            $("#city_label").text("This field must contains 3 to 18 characters");
            return false;
            }
        else{
            $("#city_psw").addClass("has-success");
            $("#city_label").text("");
            return true;
            }
        }


}




$("#city_psw").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})

////////////

function region_valid(){
	var region_check = $("#region_Check_ist").val();
    if(region_check.length == '' || region_check.length == null) {
        $("#region_Check_ist").removeClass("has-success");
        $("#region_Check_ist").addClass("has-error");
        $("#region_label").text("This Field is required");
        return false;
    }
    else{
        if(region_check.length > 18 || region_check.length < 3){
            $("#region_Check_ist").removeClass("has-success");
            $("#region_Check_ist").addClass("has-error");
            $("#region_label").text("This Field must contains 3 to 18 characters");
            return false;
            }
        else{
            $("#region_Check_ist").addClass("has-success");
            $("#region_label").text("");
            return true;
            }
        }


}




$("#region_Check_ist").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})

//////////////



function ist_zip_code(){
    var legal =$("#check_zip_ist").val();
    var letterNumber = /^[+0-9 ]*$/;
    if(legal.length == '' || legal.length == null) {
        $("#check_zip_ist").removeClass("has-success");
        $("#check_zip_ist").addClass("has-error");
        $("#label_zip_ist").text("This Field is required");
        return false;
    }
    else{
        if(legal.match(letterNumber)){
                $("#check_zip_ist").addClass("has-success");
                $("#label_zip_ist").text("");
                return true;
            }
        else{
            $("#check_zip_ist").removeClass("has-success");
            $("#check_zip_ist").addClass("has-error");
            $("#label_zip_ist").text("It contains only numbers");
            return false;
        }
    }
    }

$("#check_zip_ist").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})


////////////

function countary_check(){

    if ($("#countary_check_text").val() == 'Please_Select') {
        $("#countary_check_text").removeClass("has-success");
        $("#countary_check_text").addClass("has-error");
        $("#add_contact_label_countary").text("This Field is required");
        return false;
    }
    else{
        $("#countary_check_text").addClass("has-success");
        $("#add_contact_label_countary").text("");
        return true;
    }
}

$("#countary_check_text").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})


$(document).on('change', '#countary_check_text', function(){
    if (($("#countary_check_text").val() == 'American_Samoa' || $("#countary_check_text").val() == 'United_States') && (($("#entity_Check").val() == "Private_Investor") || ($("#entity_type").val() == "Retirement Plan")) ){
        $("#usa_showing_div").show();

    }
    else{
        $("#usa_showing_div").hide();
    }
    if (($("#countary_check_text").val() == 'American_Samoa' || $("#countary_check_text").val() == 'United_States') && ($("#entity_type").val() == "RetirementPlan")) {
        $("#usa_showing_div").show();

    }

    if ($(this).val() == 'Please_Select'){
        $("#countary_check_text").removeClass("has-success");
        $("#countary_check_text").addClass("has-error");
        $("#add_contact_label_countary").text("This Field is required");
        return false ;

	}
	else {
		$("#countary_check_text").addClass("has-success");
		$("#add_contact_label_countary").text("");
		return true;
    }
});

///////////////
function type_of_account_check(){
    if ($("#type_of_account").val() == 'Please_Select') {
        $("#type_of_account").removeClass("has-success");
        $("#type_of_account").addClass("has-error");
        $("#account_type_check_label").text("This Field is required");
        return false;
    }
    else{
        $("#type_of_account").addClass("has-success");
        $("#account_type_check_label").text("");
        return true;
    }
}

$("#type_of_account").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})


$(document).on('change', '#type_of_account', function(){
	if ($(this).val() == 'Please_Select'){
        $("#type_of_account").removeClass("has-success");
        $("#type_of_account").addClass("has-error");
        $("#account_type_check_label").text("This Field is required");
        return false ;

	}
	else {
		$("#type_of_account").addClass("has-success");
		$("#account_type_check_label").text("");
		return true;
	}
});


////////////////

function Account_number_check(){
    var legal =$("#account_number").val();
    var letterNumber = /^[+0-9 ]*$/;
    if(legal.length == '' || legal.length == null) {
        $("#account_number").removeClass("has-success");
        $("#account_number").addClass("has-error");
        $("#account_check_label").text("This Field is required");
        return false;
    }
    else{

        if(legal.length > 10 || legal.length < 3){
            $("#account_number").removeClass("has-success");
            $("#account_number").addClass("has-error");
            $("#account_check_label").text("This Field must contains 3 to 10 characters");
            return false;
            }
        else{

            if(legal.match(letterNumber)){
                $("#account_number").addClass("has-success");
                $("#account_check_label").text("");
                return true;
            }
            else{
                $("#account_number").removeClass("has-success");
                $("#account_number").addClass("has-error");
                $("#account_check_label").text("It contains only numbers");
                return false;
            }

            }
        }

    }

$("#account_number").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})

//////////////


function MobileNumberCheckRegister(){
    var legal =$("#phone_number_register").val();
    var letterNumber = /^[+0-9 ]*$/;
    if(legal.length == '' || legal.length == null) {
        $("#phone_number_register").removeClass("has-success");
        $("#phone_number_register").addClass("has-error");
        $("#phone_number_register_label").text("This Field is required");
        return false;
    }
    else{

        if(legal.length > 15 || legal.length < 10){
            $("#phone_number_register").removeClass("has-success");
            $("#phone_number_register").addClass("has-error");
            $("#phone_number_register_label").text("This Field must contains 10 to 15 Numbers");
            return false;
            }
        else{

            if(legal.match(letterNumber)){
                $("#phone_number_register").addClass("has-success");
                $("#phone_number_register_label").text("");
                return true;
            }
            else{
                $("#phone_number_register").removeClass("has-success");
                $("#phone_number_register").addClass("has-error");
                $("#phone_number_register_label").text("It contains only numbers");
                return false;
            }

            }
        }

    }

$("#phone_number_register").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})

///////////////
function SwiftCode(){
    var letterNumber = /^[+0-9 ]*$/;
    var legal =$("#swiftcode").val();
    if(legal.length == '' || legal.length == null) {
        $("#swiftcode").removeClass("has-success");
        $("#swiftcode").addClass("has-error");
        $("#swift_label").text("This Field is required");
        return false;
    }
    else{
        if(legal.length > 10 || legal.length < 3){
            $("#swiftcode").removeClass("has-success");
            $("#swiftcode").addClass("has-error");
            $("#swift_label").text("This Field must contains 3 to 10 characters");
            return false;
            }
        else{
            if(legal.match(letterNumber)){
                $("#swiftcode").addClass("has-success");
                $("#swift_label").text("");
                return true;
            }
            else{
                $("#swiftcode").removeClass("has-success");
                $("#swiftcode").addClass("has-error");
                $("#swift_label").text("It contains only numbers");
                return false;
            }

            }
    }
    }

$("#swiftcode").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})


/////////////
function Financial_account_Valid(){
    var legal =$("#Financial_account").val();
    if(legal.length == '' || legal.length == null) {
        $("#Financial_account").removeClass("has-success");
        $("#Financial_account").addClass("has-error");
        $("#bank_namelabel").text("This Field is required");
        return false;
    }
    else{
        $("#Financial_account").addClass("has-success");
        $("#bank_namelabel").text("");
        return true;
    }
    }

$("#Financial_account").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})
////

////////entity

function legal_name_entity(){
    var legal =$("#Legal_investing_name").val();
    if(legal.length == '' || legal.length == null) {
        $("#Legal_investing_name").removeClass("has-success");
        $("#Legal_investing_name").addClass("has-error");
        $("#legal_name_label_entity").text("This Field is required");
        return false;
    }
        else{
            $("#Legal_investing_name").addClass("has-success");
            $("#legal_name_label_entity").text("");
            return true;
        }
    }

$("#Legal_investing_name").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})
//////

function adress_label_entity(){
    var legal =$("#entity_address").val();
    if(legal.length == '' || legal.length == null) {
        $("#entity_address").removeClass("has-success");
        $("#entity_address").addClass("has-error");
        $("#address_label_entity").text("This Field is required");
        return false;
    }
    else{
        $("#entity_address").addClass("has-success");
        $("#address_label_entity").text("");
        return true;
    }
    }

$("#entity_address").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})

////////////

function city_valid_entity(){
	var city = $("#entity_city").val();
    if(city.length == '' || city.length == null) {
        $("#entity_city").removeClass("has-success");
        $("#entity_city").addClass("has-error");
        $("#entity_city_label").text("This Field is required");
        return false;
    }
    else{
        if(city.length > 18 || city.length < 3){
            $("#entity_city").removeClass("has-success");
            $("#entity_city").addClass("has-error");
            $("#entity_city_label").text("This field must contains 3 to 18 characters");
            return false;
            }
        else{
            $("#entity_city").addClass("has-success");
            $("#entity_city_label").text("");
            return true;
            }
        }


}




$("#entity_city").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})

////////////




//////////////



function entity_zip_code_check(){
    var letterNumber = /^[+0-9 ]*$/;
    var legal =$("#entity_zip_Code").val();
    if(legal.length == '' || legal.length == null) {
        $("#entity_zip_Code").removeClass("has-success");
        $("#entity_zip_Code").addClass("has-error");
        $("#entity_zip_label").text("This Field is required");
        return false;
    }
    else{
        if(legal.match(letterNumber)){
               $("#entity_zip_Code").addClass("has-success");
                $("#entity_zip_label").text("");
                return true;
            }
            else{
                $("#entity_zip_Code").removeClass("has-success");
                $("#entity_zip_Code").addClass("has-error");
                $("#entity_zip_label").text("It contains only numbers");
                return false;
            }
        
    }
    }

$("#entity_zip_Code").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})


////////////

function countary_check_Entity(){
    if ($("#countary_zip_code_entity").val() == 'Please_Select') {
        $("#countary_zip_code_entity").removeClass("has-success");
        $("#countary_zip_code_entity").addClass("has-error");
        $("#add_contact_label_countary").text("This Field is required");
        return false;
    }
    else{
        $("#countary_zip_code_entity").addClass("has-success");
        $("#add_contact_label_countary").text("");
        return true;
    }
}

$("#countary_zip_code_entity").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})


$(document).on('change', '#countary_zip_code_entity', function(){
    if (($("#countary_zip_code_entity").val() == 'American_Samoa' || $("#countary_zip_code_entity").val() == 'United_States') && (($("#entity_Check").val() == "Private_Investor") || ($("#entity_type").val() == "Retirement Plan"))) {
        $("#usa_showing_div").show();
    }
    else{
        $("#usa_showing_div").hide();
    }
    
    if (($("#countary_check_text").val() == 'American_Samoa' || $("#countary_check_text").val() == 'United_States') && ($("#entity_type").val() == "Retirement Plan")) {
        $("#usa_showing_div").show();

    }

	if ($(this).val() == 'Please_Select'){
        $("#countary_zip_code_entity").removeClass("has-success");
        $("#countary_zip_code_entity").addClass("has-error");
        $("#countary_zip_code_label").text("This Field is required");

	}
	else {
		$("#countary_zip_code_entity").addClass("has-success");
		$("#countary_zip_code_label").text("");
		return true;
	}
});


////////////// entities



















///////////////////
$(document).on('submit', '#submit_function', function(){
	var get_value_of = $("#entity_Check").val();
	if (get_value_of == 'Private_Investor'){
			     if (Email_check() && SwiftCode() && MobileNumberCheckRegister() && Financial_account_Valid() && 
					Account_number_check() && type_of_account_check() && ist_zip_code() 
					&& countary_check() && legal_name_check() && city_valid() && region_valid() 
					&& adress_label() && Email_valid_check() && Password() && entity_Check() == true){
                    if ($("#countary_check_text").val() == 'American_Samoa' || $("#countary_check_text").val() == 'United_States'){
                        if (ssn_check_fun() == true){
                            return true ;
                        }
                        else{
                            Email_check();
                            SwiftCode();
                            MobileNumberCheckRegister();
                            Financial_account_Valid();
                            Account_number_check();
                            type_of_account_check();
                            countary_check();
                            Email_valid_check();
                            Password();
                            ist_zip_code();
                            entity_Check();
                            city_valid();
                            legal_name_check();
                            adress_label();
                            region_valid();
                            ssn_check_fun();
                            return false;
                        }
                    }
                    else{
                        return true;
                    }						
				}
				else{
					Email_check();
					SwiftCode();
					Financial_account_Valid();
					Account_number_check();
					type_of_account_check();
					countary_check();
					Email_valid_check();
					Password();
					ist_zip_code();
					entity_Check();
					city_valid();
					legal_name_check();
					adress_label();
                    region_valid();
                    MobileNumberCheckRegister();
					return false ;
				}

			}
	else{
		if (Email_check() && Email_valid_check() && MobileNumberCheckRegister() && Password() && entity_Check() 
         && check_entity_type() && legal_name_entity() && adress_label_entity() 
			&& city_valid_entity() && entity_zip_code_check() && 
			countary_check_Entity() && SwiftCode() && Financial_account_Valid() 
			&& Account_number_check() &&type_of_account_check() 
             == true){
                if ($("#countary_zip_code_entity").val() == 'American_Samoa' || $("#countary_zip_code_entity").val() == 'United_States'){
                        if (ssn_check_fun() == true){
                            return true ;
                        }
                        else{
                            Email_check();
                            SwiftCode();
                            Financial_account_Valid();
                            Account_number_check();
                            type_of_account_check();
                            countary_check();
                            Email_valid_check();
                            Password();
                            check_entity_type();
                            MobileNumberCheckRegister();
                            ist_zip_code();
                            entity_Check();
                            city_valid();
                            legal_name_check();
                            adress_label();
                            ssn_check_fun();
                            return false;
                        }
                    }
                else{
                    return true;
                }
		}
		else{
			Email_check();
            check_entity_type();
			legal_name_entity();
			adress_label_entity() ;
			city_valid_entity();
			entity_zip_code_check();
			countary_check_Entity();
            SwiftCode();
            MobileNumberCheckRegister();
			Financial_account_Valid();
			Account_number_check();
			type_of_account_check();
			Email_valid_check();
			Password();
			entity_Check();
			return false;

		}
	}

	
})