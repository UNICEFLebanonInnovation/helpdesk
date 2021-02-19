
$(document).ready(function(){
    resizeTable();
    $(window).resize(function() {
        resizeTable();
    });

    $('.show-dependent').click(function(e){
        e.preventDefault();

        $('#person-dependents-body-content').empty("");
        $('#person-dependents-body-content').append("Loading...");
        $('#dependentModal').modal('show');

        $.ajax({
            type: "GET",
            url: $(this).attr('href'),
            cache: false,
            async: false,
            dataType: 'html',
            success: function (response) {
                $('#person-dependents-body-content').empty("");
                $('#person-dependents-body-content').append(response);
            },
            error: function(response) {
                console.log(response);
            }
        });
    });

    $('.show-absence').click(function(e){
//        e.preventDefault();
//        $('#person-absence-frame').html('');
//        $('#person-absence-frame').attr('src', '');
//        $('#person-absence-frame').attr('src', $(this).attr('href'));
//        $('#absenceModal').modal('show');

        e.preventDefault();

        $('#person-absences-body-content').empty("");
        $('#person-absences-body-content').append("Loading...");
        $('#absenceModal').modal('show');

        $.ajax({
            type: "GET",
            url: $(this).attr('href'),
            cache: false,
            async: false,
            dataType: 'html',
            success: function (response) {
                $('#person-absences-body-content').empty("");
                $('#person-absences-body-content').append(response);
            },
            error: function(response) {
                console.log(response);
            }
        });

    });

    $('.show-travel').click(function(e){
//        e.preventDefault();
//        $('#person-travels-frame').html('');
//        $('#person-travels-frame').attr('src', '');
//        $('#person-travels-frame').attr('src', $(this).attr('href'));
//        $('#travelModal').modal('show');

        e.preventDefault();

        $('#person-travels-body-content').empty("");
        $('#person-travels-body-content').append("Loading...");
        $('#travelModal').modal('show');

        $.ajax({
            type: "GET",
            url: $(this).attr('href'),
            cache: false,
            async: false,
            dataType: 'html',
            success: function (response) {
                $('#person-travels-body-content').empty("");
                $('#person-travels-body-content').append(response);
            },
            error: function(response) {
                console.log(response);
            }
        });
    });

    $('.download-report').click(function(e){
        e.preventDefault();
        var form = $(this).parent('form');
        var url = $(this).attr('href');
        $(form).attr('action', url);
        $(form).attr('target', '_blank');
        $(form).submit();
    });

    $('.filter-report').click(function(e){
        e.preventDefault();
        var form = $(this).parent('form');
        $(form).attr('action', '');
        $(form).removeAttr('target');
        $(form).submit();
    });


});

function resizeTable()
{
    var window_width = $(window).width();
    var left_menu_width = 400;
    if(window_width <= 1250){
        left_menu_width = 200;
    }
    if(window_width <= 990){
        left_menu_width = 100;
    }
    $('.table-responsive').css('max-width', $(window).width() - left_menu_width);
}