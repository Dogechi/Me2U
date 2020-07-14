function preparedDocument(){
    jQuery("form#search").submit(function(){
        text = jQuery("#id_q").val();
        if (text =="search" || text == "Search"){
            // pop up alert
            alert("Enter a search term");
            // halt submission of form
            return false
        }
    });

    jQuery("#submit_review").click(addProductReview);
    jQuery("#first_time").hide();
    jQuery("#first_time").click(slideToggleReviewForm);
    jQuery("#review_form").hide();
    jQuery("#add_review").click(slideToggleReviewForm);
    jQuery("#add_review").addClass('visible');
    jQuery("#cancel_review").click(slideToggleReviewForm);

    function slideToggleReviewForm(){
        jQuery("#add_review").slideToggle();
        jQuery("#review_form").slideToggle();
        jQuery("#first_time").slideToggle();


    };

      // toggles visibility of "write review" link
    // and the review form.




    function addProductReview(){
           console.log('we came here')
    // build an object of review data to submit

        var review = {
            title: jQuery("#id_title").val(),
            content: jQuery("#id_content").val(),
            rating: jQuery("#id_rating").val(),
            slug: jQuery("#id_slug").val()
        }
        console.log(review)


        jQuery.post("add/review/", review,
          function (response){
            console.log("we got the response here")
            console.log(response)

            jQuery("#review_errors").empty();
            // evaluate the successs parameter
            if(response.success == "True"){
                  console.log('success for sure is True')

                  // disable the submit button to prevent duplicates
                  jQuery("#submit_review").attr('disabled','disabled');
                  // if this is first review, get rid of "no reviews" text
                  jQuery("#no_reviews").empty()
                  // add a new review section
                  jQuery("#reviews").prepend(response.html).slideDown();
                  // Get response and style interval
                  new_review = jQuery("#reviews").children(":first");
                  console.log('first review', new_review)
                  new_review.addClass('new_review');
                  // hide the review review_form
                  jQuery("#review_form").slideToggle();
            }
            else{
                  console.log('we might as well end here')
                  // add the error text to the review_errors div
                  jQuery("#review_errors").append(response.html);
                }
          }, "json");
    }

    var token =  jQuery('input[name="csrfmiddlewaretoken"]').attr('value')

    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", token);
            }
        }
    });

    function statusBox(){
        jQuery('<div id="loading"> Loading...</div>')
        .prependTo("#main")
        .ajaxStart(function(){jQuery(this).show();})
        .ajaxStop(function(){jQuery(this).hide();})
    }



// Checkout form code
    var hideable_billing_form = $('.hideable_billing_form');
    var hideable_shipping_form = $('.hideable_shipping_form');
    var same_as_shipping = $('.same_as_shipping')


    var use_default_shipping = document.querySelector("input[name='use_default_shipping']");
    var use_default_billing = document.querySelector("input[name='use_default_billing']");


    var form = document.getElementById('same_billing_address');
    form.addEventListener('change', function(event){
      event.preventDefault();

      if (form.checked) {
          same_as_shipping.hide();
        } else {
          same_as_shipping.show();

        };
    });


    use_default_shipping.addEventListener('change', function(event) {
      event.preventDefault();

        if (use_default_shipping.checked) {
          hideable_shipping_form.hide();
        } else {
          hideable_shipping_form.show();
        };
    });

    // var form = document.getElementById('use_default_billing');
    // form.addEventListener('change', function(event) {

    use_default_billing.addEventListener('change', function(event) {
      event.preventDefault();

        if (use_default_billing.checked) {
          hideable_billing_form.hide();
        } else {
          hideable_billing_form.show();
        };
    });



}


jQuery(document).ready(preparedDocument)
statusBox()