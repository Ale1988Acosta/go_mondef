var expr= /^[a-zA-Z]+\s?[a-zA-Z]+?\s?$/;
var dir= /^[0-9]/;
var esp = /^[a-zA-Z\d?]+$/;
var msj = document.getElementById("#mensaje");

$(document).ready(function(){
    $("#reg").click(function(e){
        var nomb = $("#nomb").val();
        var ape = $("#Ap").val();
        var telefo = $("#telefo").val();
        let mensajeMostrar ="";
        let entrar = false;

        //validación del nombre
        if(nomb == "" || !expr.test(nomb)){
            $("#mensajeN").fadeIn();
            return false;

        }else{
            $("#mensajeN").fadeOut();

            //validación del apellido
            if(ape == "" || !expr.test(ape)){
                $("#mensajeA").fadeIn();
                return false;
            }else{
                $("#mensajeA").fadeOut();

                //validación del telefono
                if(telefo == "" || !dir.test(telefo)){
                    $("#mensajeD").fadeIn();
                    return false;
                }else{
                    $("#mensajeD").fadeOut();

                }
            }
        }

    });

})