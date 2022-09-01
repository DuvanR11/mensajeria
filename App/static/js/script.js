/* --------------------------
SCRIPTS PARA TODA LA PAGINA
-----------------------------*/

// 1) funcion cuando pulsa el texto
$(document).ready(function(){
    (function pulse() {
        $('.text-pulse').fadeOut(1000).fadeIn(1000, pulse);

    })();
})

//2) Funcion para mostrar la contraseña
function myFunction(params) {
    let p = document.getElementById("password")
    if(p.type === "password"){
        p.type = 'text';
    }else{
        p.type = 'password';
    }
}