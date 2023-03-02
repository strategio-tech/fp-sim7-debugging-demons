// Signup Page Functions

const form = document.querySelector('form');

form.addEventListener('submit', event => {
  event.preventDefault(); // prevent the default form submission
  
  //console.log("hello");

  const name = document.getElementById('name').value;
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;
  const adminPassword = document.getElementById('admin-password').value;

  axios.post('http://scribbleaiv2-env.eba-mep75nuh.us-east-1.elasticbeanstalk.com/signup', {
    name: name,
    user: username,
    password: password,
    admin_password: adminPassword
  })
  .then(response => {
    // handle success response
    console.log(response.data);
    // redirect to the dashboard page
    window.location.href = './Dashboard.html';
  })
  .catch(function (error) {
    // handle error response
    console.log(error.response.data);
    // display an error message to the user
    const errorText = document.createElement('p');
    errorText.classList.add('error');
    errorText.textContent = error.response.data.message;
    form.appendChild(errorText);
  });
});
