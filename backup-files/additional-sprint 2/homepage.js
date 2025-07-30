        document.addEventListener('DOMContentLoaded', () => {
            // Sample data for search (replace with backend data)
            const searchData = [
                { name: 'John Doe', role: 'Software Engineer', company: 'Google', domain: 'Tech' },
                { name: 'Jane Smith', role: 'Product Manager', company: 'Microsoft', domain: 'Tech' },
                { name: 'Alice Johnson', role: 'Data Scientist', company: 'Amazon', domain: 'Data' }
            ];

            const searchInput = document.querySelector('#searchInput');
            const clearSearch = document.querySelector('#clearSearch');
            const roleButtons = document.querySelectorAll('.role-btn');

            // Search functionality
            if (searchInput) {
                searchInput.addEventListener('input', () => {
                    const query = searchInput.value.toLowerCase();
                    clearSearch.classList.toggle('d-none', !query);
                    // Client-side filtering (replace with server-side logic if needed)
                    const results = searchData.filter(item =>
                        Object.values(item).some(value =>
                            value.toLowerCase().includes(query)
                        )
                    );
                    console.log('Search results:', results); // Replace with UI update (e.g., display results)
                });

                clearSearch.addEventListener('click', () => {
                    searchInput.value = '';
                    clearSearch.classList.add('d-none');
                    console.log('Search cleared'); // Reset UI if displaying results
                });
            }

            // Role button selection
            roleButtons.forEach(button => {
                button.addEventListener('click', () => {
                    roleButtons.forEach(btn => {
                        btn.classList.remove('selected-btn', 'selected-visitor-btn');
                    });
                    if (button.dataset.role === 'visitor') {
                        button.classList.add('selected-visitor-btn');
                    } else {
                        button.classList.add('selected-btn');
                    }
                    console.log(`Selected role: ${button.dataset.role}`); // Replace with navigation or action
                });
            });

            // Dark mode toggle
            const themeToggle = document.getElementById('themeToggle');
            themeToggle.addEventListener('click', () => {
                document.body.dataset.theme = document.body.dataset.theme === 'dark' ? 'light' : 'dark';
                themeToggle.innerHTML = document.body.dataset.theme === 'dark' ?
                    '<i class="bi bi-sun-fill"></i>' : '<i class="bi bi-moon-stars-fill"></i>';
            });
        });
