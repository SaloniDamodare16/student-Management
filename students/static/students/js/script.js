// ========================================
// PAGE LOADED
// ========================================

console.log("Student Management System loaded successfully.");


// ========================================
// SUCCESS MESSAGE POPUP
// ========================================

const message = document.querySelector('.message');

if (message) {

    alert(message.textContent.trim());

}


// ========================================
// DELETE CONFIRMATION
// ========================================

const deleteButtons =
    document.querySelectorAll('.delete-btn');


deleteButtons.forEach(function(button) {

    button.addEventListener('click', function(event) {

        const answer = confirm(
            'Are you sure you want to delete this student?'
        );

        if (!answer) {
            event.preventDefault();
        }

    });

});