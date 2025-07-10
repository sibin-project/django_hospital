document.getElementById('bookingForm').addEventListener('submit', function(event) {
    let isValid = true;

    // Clear any previous error messages
    let errorElements = document.querySelectorAll('.error');
    errorElements.forEach(function(el) {
        el.textContent = '';
    });

    let name = document.getElementById('id_p_name').value;
    let phone = document.getElementById('id_p_phone').value;
    let email = document.getElementById('id_p_email').value;
    let doctor = document.getElementById('id_doc_name').value;
    let date = document.getElementById('id_booking_date').value;

    // Create error elements
    let nameError = document.createElement('span');
    let phoneError = document.createElement('span');
    let emailError = document.createElement('span');
    let doctorError = document.createElement('span');
    let dateError = document.createElement('span');

    // Assign class for error styling
    nameError.className = 'error';
    phoneError.className = 'error';
    emailError.className = 'error';
    doctorError.className = 'error';
    dateError.className = 'error';

    // Validation checks and attaching error messages
    if (!name) {
        nameError.textContent = 'Patient name is required.';
        document.getElementById('id_p_name').parentNode.appendChild(nameError);
        isValid = false;
    }

    if (!phone.match(/^\d{10}$/)) {
        phoneError.textContent = 'Phone number must be 10 digits.';
        document.getElementById('id_p_phone').parentNode.appendChild(phoneError);
        isValid = false;
    }

    if (!email.match(/^[^@\s]+@[^@\s]+\.[^@\s]+$/)) {
        emailError.textContent = 'Invalid email address.';
        document.getElementById('id_p_email').parentNode.appendChild(emailError);
        isValid = false;
    }

    if (!doctor) {
        doctorError.textContent = 'Doctor selection is required.';
        document.getElementById('id_doc_name').parentNode.appendChild(doctorError);
        isValid = false;
    }

    if (!date) {
        dateError.textContent = 'Booking date is required.';
        document.getElementById('id_booking_date').parentNode.appendChild(dateError);
        isValid = false;
    }

    if (!isValid) {
        event.preventDefault();
    }
});
