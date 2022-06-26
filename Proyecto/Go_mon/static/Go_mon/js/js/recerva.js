$(document).ready(function(){
    $("#form1").submit(function(e){
        e.preventDefault();
        let mensajeMostrar = "";
        let entrar = false;

        //fecha de nacimiento
        var fecharec = $("#fecha").val();
        var date = new Date().toLocaleDateString('en-CA');
        if(fecharec<=date){
            mensajeMostrar+="la fecha de recerva debe ser despues del dia de hoy.<br>";
            entrar=true;
        }

        //horas
        if(!document.querySelector('input[id="check1"]:checked')) {
            mensajeMostrar+="Debes seleccionar al menos una hora.<br>";
            entrar = true;
        }

        if(entrar){
            $("#mensaje").html(mensajeMostrar);
        }
        else{
            $("#mensaje").html("recerva completa, espere los resultados");
            onclick=$(location).attr('href','buscador.html');
        }
    });
})