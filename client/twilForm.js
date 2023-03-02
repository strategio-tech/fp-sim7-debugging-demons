const form = document.querySelector("form");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const token = localStorage.getItem("token");
  const user = localStorage.getItem("user");

  const keyPoints = [form.topic1.value, form.topic2.value, form.topic3.value].filter(Boolean);

  axios.post("/twil", {
    user,
    token,
    key_points: keyPoints,
  })
    .then((response) => {
      console.log(response.data.completion);
      const generatedTwilContent = response.data.completion;
      const urlParams = new URLSearchParams();
      urlParams.set("generatedTwilContent", generatedTwilContent);
      window.location.href = `./GeneratedTwil.html?${urlParams.toString()}`;
    })
    .catch((error) => {
      console.error(error);
    });
});