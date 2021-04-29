$(document).ready(function () {

    $('#contactData').click(function (e) {
        e.preventDefault();
        let fn = $('#id_full_name').val();
        let email = $('#id_email').val();
        let subject = $('#id_subject').val();
        let message = $('#id_message').val();
        let send_data = {
            full_name: fn,
            email: email,
            subject: subject,
            message: message
        }

        let send_url = "http://127.0.0.1:8000/contact";

        $.ajax({
            type: "post",
            url: send_url,
            data: send_data,
            success: function (response) {
                let mess = response.success
                Swal.fire({
                    icon: 'success',
                    title: 'sending ....',
                    text: mess,
                    timer: 2000

                })

                $('#myForm')[0].reset();

            },
            else: Swal.fire({
                icon: 'error',
                title: 'sending ....',
                text: 'please wait',
                isConfirmed: false

            })
        })

    });
});