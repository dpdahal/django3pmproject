$(document).ready(function () {
    function getEmployee() {
        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:8000/employee-get',
            success: function (response) {
                var data = response.employeeData;
                showEmployee(data);
            }
        })

    }

    getEmployee();

    function showEmployee(empData) {
        var outPut = ""
        empData.forEach((emp, key) => {
            outPut += `<tr>`;
            outPut += `<td>${++key}</td>`;
            outPut += `<td>${emp.full_name}</td>`;
            outPut += `<td>${emp.email}</td>`;
            outPut += `<td>${emp.phone}</td>`;
            outPut += `<td>${emp.address}</td>`;
            outPut += `<td>
                        <button class="editEmployee" data-id="${emp.id}">Edit</button>
                        <button class="deleteEmployee" data-id="${emp.id}">Delete</button>
                    </td>`;
            outPut += '</tr>'
        });

        $('#employeeList').html(outPut);

        $('.deleteEmployee').each((i, items) => {
            $(items).click(function () {
                deleteRecord(items)
            });
        })
        $('.editEmployee').each((i, items) => {
            $(items).click(function () {
                getByCriteria(items)
            });
        });
    }

    $('#addEmployee').click(function (e) {
        e.preventDefault();
        var criteria = $('#criteria').val();
        if (criteria == '') {
            var full_name = $('#full_name').val();
            var email = $('#email').val();
            var phone = $('#phone').val();
            var address = $('#address').val();
            var send_data = {
                full_name: full_name,
                email: email,
                phone: phone,
                address: address
            }
            insertEmployee(send_data);
        } else {
            var full_name = $('#full_name').val();
            var email = $('#email').val();
            var phone = $('#phone').val();
            var address = $('#address').val();
            var send_data = {
                full_name: full_name,
                email: email,
                phone: phone,
                address: address
            }
            updateEmployee(criteria, send_data);
        }

    });

    function insertEmployee(data) {
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        var sendUrl = 'http://127.0.0.1:8000/employee-insert'
        $.ajax({
            type: "POST",
            url: sendUrl,
            data: data,
            headers: {'X-CSRFToken': csrftoken},
            success: function (response) {
                var message = response.success;
                Swal.fire({
                    icon: 'success',
                    title: 'inserted ....',
                    text: message,
                    timer: 2000
                });
                $('#myForm')[0].reset();
                getEmployee();
            }
        })
    }


    function deleteRecord(criteria) {
        var id = $(criteria).data('id');
        var sendUrl = 'http://127.0.0.1:8000/employee-delete/' + id
        $.ajax({
            type: "GET",
            url: sendUrl,
            success: function (response) {
                var message = response.success;
                Swal.fire({
                    icon: 'success',
                    title: 'deleted ....',
                    text: message,
                    timer: 2000
                });
                getEmployee();
            }
        });
    }

    function getByCriteria(criteria) {
        var id = $(criteria).data('id');
        var sendUrl = 'http://127.0.0.1:8000/employee-edit/' + id
        $.ajax({
            type: "GET",
            url: sendUrl,
            success: function (response) {
                $('#criteria').val(response.id);
                var full_name = $('#full_name').val(response.full_name);
                var email = $('#email').val(response.email);
                var phone = $('#phone').val(response.phone);
                var address = $('#address').val(response.address);
                getEmployee();
            }
        });
    }

    function updateEmployee(id, data) {
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        var sendUrl = 'http://127.0.0.1:8000/employee-update/' + id;
        $.ajax({
            type: "POST",
            url: sendUrl,
            data: data,
            headers: {'X-CSRFToken': csrftoken},
            success: function (response) {
                var message = response.success;
                Swal.fire({
                    icon: 'success',
                    title: 'inserted ....',
                    text: message,
                    timer: 2000
                });
                $('#myForm')[0].reset();
                getEmployee();
            }
        })
    }
});