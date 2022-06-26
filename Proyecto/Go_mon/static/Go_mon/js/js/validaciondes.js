$(document).ready(function(){
    $("#form1").submit(function(e){
        let mensajeMostrar = "";
        let entrar = false;

        var anno = moment().format('YYYY');
        var sem = moment().format('WW');
        var hoy = (anno+"-W"+sem);
        var fecha = $("#semana").val();

        if(fecha<hoy){
            mensajeMostrar+="No se pueden seleccionar semanas anteriores a la de hoy.<br>";
            entrar=true;
        }

        if(entrar){
            $("#mensaje").html(mensajeMostrar);
        }
        else{
            onclick=$(location).attr('href','');
        }
    });
})