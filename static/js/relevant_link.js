$(document).ready(function () {

    $('#result_list .field-relevant_link').each(function (i, val) {
        var item = $(this);
        updateRelevantLink(item);
    });

});


function updateRelevantLink(item) {
    var link = item.html();
    item.html('<a href="' + link + '" target="_blank">' + link + '</a>');
}

