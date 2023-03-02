const copyBtn = document.querySelector('.copy_btn');
const blogContentElem = document.querySelector('.generated_blog_content p');

copyBtn.addEventListener('click', () => {
  navigator.clipboard.writeText(blogContentElem.textContent)
    .then(() => {
      alert('Blog copied to clipboard!');
    })
    .catch(() => {
      alert('Failed to copy blog to clipboard!');
    });
});