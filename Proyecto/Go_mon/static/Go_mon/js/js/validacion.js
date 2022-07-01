$(document).ready(function(){
    $("#FormReg").submit(function(e){
        let mensajeMostrar = "";
        let entrar = false;

        var nom = $("#nomb").val();
        
        //nombre
        if(nom.trim().length<4){
            mensajeMostrar+= "El nombre debe contener mas de tres letras<br>";
            entrar=true;
        }
        
        var letra = nom.charAt(0);
        if(!esMayuscula(letra)){
            mensajeMostrar+="la primera letra del nombre esta en minúscula<br>";
            entrar=true;
            }


        var ap = $("#Ap").val();
        //p_apellido
        if($("#Ap").val().trim().length==0){
            mensajeMostrar+= "Debe ingresar el primer apellido<br>";
            entrar=true;
        }

        var letra = ap.charAt(0);
        if(!esMayuscula(letra)){
        mensajes +="la primera letra del apellido esta en minúscula<br>";
        entrar=true;
        }

        // telefono
        var telfo = $("#telefo").val();
        if(telfo.trim().length!=9){
            mensajeMostrar+="la longuitud del numero celular debe ser 9<br>";
            entrar=true;
        }

        var numeros = /^[0-9]+$/;
        if(!numeros.test(telfo)){  
            mensajeMostrar+="Solo se deben ingresar numeros en el telefono<br>";
            entrar=true;
        }
    
        // descripcion
        var desc = $("#descrip").val();
        desc = desc.replace (/\r?\n/g," ");
        desc = desc.replace (/[ ]+/g," ");
        desc = desc.replace (/^ /,"");
        desc = desc.replace (/ $/,"");
        desc = desc.split (" ");

        if(desc.length>81 || desc.length<20){
            mensajeMostrar+="la longuitud de la descripción debe ser mayor a 20 o igual a 80<br>";
            entrar=true;
        }

        //imagen
        var imagen = $("#Image").val();
        var imageRegex = /([^\s]+(?=\.(jpg|gif|png|JPG|GIF|PNG))\.\2)/gm;
        if(!imageRegex.test(imagen)){  
            mensajeMostrar+="la imagen debe tener formato png, jpg o gif<br>";
            entrar=true;
        }


        //video
        var video = $("#recording").val();
        var reg=/^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \?=.-]*)*\/?$/;   
        if(video.length==0){
            entrar=false;
        }else if (!reg.test(video)){  
            mensajeMostrar+="Debe ingresar una dirección o link de su video.<br>";
            entrar=true;
        }

        //fecha de nacimiento
        var anohoy = new Date();
        var year = anohoy.getFullYear();
        //transforma el valor en una fecha (usando la clase Date  DD/MM/AA) y obtén el valor del año con el método getFullYear().
        var naci = $("#nacim").val();
        var anonaci = new Date(naci).getFullYear();
        var date = new Date().toLocaleDateString('en-CA');
        if(naci>=date){
            mensajeMostrar+="la fecha de nacimiento debe ser anterior al dia de hoy.<br>";
            entrar=true;
        }else if (year-anonaci<18){
            mensajeMostrar+="Debes ser mayor de edad.<br>";
            entrar=true;
        }

        //Tarifa
        var precio = $("#tarifa").val();
        if(precio>10001 || precio<2999){
            mensajeMostrar+="El precio por hora no puede ser menor que 3000 o mayor a 10000 pesos.<br>";
            listo=true;
        }

        var numeros = /^[0-9]+$/;
        if(!numeros.test(precio)){  
            mensajeMostrar+="Solo se deben ingresar numeros en en tarifa<br>";
            entrar=true;
        }

        if(entrar){
            $("#mensaje").html(mensajeMostrar);
        }
        else{

        }
    });
})