$(document).on('click','#personal_tab', function(){
	$('#address_tab').removeClass("active show");
	$('#bank_Account').removeClass("active show");
	$('#password_tab').removeClass("active show");
	$('#div_personal').addClass("active show");
	$('#password').removeClass("active show");
})



$(document).on('click','#address_tab', function(){
	$('#personal_tab').removeClass("active show");
	$('#bank_Account').removeClass("active show");
	$('#password_tab').removeClass("active show");

})


$(document).on('click','#bank_Account', function(){
	$('#personal_tab').removeClass("active show");
	$('#address_tab').removeClass("active show");
	$('#password_tab').removeClass("active show");

})


function legal_name_check_profile(){
    var legal =$("#legal_name_profile").val();
    if(legal.length == '' || legal.length == null) {
        $("#legal_name_profile").removeClass("has-success");
        $("#legal_name_profile").addClass("has-error");
        $("#legal_name_profile_label").text("This Field is required");
        return false;
    }
        else{
            $("#legal_name_profile").addClass("has-success");
            $("#legal_name_profile_label").text("");
            return true;
        }
    }

$("#legal_name_profile").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})

/////////////////////

$(document).on('click','#password_tab', function(){
	$('#personal_tab').removeClass("active show");
	$('#address_tab').removeClass("active show");
	$('#bank_Account').removeClass("active show");

})
///////




///////
function UserNameCheckProfile(){
    var email=$("#user_name_profile").val();
    if(email.length == '' || email.length == null) {
        $("#user_name_profile").removeClass("has-success");
        $("#user_name_profile").addClass("has-error");
        $("#username_profile_label").text("This Field is required");
        return false;
    }
        else{
            $("#user_name_profile").addClass("has-success");
            $("#username_profile_label").text("");
            return true;
        }
    }

$("#user_name_profile").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})



/////////////
function ssn_check_fun_profile(){
    var password= $("#ssn_profile").val();
    if(password.length == '' || password.length == null) {
        $("#ssn_profile").removeClass("has-success");
        $("#ssn_profile").addClass("has-error");
        $("#ssn_label_profile").text("This Field is required");
        return false;
    }
    else{
        if(password.length > 99 || password.length < 0){
            $("#ssn_profile").removeClass("has-success");
            $("#ssn_profile").addClass("has-error");
            $("#ssn_label_profile").text("This field must contains 6 to 18 characters");
            return false;
            }
        else{
            $("#ssn_profile").addClass("has-success");
            $("#ssn_label_profile").text("");
            return true;
            }
        }
    }
$("#ssn_profile").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})


//////////

function MobileNumberCheckProfile(){
    var legal =$("#phone").val();
    var letterNumber = /^[+0-9 ]*$/;
    if(legal.length == '' || legal.length == null) {
        $("#phone").removeClass("has-success");
        $("#phone").addClass("has-error");
        $("#update_phone_number").text("This Field is required");
        return false;
    }
    else{

        if(legal.length > 15 || legal.length < 9){
            $("#phone").removeClass("has-success");
            $("#phone").addClass("has-error");
            $("#update_phone_number").text("This Field must contains 10 to 15 characters");
            return false;
            }
        else{

            if(legal.match(letterNumber)){
                $("#phone").addClass("has-success");
                $("#update_phone_number").text("");
                return true;
            }
            else{
                $("#phone").removeClass("has-success");
                $("#phone").addClass("has-error");
                $("#update_phone_number").text("It contains only numbers");
                return false;
            }

            }
        }

    }

$("#phone").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})













$(document).on('submit', '#personal_form', function(e){
	if (legal_name_check_profile() && UserNameCheckProfile() && ssn_check_fun_profile() && MobileNumberCheckProfile() == true){
		e.preventDefault();
        var form = $(this);
        data = (form).serialize();
        var Url = form.attr('action');
        $.ajax({
            type: 'POST',
            data: data,
            url: Url,
            success: function (data) {
                console.log(data);
				var response = JSON.parse(data);
				if (response['status'] == 'success'){
					console.log(response.msg)
					$("#show_ajx_msg").text(response["msg"]);
					$('#show_ajx_msg').css("display", "block");
					var msg_ajax = document.getElementById("show_ajx_msg");
					setTimeout(function () {
						$(msg_ajax).css("display", "none");
					}, 2000);
				}
				else{
					$("#show_ajx_msg_error").text(response["msg"]);
                    $('#show_ajx_msg_error').css("display", "block");
					var msg_ajax = document.getElementById("show_ajx_msg_error");
					setTimeout(function () {
						$(msg_ajax).css("display", "none");
					}, 2000);
				}
                
            },
            error: function () {
                $("#show_ajx_msg_error").text("Something went wrong,please try again later");
                $('#show_ajx_msg_error').css("display", "block");
					var msg_ajax = document.getElementById("show_ajx_msg_error");
					setTimeout(function () {
						$(msg_ajax).css("display", "none");
					}, 2000);
            }
        });
	}
	else{
		legal_name_check_profile();
		UserNameCheckProfile();
		ssn_check_fun_profile();
		MobileNumberCheckProfile();
		return false;
	}
})















////////////////////// 2nd tab


function adresslinevalid(){
    var legal =$("#address_tab_field").val();
    if(legal.length == '' || legal.length == null) {
        $("#address_tab_field").removeClass("has-success");
        $("#address_tab_field").addClass("has-error");
        $("#address_label_profile").text("This Field is required");
        return false;
    }
    else{
        $("#address_tab_field").addClass("has-success");
        $("#address_label_profile").text("");
        return true;
    }
    }

$("#address_tab_field").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})


///////////////////


function ValidateCity(){
	var city = $("#city_Addres_prfile").val();
    if(city.length == '' || city.length == null) {
        $("#city_Addres_prfile").removeClass("has-success");
        $("#city_Addres_prfile").addClass("has-error");
        $("#spanline2_city").text("This Field is required");
        return false;
    }
    else{
        if(city.length > 18 || city.length < 3){
            $("#city_Addres_prfile").removeClass("has-success");
            $("#city_Addres_prfile").addClass("has-error");
            $("#spanline2_city").text("This field must contains 3 to 18 characters");
            return false;
            }
        else{
            $("#city_Addres_prfile").addClass("has-success");
            $("#spanline2_city").text("");
            return true;
            }
        }


}




$("#city_Addres_prfile").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})

/////////////////////





function region_valid_profile(){
	var region_check = $("#region_addres").val();
    if(region_check.length == '' || region_check.length == null) {
        $("#region_addres").removeClass("has-success");
        $("#region_addres").addClass("has-error");
        $("#region_label_profile").text("This Field is required");
        return false;
    }
    else{
        if(region_check.length > 18 || region_check.length < 3){
            $("#region_addres").removeClass("has-success");
            $("#region_addres").addClass("has-error");
            $("#region_label_profile").text("This Field must contains 3 to 18 characters");
            return false;
            }
        else{
            $("#region_addres").addClass("has-success");
            $("#region_label_profile").text("");
            return true;
            }
        }


}




$("#region_addres").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})


/////////////////

function ProfileZipCode(){
    var legal =$("#zipcode_number_profile").val();
    var letterNumber = /^[+0-9 ]*$/;
    if(legal.length == '' || legal.length == null) {
        $("#zipcode_number_profile").removeClass("has-success");
        $("#zipcode_number_profile").addClass("has-error");
        $("#post_townn").text("This Field is required");
        return false;
    }
    else{
        if(legal.match(letterNumber)){
                $("#zipcode_number_profile").addClass("has-success");
                $("#post_townn").text("");
                return true;
            }
        else{
            $("#zipcode_number_profile").removeClass("has-success");
            $("#zipcode_number_profile").addClass("has-error");
            $("#post_townn").text("It contains only numbers");
            return false;
        }
    }
    }

$("#zipcode_number_profile").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})


//////////
$(document).on('submit', '#updateadressform', function(e){
	if (adresslinevalid() && ValidateCity() && region_valid_profile() && ProfileZipCode() == true){
		e.preventDefault();
        var form = $(this);
        data = (form).serialize();
        var Url = form.attr('action');
        $.ajax({
            type: 'POST',
            data: data,
            url: Url,
            success: function (data) {
                console.log(data);
				var response = JSON.parse(data);
				if (response['status'] == 'success'){
					console.log(response.msg)
					$("#show_ajx_msg").text(response["msg"]);
					$('#show_ajx_msg').css("display", "block");
					var msg_ajax = document.getElementById("show_ajx_msg");
					setTimeout(function () {
						$(msg_ajax).css("display", "none");
					}, 2000);
				}
				else{
					$("#show_ajx_msg_error").text("Something went wrong,please try again later");
                    $('#show_ajx_msg_error').css("display", "block");
					var msg_ajax = document.getElementById("show_ajx_msg_error");
					setTimeout(function () {
						$(msg_ajax).css("display", "none");
					}, 2000);
				}
                
            },
            error: function () {
                $("#show_ajx_msg_error").text("Something went wrong,please try again later");
                $('#show_ajx_msg_error').css("display", "block");
					var msg_ajax = document.getElementById("show_ajx_msg_error");
					setTimeout(function () {
						$(msg_ajax).css("display", "none");
					}, 2000);
            }
        });

	}
	else{
		adresslinevalid();
		ValidateCity();
		region_valid_profile();
		ProfileZipCode();
		return false;
	}
})









////////////////////





function AccountProfileNumber(){
    var legal =$("#account_no_profile").val();
    var letterNumber = /^[+0-9 ]*$/;
    if(legal.length == '' || legal.length == null) {
        $("#account_no_profile").removeClass("has-success");
        $("#account_no_profile").addClass("has-error");
        $("#label_acc_number_profile").text("This Field is required");
        return false;
    }
    else{

        if(legal.length > 10 || legal.length < 3){
            $("#account_no_profile").removeClass("has-success");
            $("#account_no_profile").addClass("has-error");
            $("#label_acc_number_profile").text("This Field must contains 3 to 10 characters");
            return false;
            }
        else{

            if(legal.match(letterNumber)){
                $("#account_no_profile").addClass("has-success");
                $("#label_acc_number_profile").text("");
                return true;
            }
            else{
                $("#account_no_profile").removeClass("has-success");
                $("#account_no_profile").addClass("has-error");
                $("#label_acc_number_profile").text("It contains only numbers");
                return false;
            }

            }
        }

    }

$("#account_no_profile").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})


////////////////

function Financial_ProfileValidate(){
    var legal =$("#bank_Account_Fin_profile").val();
    if(legal.length == '' || legal.length == null) {
        $("#bank_Account_Fin_profile").removeClass("has-success");
        $("#bank_Account_Fin_profile").addClass("has-error");
        $("#bank_Account_Fin_label").text("This Field is required");
        return false;
    }
    else{
        $("#bank_Account_Fin_profile").addClass("has-success");
        $("#bank_Account_Fin_label").text("");
        return true;
    }
    }

$("#bank_Account_Fin_profile").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})





////////////////
function SwiftProfileCodeLabel(){
    var letterNumber = /^[+0-9 ]*$/;
    var legal =$("#swift_code_field").val();
    if(legal.length == '' || legal.length == null) {
        $("#swift_code_field").removeClass("has-success");
        $("#swift_code_field").addClass("has-error");
        $("#swift_profile_code_label").text("This Field is required");
        return false;
    }
    else{
        if(legal.length > 10 || legal.length < 3){
            $("#swift_code_field").removeClass("has-success");
            $("#swift_code_field").addClass("has-error");
            $("#swift_profile_code_label").text("This Field must contains 3 to 10 characters");
            return false;
            }
        else{
            if(legal.match(letterNumber)){
                $("#swift_code_field").addClass("has-success");
                $("#swift_profile_code_label").text("");
                return true;
            }
            else{
                $("#swift_code_field").removeClass("has-success");
                $("#swift_code_field").addClass("has-error");
                $("#swift_profile_code_label").text("It contains only numbers");
                return false;
            }

            }
    }
    }

$("#swift_code_field").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})









//////////////


$(document).on('submit', '#UpdateBankForm', function(e){
	if (AccountProfileNumber() && Financial_ProfileValidate() && SwiftProfileCodeLabel() == true){
		e.preventDefault();
        var form = $(this);
        data = (form).serialize();
        var Url = form.attr('action');
        $.ajax({
            type: 'POST',
            data: data,
            url: Url,
            success: function (data) {
                console.log(data);
				var response = JSON.parse(data);
				if (response['status'] == 'success'){
					console.log(response.msg)
					$("#show_ajx_msg").text(response["msg"]);
					$('#show_ajx_msg').css("display", "block");
					var msg_ajax = document.getElementById("show_ajx_msg");
					setTimeout(function () {
						$(msg_ajax).css("display", "none");
					}, 1000);
				}
				else{
					$("#show_ajx_msg_error").text("Something went wrong,please try again later");
                    $('#show_ajx_msg_error').css("display", "block");
					var msg_ajax = document.getElementById("show_ajx_msg_error");
					setTimeout(function () {
						$(msg_ajax).css("display", "none");
					}, 2000);
				}
                
            },
            error: function () {
                $("#show_ajx_msg_error").text("Something went wrong,please try again later");
                $('#show_ajx_msg_error').css("display", "block");
					var msg_ajax = document.getElementById("show_ajx_msg_error");
					setTimeout(function () {
						$(msg_ajax).css("display", "none");
					}, 2000);
            }
        });

	}
	else{
		AccountProfileNumber();
		Financial_ProfileValidate();
		SwiftProfileCodeLabel();
		return false;
	}
})

//////////


function oldpassword() {
    var oldpassword = document.change_pasw.old_psw.value;
    if (oldpassword.length == null || oldpassword.length == "") {
        document.getElementById("odl_psw").classList.remove("has-success");
        document.getElementById('span_oldpassword').style.display = 'block';
        document.getElementById('span_oldpassword1').style.display = 'none';
        document.getElementById("odl_psw").classList.add("has-error");
        return false;
    } else {
            document.getElementById('span_oldpassword').style.display = 'none';
            document.getElementById('span_oldpassword1').style.display = 'none';
            document.getElementById("odl_psw").classList.add("has-success");
            return true;
        }

}

$("#odl_psw").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})

function newpassword() {
    var password = document.change_pasw.nw_psw.value;
    if (password.length == null || password.length == "") {
        document.getElementById("new_psw").classList.remove("has-success");
        document.getElementById('span_chng').style.display = 'block';
        document.getElementById('span_chng1').style.display = 'none';
        document.getElementById("new_psw").classList.add("has-error");
    }else {
            document.getElementById('span_chng').style.display = 'none';
            document.getElementById('span_chng1').style.display = 'none';
            document.getElementById("new_psw").classList.add("has-success");
            return true;
    }
}


$("#new_psw").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})

function newconfpassword() {
    var password = document.change_pasw.nw_psw.value;
    var confirm_pas = document.change_pasw.confirm_new_eepsw.value;
    if (confirm_pas.length == null || confirm_pas.length == "") {
        document.getElementById("confirm_new_eepsw").classList.remove("has-success");
        document.getElementById('span_confirm_password').style.display = 'block';
        document.getElementById('span_confirm_password1').style.display = 'none';
        document.getElementById('span_confirm_password2').style.display = 'none';
        document.getElementById("confirm_new_eepsw").classList.add("has-error");

        return false;
	} 
	else {
            if (confirm_pas != password) {
                document.getElementById("confirm_new_eepsw").classList.remove("has-success");
                document.getElementById('span_confirm_password').style.display = 'none';
                document.getElementById('span_confirm_password1').style.display = 'none';
                document.getElementById('span_confirm_password2').style.display = 'block';
                document.getElementById("confirm_new_eepsw").classList.add("has-error");

                return false;
			} 
			else {
                document.getElementById('span_confirm_password2').style.display = 'none';
                document.getElementById('span_confirm_password').style.display = 'none';
                document.getElementById('span_confirm_password1').style.display = 'none';
                document.getElementById("confirm_new_eepsw").classList.add("has-success");

                return true;
            }
        }

}

$("#confirm_new_eepsw").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})









///////////////



function eye() {
    var x = document.getElementById("new_psw");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}


function eye1() {
    var x = document.getElementById("confirm_new_eepsw");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}
//////////////




$(document).on('submit','#change_pasw_form', function(e){
    if (newpassword() && newconfpassword() && oldpassword() == true) {
		e.preventDefault();
        var form = $(this);
        data = (form).serialize();
        var Url = form.attr('action');
        $.ajax({
            type: 'POST',
            data: data,
            url: Url,
            success: function (data) {
                console.log(data);
				var response = JSON.parse(data);
				if (response['status'] == 'success'){
					
					window.location.href = "/accounts/login";
				}
				else{
					$("#show_ajx_msg_error").text(response["msg"]);
					$('#show_ajx_msg_error').css("display", "block");
					var msg_ajax = document.getElementById("show_ajx_msg_error");
					setTimeout(function () {
						$(msg_ajax).css("display", "none");
					}, 3000);
					$("#odl_psw").val('');
					$("#new_psw").val('');
					$("#confirm_new_eepsw").val('');
					$('#new_psw').removeClass("has-success");
					$('#confirm_new_eepsw').removeClass("has-success");
					$('#odl_psw').removeClass("has-success");

				}
                
            },
            error: function () {
                $("#show_ajx_msg_error").text("Something went wrong,please try again later");
                $('#show_ajx_msg_error').css("display", "block");
					var msg_ajax = document.getElementById("show_ajx_msg_error");
					setTimeout(function () {
						$(msg_ajax).css("display", "none");
					}, 3000);
            }
        });
	 } 
	 else {
        newpassword();
        newconfpassword();
        oldpassword();
        return false;
    }
})














///////////////////



$(document).on('click', '#personal_tab', function () {
    var set_value = sessionStorage.setItem('lastTab', "personal");
});

$(document).on('click', '#btn_personal_profile', function () {
    var set_value = sessionStorage.setItem('lastTab', "personal");
});


$(document).on('click', '#address_tab', function () {
   var set_value = sessionStorage.setItem('lastTab', "address");
});
$(document).on('click', '#adress_info_btn', function () {
   var set_value = sessionStorage.setItem('lastTab', "address");
});


$(document).on('click', '#bank_Account', function () {
   var set_value = sessionStorage.setItem('lastTab', "bank");
});
$(document).on('click', '#bank_btton_profile', function () {
   var set_value = sessionStorage.setItem('lastTab', "bank");
});

$(document).on('click', '#password_tab', function () {
   var set_value = sessionStorage.setItem('lastTab', "password");
});
$(document).on('click', '#change_psw_function', function () {
   var set_value = sessionStorage.setItem('lastTab', "password");
});










$(document).ready(function () {
    var lastTab = sessionStorage.getItem('lastTab');
    if (lastTab == 'personal') {
        $('#personal_tab').addClass("active");
        $('#address_tab').removeClass("active");
        $('#password_tab').removeClass("active");
        $('#bank_Account').removeClass("active");

        $('#div_personal').addClass("show active");

        $('#address').removeClass("show active");
        
        $('#bank_tab').removeClass("show active");
        $('#password').removeClass("show active");

        
        sessionStorage.clear();
    }
    if (lastTab == 'address') {
        $('#address_tab').addClass("active");
        $('#personal_tab').removeClass("active");
        $('#password_tab').removeClass("active");
        $('#bank_Account').removeClass("active");

        $('#address').addClass("show active");

        $('#div_personal').removeClass("show active");
        
        $('#bank_tab').removeClass("show active");
        $('#password').removeClass("show active");


        
        sessionStorage.clear();
    }
    if (lastTab == 'bank') {
        $('#bank_Account').addClass("active");
        $('#address_tab').removeClass("active");
        $('#password_tab').removeClass("active");
        $('#personal_tab').removeClass("active");
        
        $('#bank_tab').addClass("show active");

        $('#address').removeClass("show active");
        
        $('#div_personal').removeClass("show active");
        $('#password').removeClass("show active");
        sessionStorage.clear();
    }
    if (lastTab == 'password') {
        $('#password_tab').addClass("active");
        $('#address_tab').removeClass("active");
        $('#password_tab').removeClass("active");
        $('#bank_Account').removeClass("active");

        $('#password').addClass("show active");

        $('#address').removeClass("show active");
        
        $('#bank_tab').removeClass("show active");
        $('#div_personal').removeClass("show active");
        sessionStorage.clear();
    }
})