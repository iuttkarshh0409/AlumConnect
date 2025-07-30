// homepage.js

// References to buttons and sections
const studentBtn = document.getElementById('studentBtn');
const alumniBtn = document.getElementById('alumniBtn');
const visitorBtn = document.getElementById('visitorBtn');
const continueBtn = document.getElementById('continueBtn');
const selectionSection = document.getElementById('selectionSection');
const formsSection = document.getElementById('formsSection');
const visitorSection = document.getElementById('visitorSection');
const loginTitle = document.getElementById('loginTitle');
const registerTitle = document.getElementById('registerTitle');

let selectedType = null;

// Handle button selection
function clearSelection() {
  studentBtn.classList.remove('selected-btn');
  alumniBtn.classList.remove('selected-btn');
  visitorBtn.classList.remove('selected-visitor-btn');
}

// Event listeners for identity buttons
studentBtn.addEventListener('click', function() {
  selectedType = 'Student';
  clearSelection();
  studentBtn.classList.add('selected-btn');
  continueBtn.disabled = false;
});
alumniBtn.addEventListener('click', function() {
  selectedType = 'Alumni';
  clearSelection();
  alumniBtn.classList.add('selected-btn');
  continueBtn.disabled = false;
});
visitorBtn.addEventListener('click', function() {
  selectedType = 'Visitor';
  clearSelection();
  visitorBtn.classList.add('selected-visitor-btn');
  continueBtn.disabled = false;
});

// Continue button handler
continueBtn.addEventListener('click', function() {
  if (!selectedType) return;
  selectionSection.style.display = 'none';
  if (selectedType === 'Visitor') {
    visitorSection.style.display = '';
    formsSection.style.display = 'none';
  } else {
    formsSection.style.display = '';
    visitorSection.style.display = 'none';
    // Update Login/Registration titles accordingly
    loginTitle.textContent = selectedType + " Login";
    registerTitle.textContent = "New " + selectedType + " Registration";
  }
});
