// Function to include navbar in all pages
function includeNavbar() {
  const header = document.querySelector('header');
  if (header) {
    // Add header styles
    header.style.padding = '20px 50px';
    header.style.backgroundColor = '#1a242f';
    header.style.display = 'flex';
    header.style.justifyContent = 'space-between';
    header.style.alignItems = 'center';
    header.style.position = 'fixed';
    header.style.width = '100%';
    header.style.top = '0';
    header.style.zIndex = '1000';

    // Load navbar content
    fetch('navbar.html')
      .then(response => response.text())
      .then(data => {
        header.innerHTML = data;
      })
      .catch(error => console.error('Error loading navbar:', error));
  }
}

// Call the function when the page loads
document.addEventListener('DOMContentLoaded', includeNavbar); 