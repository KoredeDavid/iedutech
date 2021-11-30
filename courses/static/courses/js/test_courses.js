// window.onscroll = function() {
//     // myFunction()
//     myFunction()
// };
//
//
//
//
//
//
// function myFunction() {
//     var bals = document.querySelector('#my').getBoundingClientRect().top
//     var got =  document.getElementById("my")
//
//     if (window.scrollY === elementOffset + 100){
//         got.classList.remove("enroll-card")
//         got.classList.add("fixed-enroll-card")
//     }
// }
//
// function wmyFunction(){
//     var bals = document.querySelector('#my').getBoundingClientRect().top
//     var got =  document.getElementById("my")
//     if (bals > -172)  {
//         got.classList.add("enroll-card")
//         got.classList.remove("fixed-enroll-card")
//     }
// }


window.onload = function (){
    window.onscroll = function(){
        function Utils() {

        }


        Utils.prototype = {
            constructor: Utils,
            isElementInView: function (element, fullyInView) {
                var pageTop = $(window).scrollTop();
                var pageBottom = pageTop + $(window).height();
                var elementTop = $(element).offset().top;
                var elementBottom = elementTop + $(element).height();

                if (fullyInView === true) {
                    return ((pageTop < elementTop) && (pageBottom > elementBottom));
                } else {
                    console.log(elementTop, pageBottom, elementBottom, pageTop)
                    if ($(element).hasClass('fixed-enroll-card')){
                        return pageTop === 0;
                    }else{
                        return ((elementTop <= pageBottom) && (elementBottom >= pageTop));
                    }
                }
            }
        };

        var Utils = new Utils();

        var isElementInView = Utils.isElementInView($('#fuck'), false);

        var got =  document.getElementById("fuck")
        if (!isElementInView) {
            got.classList.remove("enroll-card")
            got.classList.add("fixed-enroll-card")
            console.log('out of view');
        } else {
            got.classList.add("enroll-card")
            got.classList.remove("fixed-enroll-card")
            console.log('in view');
        }

    }

};

