

$(document).ready(function() {

    $('.search-filter').change(function (e) {
        $('#changelist-search').submit();
    });

    $('.field-frequency').each(function (i, val) {
        var item = $(this);
        var input = item.find('input');
        input.hide();
        var frequency = parseInt(input.val());

        for (i = 0; i < frequency; i++) {
            add_badge(item, i);
        }
    });

    $('.field-frequency').dblclick(function (e) {
        var item = $(this);
        var input = item.find('input');
        var frequency = parseInt(input.val());
        input.val(frequency + 1);
        add_badge(item, frequency);
    });

    $(document).on('click', '.close', function(){
        $("#feedbackModal").hide();
    });
    $(document).on('click', '.btn-close', function(){
        $("#feedbackModal").hide();
    });

    $(document).on('click', '.btn-save', function(){
        var record_id= $('#record_id').val();
        var feedback_text= $('#feedback_text').val();
        var feedback_status = $("input[name='status_options']:checked").val();
        var feedback_color='';
        if (feedback_status=='not started')
        {
            feedback_color='grey';
        }
        else if (feedback_status=='initiated')
        {
            feedback_color='yellow';
        }
        else
        {
            feedback_color='green';
        }

        requestHeaders = getHeader();
        requestHeaders["content-type"] = 'application/x-www-form-urlencoded';

        $.ajax({
            type: "POST",
            url: '/survey/feedback-update-view/',
            data:{
                record_id:record_id,
                feedback_text:feedback_text,
                feedback_status: feedback_status,
                feedback_color: feedback_color
            },
            cache: false,
            async: false,
            headers: requestHeaders,
            dataType: 'json',
            success: function (response) {

                if(response.result)
                {
                    var item= "#feedback"+record_id;
                    $(item).css("background-color", feedback_color);
                    $("#feedbackModal").hide();
                }
                else
                {
                    alert("error saving the feedback ");
                }

                console.log(response);
                },
                error: function(response) {
                    console.log(response);
                }

    });


    });

    if (isTrackerDetailsPage()) {
        $('.field-relevant_link').each(function (i, val) {
            var item = $(this);
            updateRelevantLink(item);
        });

        $('.field-source_relevant_link').each(function (i, val) {
            var item = $(this);
            updateRelevantLink(item);
        });
    }

    relocateAddButton();
    relocateSaveButton();

});

function showFeedbackPopup(recordID)
{
    $('#record_id').val(recordID);
    requestHeaders = getHeader();
    requestHeaders["content-type"] = 'application/x-www-form-urlencoded';

    $.ajax({
        type: "POST",
        url: '/survey/feedback-select-view/',
        data:{
            record_id:recordID
        },
        cache: false,
        async: false,
        headers: requestHeaders,
        dataType: 'json',
        success: function (response) {
            if(response.result)
            {
                feedback = response;
                feedback_status = feedback.feedback_status;
                feedback_text = feedback.feedback_text;
                feedback_color = feedback.feedback_color;
                can_edit = feedback.can_edit;

                if (can_edit)
                {
                    $(':input[type="button"][name="feedback_save"]').prop('disabled', false);

                }
                else
                {
                    $(':input[type="button"][name="feedback_save"]').prop('disabled', true);

                }

                $("input[name='status_options'][value='"+feedback_status+"']").prop('checked', true);
                $('#feedback_text').val(feedback_text);
                $('#record_id').val(recordID);
            }

            console.log(response);
            },
            error: function(response) {
                console.log(response);
            }

    });
    $("#feedbackModal").show();
}

function relocateAddButton()
{

    if (isTrackerDetailsPage())
    {
        var originalButton = $(".object-tools");
        var buttonParent = originalButton.parent();
        var newButton = originalButton.clone();

        newButton.addClass( "upper-add-button");
        newButton.prependTo(buttonParent);
        originalButton.css('visibility', 'hidden');
    }


}

function isTrackerDetailsPage()
{

    var url_loc = window.location.toString();

    return (url_loc.toLowerCase().search(/^.*\/survey\/knowledgetracker(\/*)(\?.*)?$/i)>=0);

}

function relocateSaveButton() {
    if (isTrackerDetailsPage()) {
        $("input[name='_save']").addClass("lower-save-button");
    }
}


function updateRelevantLink(item)
{
    var link =item.html();
    item.html('<a href="'+link+'" target="_blank">'+link+'</a>');
}



function add_badge(item, frequency){

    var badge_info = '<div class="mb-2 mr-2 badge badge-dot badge-dot-lg badge-info"></div>';
    var badge_primary = '<div class="mb-2 mr-2 badge badge-dot badge-dot-lg badge-primary"></div>';
    var badge_warning = '<div class="mb-2 mr-2 badge badge-dot badge-dot-lg badge-warning"></div>';
    var badge_danger = '<div class="mb-2 mr-2 badge badge-dot badge-dot-lg badge-danger"></div>';


        var badge = ''
        if(frequency > 0 && frequency <= 4) {
            badge = badge_info;
        }
        if(frequency > 4 && frequency <= 8) {
            badge = badge_primary;
        }
        if(frequency > 8 && frequency <= 12) {
            badge = badge_warning;
        }
        if(frequency > 12) {
            badge = badge_danger;
        }

        console.log(frequency);
        console.log(badge);
        item.append(badge);
}

function getHeader()
 {

     var csrfHeader = $("[name=csrfmiddlewaretoken]").val();

     var header = {
         // 'Authorization': 'Token '+user_token,
         // 'HTTP_REFERER': href_full_path,
         // 'Cookie': 'token=Token '+user_token,
         'X-CSRFToken': csrfHeader
     };

     return header;
}

