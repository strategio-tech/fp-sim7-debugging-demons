// Login

const form = document.querySelector('.login__form');

form.addEventListener('submit', event => {
  event.preventDefault(); // prevent the default form submission

  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  axios.post('http://scrib-samp-ao5viirvgl0i.eba-qnybmrjh.us-east-1.elasticbeanstalk.com/login', {
    user: username,
    password: password
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
    alert('There was an error, try again later');
  });
});
