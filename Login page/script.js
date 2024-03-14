let wrapper = document.querySelector(".wrapper");

let loginLink = document.querySelector(".login-link");
let registerLink = document.querySelector(".register-link");

let loginButton = document.querySelector(".login-popup");
let iconClose = document.querySelector(".icon-close");

registerLink.addEventListener("click", () => {
    wrapper.classList.add("active");
});

loginLink.addEventListener("click", () => {
    wrapper.classList.remove("active");
});

loginButton.addEventListener("click", () => {
    wrapper.classList.add("active-popup");
});

iconClose.addEventListener("click", () => {
    wrapper.classList.remove("active-popup");
});