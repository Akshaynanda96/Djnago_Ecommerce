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

})

$(document).ready(function() {
    $('.btn-plus').click(function() {
        var button = $(this);
        var uuid = button.data('uuid');
        console.log(uuid);
        var quantityInput = $('.quantity-input');
        $.ajax({
            type:'GET',
            url: '/increment_quantity',
            data:{
                prod_id : uuid,  
            },
            success: function (data) {
                console.log(data);
                quantityInput.val(data.qty);
                $('#totalAmt').text('₹' + data.totalAmt.toFixed(2));
                $('#Subtotal').text('₹' + data.Subtotal.toFixed(2));
                $('#finalamount').text('₹' + data.finalAmount.toFixed(2));
                
     
            }
        })
        
    });
});



$(document).ready(function() {
    $('.btn-minus').click(function() {
        var button = $(this);
        var uuid = button.data('uuid');
        console.log(uuid);
        var quantityInput = $('.quantity-input');
        $.ajax({
            type:'GET',
            url: '/decrement_quantity',
            data:{
                prod_id : uuid,  
            },
            success: function (data) {
                console.log(data);
                quantityInput.val(data.qty);
                $('#totalAmt').text('₹' + data.totalAmt.toFixed(2));
                $('#Subtotal').text('₹' + data.Subtotal.toFixed(2));
                $('#finalamount').text('₹' + data.finalAmount.toFixed(2));
                
            }
        })
        
    });
});

$(document).ready(function() {
    $('.remove-item').click(function() {
        var button = $(this);
        var uuid = button.data('uuid');  
        
        $.ajax({
            type: 'GET',
            url: '/remove_to_cart/',
            data: {
                prod_id: uuid,
               
            },
            success: function(data) {
                $('#Subtotal').text('₹' + data.Subtotal.toFixed(2));
                $('#finalamount').text('₹' + data.finalAmount.toFixed(2));
                button.closest('tr').remove();
            },
            error: function(xhr, textStatus, errorThrown) {
                console.log('Error:', errorThrown);
            }
        });
    });
});


document.addEventListener('DOMContentLoaded', function() {
    // Find the checkout button element
    var checkoutButton = document.getElementById('checkoutButton');

    // Attach a click event listener to the checkout button
    checkoutButton.addEventListener('click', function(event) {
        // Find the checkbox element
        var checkbox = document.getElementById('flexCheckDefault');

        // Check if the checkbox is checked
        if (!checkbox.checked) {
            // Prevent the default action (following the link)
            event.preventDefault();

            // Alert the user
            alert('Please check the Default Address checkbox before proceeding to checkout.');
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var checkboxes = document.querySelectorAll('#price-1, #price-2, #price-3, #price-4, #price-5');

    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            if (this.checked) {
                // Submit the form automatically
                document.getElementById('price-filter-form').submit();
            }
        });
    });
});