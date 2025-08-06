document.addEventListener('DOMContentLoaded', () => {
    // Find the search input field and the table body
    const searchInput = document.querySelector('input[name="query"]');
    const table = document.querySelector('#alumniTable');
    const tbody = table.querySelector('tbody');
    
    // Store all the original rows from the table
    const originalRows = Array.from(tbody.querySelectorAll('tr'));

    // Make sure the search input exists before adding an event listener
    if (searchInput) {
        // This function will run every time the user types in the search box
        searchInput.addEventListener('input', () => {
            const query = searchInput.value.toLowerCase();

            // Clear the table to show only the filtered results
            tbody.innerHTML = '';

            // Filter the original rows to find matches
            const filteredRows = originalRows.filter(row => {
                // Check if any cell in the row contains the search query
                return Array.from(row.cells).some(cell =>
                    cell.textContent.toLowerCase().includes(query)
                );
            });

            // Add the matching rows back to the table
            filteredRows.forEach(row => tbody.appendChild(row));
        });
    }
});
