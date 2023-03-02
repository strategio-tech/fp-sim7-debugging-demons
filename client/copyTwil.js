const copyBtn = document.querySelector('.twil_copy_btn');
const twilContentElem = document.querySelector('.generated_twil_content p');

copyBtn.addEventListener('click', () => {
  navigator.clipboard.writeText(twilContentElem.textContent)
    .then(() => {
      alert('TWIL copied to clipboard!');
    })
    .catch(() => {
      alert('Failed to copy TWIL to clipboard!');
    });
});