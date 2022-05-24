$(document).on('click','#documents_tab', function(){
	$('#emergency_tab').removeClass("active show");
	$('#distribution_tab').removeClass("active show");
	$('#documents_div').addClass("active show");
})



$(document).on('click','#emergency_tab', function(){
	$('#documents_tab').removeClass("active show");
	$('#distribution_tab').removeClass("active show");
})


$(document).on('click','#distribution_tab', function(){
	$('#documents_tab').removeClass("active show");
	$('#emergency_tab').removeClass("active show");
})


/*$(document).on('click', '#personal_tab', function () {
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
});*/










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