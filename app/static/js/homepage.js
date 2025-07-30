document.addEventListener('DOMContentLoaded', function() {
    const roleButtons = document.querySelectorAll('.role-btn');
    const authModal = new bootstrap.Modal(document.getElementById('authModal'));
    const loginTitle = document.getElementById('loginTitle');
    const registerTitle = document.getElementById('registerTitle');
    const visitorSection = document.getElementById('visitorSection');
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');
    const themeToggle = document.getElementById('themeToggle');
    const clearSearch = document.getElementById('clearSearch');
    const searchInput = document.getElementById('searchInput');

    let selectedRole = null;

    // Role button click handler
    roleButtons.forEach(button => {
        button.addEventListener('click', function() {
            roleButtons.forEach(btn => {
                btn.classList.remove('selected-btn', 'selected-visitor-btn');
            });

            selectedRole = this.getAttribute('data-role');
            if (selectedRole === 'visitor') {
                this.classList.add('selected-visitor-btn');
                visitorSection.style.display = 'block';
                authModal.hide();
            } else {
                this.classList.add('selected-btn');
                visitorSection.style.display = 'none';
                loginTitle.textContent = `${selectedRole.charAt(0).toUpperCase() + selectedRole.slice(1)} Login`;
                registerTitle.textContent = `New User Registration`;
                authModal.show();
            }
        });
    });

    // Login form submission
    loginForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const email = document.getElementById('loginEmail').value;
        const password = document.getElementById('loginPassword').value;
        console.log(`Login attempt for ${selectedRole}:`, { email, password });
        // Add actual login logic here (e.g., API call)
        alert(`Login submitted for ${selectedRole} with email: ${email}`);
        authModal.hide();
    });

    // Registration form submission
    registerForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const name = document.getElementById('registerName').value;
        const email = document.getElementById('registerEmail').value;
        const password = document.getElementById('registerPassword').value;
        console.log(`Registration attempt for ${selectedRole}:`, { name, email, password });
        // Add actual registration logic here (e.g., API call)
        alert(`Registration submitted for ${selectedRole} with name: ${name}, email: ${email}`);
        authModal.hide();
    });

    // Theme toggle
    themeToggle.addEventListener('click', function() {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        if (currentTheme === 'dark') {
            document.documentElement.removeAttribute('data-theme');
            themeToggle.innerHTML = '<i class="bi bi-moon-stars-fill"></i>';
        } else {
            document.documentElement.setAttribute('data-theme', 'dark');
            themeToggle.innerHTML = '<i class="bi bi-sun-fill"></i>';
        }
    });

    // Search input handling
    searchInput.addEventListener('input', function() {
        clearSearch.classList.toggle('d-none', this.value === '');
    });

    clearSearch.addEventListener('click', function() {
        searchInput.value = '';
        clearSearch.classList.add('d-none');
        searchInput.focus();
    });
});