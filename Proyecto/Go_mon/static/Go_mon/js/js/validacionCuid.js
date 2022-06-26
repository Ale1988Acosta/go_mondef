
var regex = /[\w-\.]{2,}@[a-zA-Z0-9._-]+\.[\w-]{2,4}/;
var conta = /^(?=.*\d)(?=.*[\u0021-\u002b\u003c-\u0040])(?=.*[A-Z])(?=.*[a-z])\S{8,16}$/;
$(document).ready(function(){
    $("#entrar").click(function(e){
        var correo = $("#correoC").val();
        var clave = $("#pass").val();

        if(correo ==  "" || !regex.test(correo)){
            $("#mensajeC").fadeIn();
            return false;
        }else{
            $("#mensajeC").fadeOut();
        }
            
        if(clave == ""||!conta.test(clave)){
            $("#mensajeP").fadeIn();
            return false;
                

        }else{
            $("#mensajeP").fadeOut();
            onclick=$(location).attr('href','');

        }
            
          
        
      

        
    });

    $("#sub").click(function(s){
        s.preventDefault();
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

    





})