
var regex = /[\w-\.]{2,}@[a-zA-Z0-9._-]+\.[\w-]{2,4}/;
$("#sub").click(function(s){
    var email = $("#email").val();

    if(email == "" || !regex.test(email)){
        $("#mensajeS").fadeIn();
        return false;
    }else{
        $("#mensajeS").fadeOut();
        $("#mensajeSus").fadeIn();
        $("#mensajeSus").fadeOut(2500);
        return false;




    }
});