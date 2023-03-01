const form = document.querySelector("form");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const token = localStorage.getItem("token");
  const user = localStorage.getItem("user");

  const topic = form.topic.value;
  const keyPoints = [form.keyPoint1.value, form.keyPoint2.value, form.keyPoint3.value].filter(Boolean);

  axios.post("http://scribble-ai-stack-sampledb-ackzejcb7nss.ci89jwbnuivr.us-east-1.rds.amazonaws.com/prompt", {
    user,
    token,
    topic,
    key_points: keyPoints,
  })
    .then((response) => {
      console.log(response.data.completion);
      window.location.href = "./GeneratedBlog.html";
    })
    .catch((error) => {
      console.error(error);
    });
});
