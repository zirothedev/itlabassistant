document.addEventListener('DOMContentLoaded', function() {
    // Handle click on calendar entries
    document.querySelectorAll('.day li').forEach(item => {
        item.addEventListener('click', function() {
            const entryId = this.dataset.id;
            window.location.href = `/calendar/entry/${entryId}/`;
        });
    });
});