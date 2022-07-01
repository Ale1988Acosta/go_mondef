var regex = /[\w-\.]{2,}@[a-zA-Z0-9._-]+\.[\w-]{2,4}/;
var esp = /^[a-zA-Z\d?]+$/;
var conta = /^(?=.*\d)(?=.*[\u0021-\u002b\u003c-\u0040])(?=.*[A-Z])(?=.*[a-z])\S{8,16}$/;
var msj = document.getElementById("#mensaje");
var ruc = /^([0-9])+\-([kK0-9])+$/;

$(document).ready(function () {
    $("#reg").click(function (e) {
        var contra = $("#cont").val();
        var mail = $("#email").val();
        var rcont = $("#rcont").val();
        var run = $("#rut").val();
        let mensajeMostrar = "";
        let entrar = false;

        //validación del correo
        if (run == "" || !ruc.test(run)) {
            $("#mensajeN").fadeIn();
            return false;
        } else {
            $("#mensajeN").fadeOut();
        //validación del correo
        if (mail == "" || !regex.test(mail)) {
            $("#mensajeC").fadeIn();
            return false;
        } else {
            $("#mensajeC").fadeOut();

            if (contra == "" || !conta.test(contra)) {
                $("#mensajeLarg").fadeIn();
                return false;

            } else {
                $("#mensajeLarg").fadeOut();


                if (rcont == "" || contra != rcont) {
                    $("#mensajeIg").fadeIn();
                    return false;

                } else {
                    $("#mensajeIg").fadeOut();
                    onclick = $(location).attr('href', '');
                }
            }

        }}
    });
})