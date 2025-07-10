    document.addEventListener('DOMContentLoaded', function() {
        const form = document.querySelector('form');
        form.addEventListener('submit', function(event) {
            clearErrors();

            const name = document.getElementById('id_name').value.trim();
            const email = document.getElementById('id_email').value.trim();
            const phone = document.getElementById('id_phone').value.trim();
            const message = document.getElementById('id_message').value.trim();
            
            let hasError = false;
            
            if (name === "") {
                showError('id_name', 'Name is required.');
                hasError = true;
            }
            if (email === "") {
                showError('id_email', 'Email address is required.');
                hasError = true;
            } else if (!validateEmail(email)) {
                showError('id_email', 'Please enter a valid email address.');
                hasError = true;
            }
            if (phone === "") {
                showError('id_phone', 'Phone number is required.');
                hasError = true;
            } else if (!validatePhone(phone)) {
                showError('id_phone', 'Please enter a valid phone number (10 digits).');
                hasError = true;
            }
            if (message === "") {
                showError('id_message', 'Message is required.');
                hasError = true;
            }

            if (hasError) {
                event.preventDefault();
            }
        });

        function validateEmail(email) {
            const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return re.test(email);
        }

        function validatePhone(phone) {
            const re = /^\d{10}$/;
            return re.test(phone);
        }

        function showError(elementId, errorMessage) {
            const element = document.getElementById(elementId);
            const errorElement = document.createElement('div');
            errorElement.className = 'error-message';
            errorElement.style.color = 'red';
            errorElement.innerText = errorMessage;
            element.parentElement.appendChild(errorElement);
        }

        function clearErrors() {
            const errors = document.querySelectorAll('.error-message');
            errors.forEach(function(error) {
                error.remove();
            });
        }
    });
