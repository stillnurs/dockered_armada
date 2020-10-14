const menuToggle = document.querySelector('#menu-togle');
const mobileNavContainer = document.querySelector('#mobile-nav');

menuToggle.onclick = function(){
    menuToggle.classList.toggle('menu-icon-active');
    mobileNavContainer.classList.toggle('mobile-nav--active');
}
$(document).ready(function(){
    $(".slider").slick({
      autoplay: true,
      autoplaySpeed: 5000,
        dots:true ,
        slidesToShow: 6,
        slidesToScroll: 5,
    responsive: [
        {
          breakpoint: 1024, 
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2
          }
        },
        {
            breakpoint: 780, 
            settings: {
              slidesToShow: 2,
              slidesToScroll: 2
            }
          },
        {
          breakpoint: 480, 
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
      ]
    })
    ;
});