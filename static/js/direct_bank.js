$(document).on('change', '#transfer_made', function(){
        if ($("#transfer_made").prop('checked') == true){
           $("#bank_transfer_button").prop("disabled",false);
           return true;
       }
       else{
           $("#bank_transfer_button").prop("disabled",true);
           return false;
       } 
   })
