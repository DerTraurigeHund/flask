document.getElementById("login_button").addEventListener("click", function() {
    document.querySelector(".login").style.display = "block";
    document.querySelector(".register_step2").style.display = "none";
    document.querySelector(".register").style.display = "none";
    document.querySelector(".submit").style.display = "block";
    document.getElementById("login_button").classList.add("active");
    document.getElementById("register_button").classList.remove("active");
});

document.getElementById("register_button").addEventListener("click", function() {
    document.querySelector(".register").style.display = "block";
    document.querySelector(".login").style.display = "none";
    document.querySelector(".register_step2").style.display = "none";
    document.querySelector(".submit").style.display = "block";
    document.getElementById("login_button").classList.remove("active");
    document.getElementById("register_button").classList.add("active");
});

document.getElementById("submit").addEventListener("click", function() {
    const password1 = document.getElementById("password_").value;
    const password2 = document.getElementById("password2").value;
    const email = document.getElementById("email").value;
    const username = document.getElementById("username_").value;
    const termsChecked = document.getElementById("GT&C").checked;

    if (document.querySelector(".register").style.display === "block") {
        if (password1 !== password2 || !password1 || !password2 || !email || !username) {
            document.getElementById("error").innerHTML = "One of the fields is empty or the passwords don't match"
            return;
        }
        if (!termsChecked) {
            document.getElementById("error").innerHTML = "You need to accept the terms and conditions"
            return;
        }
        document.querySelector(".register_step2").style.display = "block";
        document.querySelector(".register").style.display = "none";
        document.querySelector(".submit").style.display = "none";
        send_registration();
    } else {
        if (!document.getElementById("username").value || !document.getElementById("password").value) {
            document.getElementById("error").innerHTML = "One of the fields is empty"
            return;
        }
        send_login(document.getElementById("username").value, document.getElementById("password").value);
    }
});


function send_registration() {
    const username = document.getElementById("username_").value;
    const password = document.getElementById("password_").value;
    const email = document.getElementById("email").value;
    
    fetch('/api/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            password: password,
            email: email
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            send_login(username, password);
        } else {
            document.getElementById("error").innerHTML = data.message
        }
    })
}

function send_login(username, password) {
    fetch('/api/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            localStorage.setItem("username", username);
            localStorage.setItem("id", data.user_id);
            window.location.href = "/";
        } else {
            document.getElementById("error").innerHTML = data.message
        }
    })
}