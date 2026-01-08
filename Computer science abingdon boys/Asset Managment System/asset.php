<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Asset Management System</title>
<style>
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  margin: 0;
  padding: 0;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #de3163;
  background-size: cover;
  color: #f5f5dc;
}

h1 {
  color: #d2b48c;
  text-align: center;
  margin-bottom: 20px;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.container {
  background-color: rgba(47, 79, 47, 0.95);
  border-radius: 12px;
  width: 320px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 20px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.6);
  margin-bottom: 15px;
}

.container input[type=text],
.container input[type=password],
.container input[type=email] {
  width: 90%;
  padding: 12px;
  margin: 8px 0;
  border: 1px solid #556b2f;
  border-radius: 5px;
  background-color: #3c5f3c;
  color: #f5f5dc;
  text-align: center;
}

button {
  background-color: #d2b48c;
  color: #1b2a1b;
  padding: 12px 0;
  margin: 10px 0 5px 0;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  width: 95%;
  font-size: 1em;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #c19a6b;
}

button.cancelbtn {
  background-color: #8b4513;
}

button.cancelbtn:hover {
  background-color: #5a2d0c;
}

label input[type=checkbox] {
  margin-right: 8px;
}

.psw a {
  color: #d2b48c;
  text-decoration: none;
}

.psw a:hover {
  text-decoration: underline;
}

#signupModal {
  display: none;
  position: fixed;
  z-index: 10;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0,0,0,0.7);
}

.modal-content {
  background-color: rgba(47, 79, 47, 0.95);
  margin: 10% auto;
  padding: 20px 25px;
  border-radius: 12px;
  width: 320px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.6);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
}

.modal-content input[type=text],
.modal-content input[type=password],
.modal-content input[type=email] {
  width: 90%;
  padding: 12px;
  margin: 8px 0;
  border: 1px solid #556b2f;
  border-radius: 5px;
  background-color: #3c5f3c;
  color: #f5f5dc;
  text-align: center;
}

.close {
  color: #d2b48c;
  position: absolute;
  top: 10px;
  right: 15px;
  font-size: 28px;
  font-weight: bold;
  cursor: pointer;
}

.close:hover {
  color: #c19a6b;
}
</style>
</head>
<body>

<form>
  <h1>Asset Management System</h1>

  <div class="container">
    <input type="text" placeholder="Username" name="uname" required>
    <input type="password" placeholder="Password" name="psw" required>
    <button type="submit">Login</button>
    <button type="button" onclick="openSignUp()">Sign Up</button>
    <label>
      <input type="checkbox" checked="checked" name="remember"> Remember me
    </label>
    <span class="psw">Forgot <a href="#">password?</a></span>
  </div>
</form> 

<div id="signupModal">
  <div class="modal-content">
    <span class="close" onclick="closeSignUp()">&times;</span>
    <h2>Create Account</h2>
    <input type="text" placeholder="Username" name="newuname" required>
    <input type="email" placeholder="Email" name="email" required>
    <input type="password" placeholder="Password" name="newpsw" required>
    <button type="submit">Sign Up</button>
  </div>
</div>

<script>
function openSignUp() {
  document.getElementById('signupModal').style.display = 'block';
}

function closeSignUp() {
  document.getElementById('signupModal').style.display = 'none';
}

window.onclick = function(event) {
  if (event.target == document.getElementById('signupModal')) {
    closeSignUp();
  }
}
</script>

</body>
</html>
