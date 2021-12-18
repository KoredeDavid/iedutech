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
        } else {
            got.classList.add("enroll-card")
            got.classList.remove("fixed-enroll-card")
        }

    }


    var enroll = $('.enroll')
    var video_id = $('#video_id').attr('value')
    var loc = window.location
    var http = 'http://'
    if (loc.protocol == 'https:'){
        http = 'https://'
    }
    var endpoint = http + loc.host

    enroll.click(function(){
        $.ajax({
            url: `${endpoint}/enroll-course/${video_id}`,
            data: {
                csrfmiddlewaretoken: Cookies.get('csrftoken'),
            },
            type: 'post',
            dataType: 'json',
            beforeSend: function () {
                enroll.toggleClass("d-none")
                $(".spinner-border").toggleClass("d-none")
            },
            success: function (data) {
                $(".spinner-border").addClass("d-none")
                $(".go_to_course").removeClass("d-none")
            },
            error: function(xhr, status, error) {
                enroll.removeClass("d-none")
                $(".spinner-border").addClass("d-none")
                enroll.html('Error!!!. Load Again')
            }
        });
    });
};

