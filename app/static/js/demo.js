var spinner;

var show_spinner = function(txt){
    txt = txt || '';
    $('#spin_overlay_text').html(txt);
    $('.spin_overlay').show();
}
var hide_spinner = function(){
    $('.spin_overlay').hide();
}

var ajx = function(url, delegate, message){
    show_spinner(message)
    $.ajax({
        url: url,
        method: 'GET',
        success: function(data , status){
            hide_spinner();
            console.log(data);
            if (delegate){
                delegate(data['data'])
            }
            $.notify(url, "success")
        },
        error: function(data, status){
            hide_spinner();
            $.notify(url, "error")
        }
    });
}

$(document).ready(function(){

    var opts = {
        lines: 13, // The number of lines to draw
        length: 28, // The length of each line
        width: 17, // The line thickness
        radius: 45, // The radius of the inner circle
        scale: 1, // Scales overall size of the spinner
        corners: 1, // Corner roundness (0..1)
        color: '#ffffff', // CSS color or array of colors
        fadeColor: 'transparent', // CSS color or array of colors
        speed: 1.5, // Rounds per second
        rotate: 0, // The rotation offset
        animation: 'spinner-line-fade-quick', // The CSS animation name for the lines
        direction: 1, // 1: clockwise, -1: counterclockwise
        zIndex: 2e9, // The z-index (defaults to 2000000000)
        className: 'spinner', // The CSS class to assign to the spinner
        top: '50%', // Top position relative to parent
        left: '50%', // Left position relative to parent
        shadow: '0 0 1px transparent', // Box-shadow for the lines
        position: 'absolute' // Element positioning
    };

    spinner = new Spinner(opts).spin();
    $('.spin_overlay')[0].appendChild(spinner.el);

    //init a countdown
    var newDateObj = new Date(new Date().getTime() + 5);
    $("#countdown_timer").countdown(newDateObj, function(event) {
        $(this).text(
            "Next window :" + event.strftime('%H:%M:%S')
        );
        if (event.offset.totalMinutes == 0){

        }
        else {
            $('#countdown_message').text("");
        }

        if (event.type == "finish"){
        }
    }).countdown("stop");

    $('#config_toggle').on('click', function(){
        if ($('#config_panel').css('top').replace('px', '') < 0){
            $('#full_overlay').fadeIn();
            $('#config_panel').css('top', '0px')
        }
        else{
            $('#config_panel').css('top', '-1500px')
            $('#full_overlay').fadeOut();
        }
    });


    $('#config_header').on('click', function(){
        $('#config_panel').css('top', '-1500px')
        $('#full_overlay').fadeOut();
    });
    $('#full_overlay').on('click', function(){
        $('#config_panel').css('top', '-1500px')
        $('#full_overlay').fadeOut();
    });
   

    $('.user_detail').on('click', function() {

        var user_id = $(this).attr('data-id')
        var url = "users/" + user_id;
        $.get(url, function(data) {

            $('#stepDialog .modal-content').html(data);
            $('#stepDialog').modal();

            $('#submit').click(function(event) {
                show_spinner('Saving')
                event.preventDefault();
                $.ajax({
                    url: url,
                    method: 'POST',
                    data: $('#stepForm').serialize(),
                    success: function(data, status, e) {
                        $('#stepDialog').modal('hide')
                        hide_spinner();
                    },
                    error: function(data, status, e) {
                        console.log('notok')
                        hide_spinner();
                        $('#stepDialog').modal('hide')
                    }
                });
            })

        });
    });
});

