$(".hamburger-menu").click(function () {
    $(".x-mark").toggleClass("nav-disable");
    $(this).toggleClass("nav-disable");
    $("nav").toggleClass("nav-disable nav-move");
});
$(".x-mark").click(function () {
    $(this).toggleClass("nav-disable");
    $(".hamburger-menu").toggleClass("nav-disable");
    $("nav").toggleClass("nav-disable nav-move");
});

$(document).ready(function(){
    $('.photo-ranking').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        // dots: true,
        // arrows: false,
        infinite: true,
        speed: 500,
        // fade: true,
        cssEase: 'linear'
    });
});
$(document).ready(function(){
    $('.thread-ranking').slick({
        slidesToShow: 2,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        // dots: true,
        // arrows: false,
        infinite: true,
        speed: 500,
        // fade: true,
        cssEase: 'linear'
    });
});
$(document).ready(function(){
    $('.mod-ranking').slick({
        slidesToShow: 2,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        // dots: true,
        // arrows: false,
        infinite: true,
        speed: 500,
        // fade: true,
        cssEase: 'linear'
    });
});