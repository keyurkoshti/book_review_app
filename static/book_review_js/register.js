function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

document.getElementById('registerform').addEventListener("submit", async function(event) {
    event.preventDefault(); //stop refresh page

    const response = await fetch('/api/register/',{
        method : "POST",
        headers : {
            "content-type" : "application/json",
            "X-CSRFToken" : getCSRFToken()
        },
        body: JSON.stringify({
            username : document.getElementById('username').value,
            email: document.getElementById('email').value,
            password1: document.getElementById('password1').value,
            password2: document.getElementById('password2').value,
        })
    });

    const data = await response.json()

    if (response.ok){
        alert("registration successful");
        window.location.href = "/login/";
    }
    else {
        document.getElementById('error').innerText = data.error || "somthing went wrong";
    }
});