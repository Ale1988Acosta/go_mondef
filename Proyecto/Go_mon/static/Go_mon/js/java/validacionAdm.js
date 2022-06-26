
var regex = /[\w-\.]{2,}@administrador\.[\w-]{2,4}/;
$(document).ready(function(){
    $("#entrar").click(function(){
        var correo = $("#correo").val();
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
                onclick=$(location).attr('href','adm.html');
                $("#mensajeP").fadeout();

            }
          
        }
      

        
    });

    





})