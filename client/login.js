// Login

const form = document.querySelector('.login__form');

form.addEventListener('submit', event => {
  event.preventDefault(); // prevent the default form submission

  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  axios.post('scribble-ai-stack-sampledb-ackzejcb7nss.ci89jwbnuivr.us-east-1.rds.amazonaws.com/login', {
    user: username,
    password
  })
  .then(response => {
    // handle success response
    console.log(response.data);
    // redirect to the dashboard page
    window.location.href = './Dashboard.html';
  })
  .catch(error => {
    // handle error response
    console.log(error.response.data);
    // display an error message to the user
    const errorText = document.createElement('p');
    errorText.classList.add('error');
    errorText.textContent = error.response.data.message;
    form.appendChild(errorText);
  });
});
