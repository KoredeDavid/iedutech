var loaded = true

function comments_api() {
    $.ajax({
        url: '/get-comments',
        data: {
            csrfmiddlewaretoken: Cookies.get('csrftoken'),
            video_id: $("#video_id").attr('value'),
            next_page_token: $("#next_page_token").attr('value')
        },
        type: 'post',
        dataType: 'json',
        beforeSend: function () {
            if (!loaded){
                $("#load_more").toggleClass("d-none")
                $(".spinner-border").toggleClass("d-none")
            }
        },
        success: function (data_) {
            var comments = data_.comments
            var next_page_token = data_.next_page_token
            comments.forEach(function (data, index) {
                $("#next_page_token").attr('value', next_page_token)
                var elements = `<img class="rounded-circle border border-warning shadow mr-2" alt="100x100" src="${data.authorProfileImageUrl}"/>`+
                `<p class="d-inline">
                    <a class="text-decoration-none text-dark font-weight-bold" href=${data.authorChannelUrl}> ${data.authorDisplayName} </a>
                 </p>`+
                `<p class="mt-2 text-break">${data.textDisplay}</p> <hr class="text-warning">`
                if (!loaded){
                    $("#load_more").removeClass("d-none")
                    $(".spinner-border").addClass("d-none")
                }
                $("#load_more").before(elements);
                $("#load_more").html('Load More')
            });
        },
        error: function(xhr, status, error) {
            $("#load_more").removeClass("d-none")
            $(".spinner-border").addClass("d-none")
            $("#load_more").html('Error!!!. Load Again')
        },
    });
    return false;
}

$(function() {
    comments_api()
    $('#load_more').click(function(){
        loaded = false
        comments_api()
    })
})