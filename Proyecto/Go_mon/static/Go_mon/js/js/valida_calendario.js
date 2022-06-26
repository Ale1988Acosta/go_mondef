$(document).ready(function(){
    $("#formu_3").submit(function(e){
        e.preventDefault();
        let mensajecal ="";
        let entrar = false;

        var anno = moment().format('YYYY');
        var sem = moment().format('WW');
        var hoy = (anno+"-W"+sem);
        var fecha = $("#unasemana").val();
        if(fecha<hoy){
        mensajecal+="No se pueden seleccionar semanas anteriores a la de hoy.<br>";
        entrar=true;
        }

        if(entrar){
        $("#mensajec").html(mensajecal);
        }else{
        $("#mensajec").html("Revise sus reservas :)");
        }
    });
 })