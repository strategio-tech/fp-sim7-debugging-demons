// Select the logout button element
const logoutButton = document.querySelector('#logout');

// Attach click event listener to the logout button
logoutButton.addEventListener('click', event => {
  event.preventDefault(); // Prevent the link from redirecting
  logout(); // Call the logout function
});

// Logout function that clears the token and redirects to login page
function logout() {
  localStorage.removeItem('token'); // Clear the token from local storage
  window.location.href = './Login.html'; // Redirect to the login page
}
