$('.dropdown-trigger').dropdown();


$(".alert").delay(4000).fadeOut(300, function() {
    $(this).alert('close');
//    MUSI ZASTĘPOWAĆ POPRZEDNI JEŻELI POPRZEDNI ISTNIEJE
});


$(document).ready(function() {
    $('.sidenav').sidenav();

    $('.fixed-action-btn').floatingActionButton();

    $('.modal').modal();

    $('select').formSelect();

    $('#selectArea').formSelect();

});


