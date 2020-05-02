const loginForm = document.getElementById("login_form");

const loginButton = document.getElementById("login_form_submit");

const loginErrorMsg = document.getElementById("login_error_msg");

//Function called click (function verifies if username/password is correct if not displays the error msg)
loginButton.addEventListener("click", (e) => { // e is a mouse event (click of a mouse)
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    //Only for test purposes
    //Edit out after we add a database
    if (username === "Jesvian" && password === "Villarroel") {
        alert("You have successfully logged in.");
        location.reload();
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})