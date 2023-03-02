const urlParams = new URLSearchParams(window.location.search);
const generatedBlogContent = urlParams.get("generatedBlogContent");
const generatedBlogContentElem = document.querySelector(".generated_blog_content p");
generatedBlogContentElem.textContent = generatedBlogContent;
