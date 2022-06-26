$(document).ready(function(){
    form1.addEventListener("submit" , e/* nombre, puede ser cualquiera*/  => {
    let mensajeMostrar ="";
    let entrar = false;
    var nom = $("#nom").val();
    var ap = $("#ap").val();
    var cont = $("#cont").val();
    var rcont = $("#rcont").val();
    var comuna = $("#comuna").val();
    var direccion = $("#direccion").val();
    var correo = $("#email").val();
    var valnombre = /^[a-zA-ZÀ-ÿ\s]{1,30}$/;

    /* Validar correo */
    var correo= $("#email").val();
    var num = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;
    if(!num.test(correo)){  
        mensajeMostrar +="Debe ingresar un correo invalido<br>";
        entrar=true;
    }

    /* Longitud de la contraseña */
    if(cont.trim().length<8 || cont.trim().length >16){
        mensajeMostrar += "La longitud de la contraseña debe ser entre 8 y 16 caracteres<br>";
        entrar = true;
    }

    if(rcont.trim().length<8 || rcont.trim().length >16){
        mensajeMostrar += "La longitud de la contraseña debe ser entre 8 y 16 caracteres<br>";
        entrar = true;
    }

    /* igualdad contraseñas */
    if(cont.value != rcont.value){
        mensajeMostrar += "Las contraseñas deben ser iguales<br>";
        entrar = true;
    }

    /* Longitud del nombre */
    if(nom.trim().length<4){
        mensajeMostrar += "La longitud del nombre no es correcta <br>";
        entrar = true;
    }

    if(!valnombre.test(nom)){
        mensajeMostrar +="En el nombre solo debes ingresar letras<br>";
        entrar=true;
    }

    /* Validar si es mayuscula la primera letra*/
    var letra = nom.charAt(0);
    if(!esMayuscula(letra)){
        mensajeMostrar +="la primera letra del nombre esta en minúscula<br>";
        entrar=true;
    }

    /* Longitud del apellido */
    if(ap.trim().length < 4 ){
        mensajeMostrar += "La longitud del apellido no es correcta <br>";
        entrar = true;
    }

    if(!valnombre.test(ap)){
        mensajeMostrar +="En el apellido solo debes ingresar letras<br>";
        entrar=true;
    }
    
    /* Validar si es mayuscula del apellido la primera letra*/
    var letra = ap.charAt(0);
        if(!esMayuscula(letra)){
        mensajeMostrar +="la primera letra del apellido esta en minúscula<br>";
        entrar=true;
    }

    //direccion
    var numer= /^[a-zA-Z\d?\s?]+\s?\W?\d+$/;
    if(!numer.test(direccion)){  
        mensajeMostrar +="Debe ingresar una direccion valida<br>";
        entrar=true;
    }
                
    if(comuna.trim().length<3){
        mensajeMostrar += "No existen comunas con solo 3 letras<br>";
        entrar=true;
    }

    if(!valnombre.test(comuna)){
        mensajeMostrar +="En la comuna solo debes ingresar letras<br>";
        entrar=true;
    }

    if(entrar){
        $("#mensaje").html(mensajeMostrar);
    }else{
        $("#mensaje").html("Datos actualizados correctamente");
    }
});

    function esMayuscula(letra){
        return letra == letra.toUpperCase();
    }

form2.addEventListener("submit" , a/* nombre, puede ser cualquiera*/  => {
    let mensajeMostrar1 ="";
    let entrar1 = false;

    /* Mostrar el mensaje en el HTML*/
    if(entrar1){
        msj1.innerHTML = mensajeMostrar1;
    }
    else{
        msj1.innerHTML = "Datos guardados correctamente";
    }
});


})