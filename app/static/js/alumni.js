        document.addEventListener('DOMContentLoaded', () => {
            const table = document.querySelector('#alumniTable');
            const tbody = table.querySelector('tbody');
            const headers = table.querySelectorAll('.sort');
            const searchInput = document.querySelector('input[name="query"]');
            const loadingOverlay = document.querySelector('#loadingOverlay');
            let originalRows = Array.from(tbody.querySelectorAll('tr'));

            // Simulate loading state (remove in production if data is pre-loaded)
            setTimeout(() => {
                loadingOverlay.classList.remove('active');
            }, 1000);

            // Row selection
            tbody.addEventListener('click', (e) => {
                const row = e.target.closest('tr');
                if (row) {
                    row.classList.toggle('selected');
                    row.focus();
                }
            });

            tbody.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    e.target.classList.toggle('selected');
                }
            });

            // Sorting
            headers.forEach(header => {
                header.addEventListener('click', () => {
                    const sortKey = header.dataset.sort;
                    const isAsc = !header.classList.contains('asc');
                    headers.forEach(h => {
                        h.classList.remove('asc', 'desc');
                        h.setAttribute('aria-sort', 'none');
                        h.querySelector('.sort-icon').textContent = '';
                    });
                    header.classList.add(isAsc ? 'asc' : 'desc');
                    header.setAttribute('aria-sort', isAsc ? 'ascending' : 'descending');
                    sortTable(sortKey, isAsc);
                });
            });

            function sortTable(key, isAsc) {
                loadingOverlay.classList.add('active');
                const rows = Array.from(tbody.querySelectorAll('tr'));
                const index = ['sr-no', 'name', 'role', 'company', 'domain'].indexOf(key);
                rows.sort((a, b) => {
                    let aValue = a.children[index].textContent;
                    let bValue = b.children[index].textContent;
                    if (key === 'sr-no') {
                        aValue = parseInt(aValue);
                        bValue = parseInt(bValue);
                    }
                    return isAsc ? aValue.localeCompare(bValue) : bValue.localeCompare(aValue);
                });
                tbody.innerHTML = '';
                rows.forEach(row => tbody.appendChild(row));
                setTimeout(() => loadingOverlay.classList.remove('active'), 300);
            }

            // Search filtering
            if (searchInput) {
                searchInput.addEventListener('input', () => {
                    loadingOverlay.classList.add('active');
                    const query = searchInput.value.toLowerCase();
                    tbody.innerHTML = '';
                    const filteredRows = originalRows.filter(row => {
                        return Array.from(row.cells).some(cell =>
                            cell.textContent.toLowerCase().includes(query)
                        );
                    });
                    filteredRows.forEach(row => tbody.appendChild(row));
                    setTimeout(() => loadingOverlay.classList.remove('active'), 300);
                });
            }

            // Export to CSV
            document.getElementById('exportBtn').addEventListener('click', () => {
                const rows = Array.from(tbody.querySelectorAll('tr'));
                const headers = Array.from(table.querySelectorAll('th')).map(th => th.textContent.replace(/\s*\u2191|\u2193/g, '').trim());
                const csv = [
                    headers.join(','),
                    ...rows.map(row =>
                        Array.from(row.cells).map(cell => `"${cell.textContent.replace(/"/g, '""')}"`).join(',')
                    )
                ].join('\n');
                const blob = new Blob([csv], { type: 'text/csv' });
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'alumni-data.csv';
                a.click();
                URL.revokeObjectURL(url);
            });

            // Sidebar toggle
            const sidebar = document.getElementById('sidebar');
            const sidebarToggle = document.getElementById('sidebarToggle');
            const mainContent = document.querySelector('.main-content');
            sidebarToggle.addEventListener('click', () => {
                sidebar.classList.toggle('hidden');
                sidebar.classList.toggle('active');
                mainContent.classList.toggle('full');
            });

            // Dark mode toggle
            const themeToggle = document.getElementById('themeToggle');
            themeToggle.addEventListener('click', () => {
                document.body.dataset.theme = document.body.dataset.theme === 'dark' ? 'light' : 'dark';
                themeToggle.innerHTML = document.body.dataset.theme === 'dark' ?
                    '<i class="bi bi-sun-fill"></i>' : '<i class="bi bi-moon-stars-fill"></i>';
            });
        });
