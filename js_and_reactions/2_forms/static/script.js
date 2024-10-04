$(document).ready(function() {
    $('#contactForm').on('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        const contactData = {
            name: $('#name').val(),
            email: $('#email').val(),
            message: $('#message').val()
        };

        $.ajax({
            url: '/submit',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(contactData),
            success: function(response) {
                $('#responseMessage').text(response.message).css('color', 'green');
                $('#contactForm')[0].reset();
            },
            error: function() {
                $('#responseMessage').text('An error occurred. Please try again.').css('color', 'red');
            }
        });
    });
});