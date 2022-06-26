
var regex = /[\w-\.]{2,}@[a-zA-Z0-9._-]+\.[\w-]{2,4}/;
$(document).ready(function(){
    $("#entrar").click(function(){
        var correo = $("#correoU").val();
        var clave = $("#pass").val();

        if(correo == "" || !regex.test(correo)){
            $("#mensajeC").fadeIn();
            return false;
        }else{
            $("#mensajeC").fadeOut();
            
            if(clave == ""){
                $("#mensajeP").fadeIn();
                return false;
                

            }else{
                onclick=$(location).attr('href','recerva.html');
                $("#mensajeP").fadeout();

            }
          
        }
      

        
    });

    





})