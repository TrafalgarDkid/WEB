$(document).ready(function () {

    $("#Registrar").click(function () {

        let nombre = $("#nombre").val();
        let apellido = $("#apellido").val();
        let email = $("#email").val();
        let contraseña = $("#pass").val();
        let contraseñaa = $("#passw").val();

        console.log(nombre, apellido, email, contraseña, contraseñaa);
        let validacion = validartodo(nombre, apellido, email, contraseña, contraseñaa);
        if (validacion) {
            $("#validar").html("<div class='alert alert-success w-50 mx-auto text-center' >Registro exitoso!</div>");
            setTimeout(() => {
                $("#formulario").submit()
            }, 1500);

        }
    })

    function validartodo(nombre, apellido, email, contraseña, contraseñaa) {

        let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (String(nombre).length < 3 || String(nombre).length > 16) {
            $("#validar").html("<div class='alert alert-danger w-50 mx-auto text-center' >El nombre debe ser entre 3 y 16 caracteres.</div>");
        } else if (String(apellido).length < 3 || String(apellido).length > 16) {
            $("#validar").html("<div class='alert alert-danger w-50 mx-auto text-center' >El apellido debe ser entre 3 y 16 caracteres.</div>");

        } else if (!emailPattern.test(email)) {
            $("#validar").html("<div class='alert alert-danger w-50 mx-auto text-center' >El correo no es valido.</div>");

        } else if (String(contraseña).length < 8 || String(contraseña).length > 20) {
            $("#validar").html("<div class='alert alert-danger w-50 mx-auto text-center' >La contraseña debe ser entre 8 y 16 caracteres.</div>");
        } else if (String(contraseñaa) != String(contraseña)) {
            $("#validar").html("<div class='alert alert-danger w-50 mx-auto text-center' >La contraseña no coincide.</div>");
        }
        else {
            return true;
        }

    }

    $('#Ingresar').click(function () {
        let email = $('#email').val();
        let password = $('#pass').val();
        let emailGuardado = localStorage.getItem('email');
        let passGuardada = localStorage.getItem('password');
        if (email === emailGuardado && password === passGuardada) {
            $("#validar").html("<div class='alert alert-primary w-50 mx-auto text-center' >Ingresaste correctamente!</div>");
            setTimeout(() => {
                $("#formulario").submit()
            }, 1500);

        } else {
            $("#validar").html("<div class='alert alert-danger w-50 mx-auto text-center' >Correo o contraseña incorrectos.</div>");          
        }
    })

    $('#Enviar').click(function () {

    })
})
