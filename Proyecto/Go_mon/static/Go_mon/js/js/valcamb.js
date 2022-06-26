var conta = /^(?=.*\d)(?=.*[\u0021-\u002b\u003c-\u0040])(?=.*[A-Z])(?=.*[a-z])\S{8,16}$/;

$(document).ready(function(){
    $("#reg").click(function(e){
        e.preventDefault();
        var contra = $("#cont").val();
        var rcont = $("#rcont").val();

        if(contra == "" || !conta.test(contra)){
            $("#mensajeLarg").fadeIn();
            return false;

        }else{
            $("#mensajeLarg").fadeOut();
            

            if(rcont == "" || contra != rcont){
                $("#mensajeIg").fadeIn();
                return false;

            }else{
                $("#mensajeIg").fadeOut();
                onclick=$(location).attr('href','Pag_Principal.html');
            }
        }

    });
})