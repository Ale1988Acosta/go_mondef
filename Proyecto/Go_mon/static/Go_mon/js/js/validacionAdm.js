
var re = /[\w-\.]{2,}@administrador\.[\w-]{2,4}/;
var conta = /^(?=.*\d)(?=.*[\u0021-\u002b\u003c-\u0040])(?=.*[A-Z])(?=.*[a-z])\S{8,16}$/;

$(document).ready(function(){
    $("#entrar").click(function(e){
        e.preventDefault();
        var correo = $("#correo").val();
        var clave = $("#clave").val();

        if(correo == "" || !re.test(correo)){
            $("#mensajeC").fadeIn();
            return false;
        }else{
            
            $("#mensajeC").fadeOut();
            
            if(clave == ""|| !conta.test(clave)){
                $("#mensajeP").fadeIn();
                return false;
                

            }else{
                onclick=$(location).attr('href','adm.html');
                $("#mensajeP").fadeOut();
                

            }
          
        }
      

        
    });

    





});