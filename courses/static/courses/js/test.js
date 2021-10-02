// $(document).ready(function() {
//
//     var toggleAffix = function(affixElement, scrollElement, wrapper) {
//
//         var height = affixElement.outerHeight(),
//             top = wrapper.offset().top;
//
//         if (scrollElement.scrollTop() >= (top - height)){
//             wrapper.height(height);
//             affixElement.addClass("affix");
//         }
//         else {
//             affixElement.removeClass("affix");
//         }
//
//     };
//
//     $('[data-toggle="affix"]').each(function() {
//         var ele = $(this), wrapper = $('<div></div>');
//
//         ele.before(wrapper);
//         $(window).on('scroll resize', function() {
//             toggleAffix(ele, $(this), wrapper);
//         });
//
//         // init
//         toggleAffix(ele, $(window), wrapper);
//     });
//
// });

document.addEventListener("DOMContentLoaded", function(){

    var el_autohide = document.querySelector('.autohide');
    var nav = document.querySelector('nav')
    var bar = document.querySelector('.fa-bars')


    if(el_autohide){
        var last_scroll_top = 0;
        window.addEventListener('scroll', function() {
            let scroll_top = window.scrollY;

            if (scroll_top === 0){
                el_autohide.classList.remove('shadow-lg')
                el_autohide.style.backgroundColor = ''

            }
            else {
                el_autohide.style.backgroundColor = 'white'
                el_autohide.classList.add('shadow-lg')
            }

            if(scroll_top < last_scroll_top) {
                el_autohide.classList.remove('scrolled-down');
                el_autohide.classList.add('scrolled-up');
            }
            else {
                el_autohide.classList.remove('scrolled-up');
                el_autohide.classList.add('scrolled-down');

            }

            // console.log(last_scroll_top, scroll_top)

            last_scroll_top = scroll_top;


        });
        bar.addEventListener('click', function () {
            nav.classList.toggle('collapse-bg')
        })
    }
});