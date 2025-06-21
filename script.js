document.addEventListener('DOMContentLoaded', () => {
    const searchIcon = document.querySelector('.search-icon');
    const searchContainer = document.querySelector('.search-bar-container');
    const searchInput = document.querySelector('.search-input');

    // Toggle search bar
    searchIcon.addEventListener('click', (e) => {
        e.preventDefault();
        searchContainer.classList.toggle('active');
        if (searchContainer.classList.contains('active')) {
            searchInput.focus();
        }
    });

    // Close search when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.search-bar-container') && 
            !e.target.closest('.search-icon')) {
            searchContainer.classList.remove('active');
        }
    });

    // Close on escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            searchContainer.classList.remove('active');
        }
    });

    // Existing search functionality (keep this)
    let searchTimeout;
    searchInput.addEventListener('input', (e) => {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            const searchTerm = e.target.value.trim().toLowerCase();
            const filtered = movies.filter(movie =>
                movie.title.toLowerCase().includes(searchTerm)
            );
            renderMovies(filtered.length > 0 ? filtered : movies);
        }, 300);
    });
});