const urlParams = new URLSearchParams(window.location.search);
const generatedTwilContent = urlParams.get("generatedTwilContent");
const generatedTwilContentElem = document.querySelector(".generated_twil_content p");
generatedTwilContentElem.textContent = generatedTwilContent;