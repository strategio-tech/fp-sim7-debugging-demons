const form = document.querySelector("form");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const token = localStorage.getItem("token");
  const user = localStorage.getItem("user");

  const topic = form.topic.value;
  const keyPoints = [form.keyPoint1.value, form.keyPoint2.value, form.keyPoint3.value].filter(Boolean);

  axios.post("/prompt", {
    user,
    token,
    topic,
    key_points: keyPoints,
  })
    .then((response) => {
      console.log(response.data.completion);
      const generatedBlogContent = response.data.completion;
      const urlParams = new URLSearchParams();
      urlParams.set("generatedBlogContent", generatedBlogContent);
      window.location.href = `./GeneratedBlog.html?${urlParams.toString()}`;
    })
    .catch((error) => {
      console.error(error);
    });
});

