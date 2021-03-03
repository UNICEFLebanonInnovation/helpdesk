$(document).ready(function(){

    $('.search-filter').change(function(e){
        $('#changelist-search').submit();
    });

    $('.field-frequency').each(function(i, val){
        var item = $(this);
        var input = item.find('input');
        input.hide();
        var frequency = parseInt(input.val());

        for (i = 0; i < frequency; i++) {
          item.append('<div class="mb-2 mr-2 badge badge-dot badge-dot-lg badge-primary"></div>');
        }
    });

    $('.field-frequency').dblclick(function(e){
        var item = $(this);
        item.append('<div class="mb-2 mr-2 badge badge-dot badge-dot-lg badge-primary"></div>');
        var input = item.find('input');
        var frequency = parseInt(input.val());
        input.val(frequency + 1);
    });

});