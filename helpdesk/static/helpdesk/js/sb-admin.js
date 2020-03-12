(function($) {
  "use strict"; // Start of use strict

  // Toggle the side navigation
  $("#sidebarToggle").click(function(e) {
    e.preventDefault();
    $("body").toggleClass("sidebar-toggled");
    $(".sidebar").toggleClass("toggled");
  });

  $("#id_queue").change(function(e) {
    $("#id_report_type").val('');
    $("#id_sub_report_type").val('');
    reArrangeFields();
  });

  $("#id_report_type").change(function(e) {
    $("#id_sub_report_type").val('');
    reArrangeFields();
  });

  $("#id_sub_report_type").change(function(e) {
    reArrangeFields();
  });

  // Prevent the content wrapper from scrolling when the fixed side navigation hovered over
  $('body.fixed-nav .sidebar').on('mousewheel DOMMouseScroll wheel', function(e) {
    if ($window.width() > 768) {
      var e0 = e.originalEvent,
        delta = e0.wheelDelta || -e0.detail;
      this.scrollTop += (delta < 0 ? 1 : -1) * 30;
      e.preventDefault();
    }
  });

  // Scroll to top button appear
  $(document).scroll(function() {
    var scrollDistance = $(this).scrollTop();
    if (scrollDistance > 100) {
      $('.scroll-to-top').fadeIn();
    } else {
      $('.scroll-to-top').fadeOut();
    }
  });

  // Smooth scrolling using jQuery easing
  $(document).on('click', 'a.scroll-to-top', function(event) {
    var $anchor = $(this);
    $('html, body').stop().animate({
      scrollTop: ($($anchor.attr('href')).offset().top)
    }, 1000, 'easeInOutExpo');
    event.preventDefault();
  });

  reArrangeFields();

})(jQuery); // End of use strict


function reArrangeFields()
{
    var id_queue = $("#id_queue").val();
    var id_report_type = $("#id_report_type").val();
    var id_sub_report_type = $("#id_sub_report_type").val();

    console.log(id_queue);
    console.log(id_report_type);

    $("#id_report_type").parent().hide();
    $("#id_sub_report_type").parent().hide();
    $("#id_other_type").parent().hide();

    if(id_queue == '1') {
        $("#id_report_type").parent().show();
    }else {
        $("#id_report_type").parent().hide();
    }

    if(id_report_type == 'Report on Refusal of vaccination by a community or an institution') {
        $("#id_sub_report_type").parent().show();
    }else if(id_report_type == 'Misconceptions and rumors' || id_report_type == 'Other challenges or complaints') {
        $("#id_sub_report_type").parent().hide();
    }

    if(id_sub_report_type == 'Other/ specify') {
        $("#id_other_type").parent().show();
    }

}