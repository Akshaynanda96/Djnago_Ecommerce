(function ($) {
    "use strict";
    
    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Vendor carousel
    $('.vendor-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:2
            },
            576:{
                items:3
            },
            768:{
                items:4
            },
            992:{
                items:5
            },
            1200:{
                items:6
            }
        }
    });


    // Related carousel
    $('.related-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:2
            },
            768:{
                items:3
            },
            992:{
                items:4
            }
        }
    });


//     // Product Quantity
    $('.quantity button').on('click', function () {
        var button = $(this);
        var oldValue = button.parent().parent().find('input').val();
        if (button.hasClass('btn-plus')) {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            if (oldValue > 1) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 0;
            }
        }
        button.parent().parent().find('input').val(newVal);
    });
    
})(jQuery);

// -----------------cart------------------
    $(document).ready(function(){
        $('.btn-plus').click(function(){
            var uuid = $(this).data('uuid');
            console.log(uuid);
            
            $.ajax({
                type: "GET",
                url: "/pluscart",
                data: {
                    pro_id: uuid
                },
                success: function(data) {
                   
                    var qty = data.qty;
                    var subtotal = data.Subtotal;
                    var finalAmount = data.finalAmount;
                    var totalAmt = data.totalAmt;

                    // Update the respective elements
                    // Update quantity input
                    $('button[data-uuid="' + uuid + '"]').closest('.quantity').find('input').val(qty);

                    // Update Subtotal
                    $('#Subtotal').text('₹' + subtotal + '.00');

                    // Update final amount
                    $('#finalamount').text('₹' + finalAmount + '.00');

                    // Update total amount for specific product
                    $('#totalAmt-' + uuid).text('₹' + totalAmt + '.00');
                },
                error: function(error) {
                    console.error('Error:', error);
                }
            });
        });
    });
