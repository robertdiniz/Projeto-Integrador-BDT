document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('return-page').addEventListener('click', function(event) {
        event.preventDefault();
        window.history.back();
    });
});