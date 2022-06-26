//nombre
//p_apellido
//s_apellido
//sexo (femenino, masculino)
//telefono
//correo 
//contraseña
//direccion
//comuna 

//usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
//nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
//password: /^.{4,12}$/, // 4 a 12 digitos.
//correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
//telefono: /^\d{7,14}$/ // 7 a 14 numeros.

$(document).ready(function(){
    $("#formu_1").submit(function(e){
        e.preventDefault();
        let mensajes ="";
        let entrar = false;
        var nom = $("#nombre").val();
        var ap = $("#p_apellido").val();

        //nombre
        if(nom.trim().length<4){
            mensajes += "El nombre debe contener mas de tres letras<br>";
            entrar=true;
        }

        var letra = nom.charAt(0);
        if(!esMayuscula(letra)){
        mensajes +="la primera letra del nombre esta en minúscula<br>";
        entrar=true;
        }

        //p_apellido
        if($("#p_apellido").val().trim().length==0){
            mensajes += "Debe ingresar el primer apellido<br>";
            entrar=true;
        }

        var letra = ap.charAt(0);
        if(!esMayuscula(letra)){
        mensajes +="la primera letra del apellido esta en minúscula<br>";
        entrar=true;
        }

        //s_apellido
        if($("#s_apellido").val().trim().length==0){
            mensajes += "Debe ingresar el segundo apellido<br>";
            entrar=true;
        }

        //correo
        if($("#email").val().trim().length==0){
            mensajes += "El email esta en blanco.<br>";
            entrar=true;
        }

        var correo= $("#email").val();
        var num = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;
        if(!num.test(correo)){  
            mensajes +="Debe ingresar un correo valido<br>";
            entrar=true;
        }
        
        //telefono
        var fono= $("#telefono").val();
        var numeros = /^[0-9]+$/;
        if(!numeros.test(fono)){  
            mensajes +="Solo se deben ingresar numeros en el telefono<br>";
            entrar=true;
        }

        if(fono.trim().length!=9){
            mensajes += "El telefono debe contener 9 numeros<br>";
            entrar=true;
        }

        //contraseña
        var pass= $("#password").val();
        if(pass.trim().length<8 || pass.trim().length >16){
            mensajes += "El largo de la contraseña debe ser mas que 8 y menos que 16 <br>";
            entrar=true;
        }

        //direccion
        var direc= $("#direccion").val();
        var numer= /^[a-zA-Z\d?\s?]+\s?\W?\d+$/;
        if(!numer.test(direc)){  
            mensajes +="Debe ingresar una direccion valida<br>";
            entrar=true;
        }

        //comuna 

        var com= $("#comuna").val();
        if(com.trim().length<3){
            mensajes += "No existen comunas con solo 3 letras<br>";
            entrar=true;
        }

        if(entrar){
            $("#mensaje").html(mensajes);
        }else{
            $("#mensaje").html("Datos actualizados correctamente");
        }

    });

    function esMayuscula(letra){
        return letra == letra.toUpperCase();
    }
})


