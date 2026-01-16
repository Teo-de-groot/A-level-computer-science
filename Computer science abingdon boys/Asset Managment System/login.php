<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Asset Management System</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
<style>
/* --- Core Setup --- */
*{box-sizing:border-box;margin:0;padding:0;}

body{
  min-height:100vh;
  display:flex;
  justify-content:center;
  align-items:center;
  font-family:'Poppins', sans-serif;
  padding:10px;
  background-color: #0f0f0f;
  /* Tech Grid Background */
  background-image: 
    linear-gradient(rgba(255, 79, 135, 0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 79, 135, 0.03) 1px, transparent 1px);
  background-size: 30px 30px;
  color:#ff4f87;
  transition: color 1s ease;
  position: relative;
  overflow: hidden;
}

/* --- Floating Orbs (Visual Interest) --- */
.orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  z-index: 0;
  opacity: 0.6;
  animation: float 10s infinite alternate ease-in-out;
}
.orb-1 {
  width: 300px;
  height: 300px;
  background: #ff4f87;
  top: -50px;
  left: -50px;
  animation-delay: 0s;
}
.orb-2 {
  width: 200px;
  height: 200px;
  background: #7b2cbf; /* Purple accent */
  bottom: -50px;
  right: -50px;
  animation-delay: -5s;
}

/* Float Animation */
@keyframes float {
  0% { transform: translate(0, 0) scale(1); }
  100% { transform: translate(30px, 50px) scale(1.1); }
}

/* --- Light Mode Overlay --- */
/* Now semi-transparent to let orbs show through slightly, creating a pastel vibe */
#gradientOverlay {
  position: fixed;
  inset: 0;
  z-index: 0; /* Above orbs, below container */
  background: linear-gradient(135deg, rgba(253, 226, 226, 0.9), rgba(255, 225, 240, 0.9));
  opacity: 0;
  transition: opacity 1.5s ease-in-out;
  pointer-events: none;
}
body.light-theme #gradientOverlay { opacity: 1; }

.page-title{
  position:fixed;
  top:30px;
  left:50%;
  transform:translateX(-50%);
  font-size:2.5rem;
  font-weight: 600;
  text-align:center;
  letter-spacing:1px;
  z-index: 10;
  
  /* Gradient Text */
  background: linear-gradient(to right, #ff4f87, #ff9068);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 0 15px rgba(255,79,135,0.3));
}

/* --- Glassmorphism Container --- */
.container, .modal-content{
  width:90%;
  max-width:450px;
  padding:40px 30px;
  
  /* Glass Effect Dark */
  background: rgba(20, 20, 20, 0.6);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  
  border: 1px solid rgba(255, 79, 135, 0.3);
  border-radius:24px;
  display:flex;
  flex-direction:column;
  align-items:center;
  position: relative; 
  z-index: 1;
  transition: border-color 1s ease, box-shadow 1s ease;
  box-shadow: 0 20px 50px rgba(0,0,0,0.5);
}

/* Glass Effect Light (Fade In) */
.container::before, .modal-content::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 24px;
  background: rgba(255, 255, 255, 0.4); /* Milky glass */
  backdrop-filter: blur(20px);
  opacity: 0;
  z-index: -1;
  transition: opacity 1.5s ease-in-out;
  border: 1px solid rgba(255, 255, 255, 0.6);
}

body.light-theme .container::before,
body.light-theme .modal-content::before { opacity: 1; }

body.light-theme .container,
body.light-theme .modal-content{
  border-color: transparent; /* Border handled by ::before in light mode */
  box-shadow: 0 20px 50px rgba(168, 114, 133, 0.2);
}

/* Ensure content is above the glass layers */
.container > *, .modal-content > * { position: relative; z-index: 2; }

/* --- Inputs --- */
input{
  width:100%;
  padding:16px;
  margin:10px 0;
  background: rgba(0, 0, 0, 0.4); /* Darker inner glass */
  border: 1px solid rgba(255, 79, 135, 0.3);
  border-radius:12px;
  color:#fff;
  text-align:left; /* Modern standard */
  padding-left: 20px;
  transition: all 0.3s ease;
  font-size:1rem;
}

body.light-theme input{
  background: rgba(255, 255, 255, 0.6);
  color:#333;
  border-color: rgba(222, 49, 99, 0.3);
}

input:focus{
  outline:none;
  border-color:#ff4f87;
  background: rgba(0, 0, 0, 0.8);
  box-shadow: 0 0 15px rgba(255,79,135,0.2);
  transform: scale(1.02);
}

body.light-theme input:focus{
  background: #fff;
  border-color: #de3163;
}

input::placeholder{color:rgba(255, 79, 135, 0.5);}
body.light-theme input::placeholder{color:rgba(222, 49, 99, 0.5);}

/* --- Buttons --- */
button{
  width:100%;
  padding:16px;
  margin-top:15px;
  background: linear-gradient(135deg, #ff4f87, #de3163);
  border:none;
  border-radius:12px;
  cursor:pointer;
  transition:all 0.3s ease;
  font-size:1.1rem;
  font-weight: 600;
  color: white;
  letter-spacing: 0.5px;
  box-shadow: 0 10px 20px rgba(255,79,135,0.3);
}
button:hover{
  transform: translateY(-3px);
  box-shadow: 0 15px 30px rgba(255,79,135,0.5);
  filter: brightness(1.1);
}
button[type="button"] {
  background: transparent;
  border: 2px solid rgba(255, 79, 135, 0.5);
  box-shadow: none;
  margin-top: 10px;
}
button[type="button"]:hover {
  background: rgba(255, 79, 135, 0.1);
  border-color: #ff4f87;
}

.error{display:none;color:#ff4f87;font-size:0.85em;margin-top:-5px;margin-bottom:10px;text-align:left;width:100%;padding-left:5px;}

.eye-toggle-container{
  position:absolute;
  right:16px;
  top:50%;
  transform:translateY(-50%);
  z-index: 10;
}
.eye-toggle{cursor:pointer;color:#ff4f87; opacity: 0.7; transition: 0.3s;}
.eye-toggle:hover{ opacity: 1; }

/* --- Modal --- */
#signupModal{
  display:none;
  position:fixed;
  inset:0;
  background:rgba(0,0,0,0.8); /* Darker overlay for focus */
  backdrop-filter: blur(5px);
  justify-content:center;
  align-items:center;
  padding:10px;
  z-index:100;
}
.modal-content{ position:relative; animation:pop 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.close{ position:absolute; top:15px; right:20px; font-size:24px; cursor:pointer; z-index: 10; color: #ff4f87; transition: 0.3s; }
.close:hover{ transform: rotate(90deg); color: #fff; }

/* --- Switch --- */
.theme-switch{ position:fixed; right:30px; bottom:30px; width:60px; height:30px; z-index:50; }
.theme-switch input{display:none;}
.track{
  width:100%; height:100%;
  background:rgba(255, 255, 255, 0.1);
  border: 1px solid #ff4f87;
  border-radius:30px;
  position:relative;
  cursor:pointer;
  backdrop-filter: blur(4px);
  transition: all 0.3s ease;
}
.knob{
  position:absolute; top:3px; left:3px; width:22px; height:22px;
  background:#ff4f87;
  border-radius:50%;
  display:flex; justify-content:center; align-items:center;
  font-size:12px; color:#111;
  transition: transform 0.5s cubic-bezier(0.68, -0.55, 0.27, 1.55), background 0.5s;
  box-shadow: 0 0 10px rgba(255,79,135,0.6);
}
body.light-theme .knob{ background:#fff; color: #ff4f87; }
input:checked + .track .knob{ transform: translateX(30px); }
input:checked + .track .knob i{ transform: rotate(360deg); } /* Full spin */
</style>
</head>
<body>

<div class="orb orb-1"></div>
<div class="orb orb-2"></div>

<div id="gradientOverlay"></div>

<h1 class="page-title">Abingdon</h1>

<label class="theme-switch">
  <input type="checkbox" id="themeToggle">
  <div class="track">
    <div class="knob">
      <i id="themeIcon" class="fa-solid fa-moon"></i>
    </div>
  </div>
</label>

<form class="container" onsubmit="return validateLogin()">
  <h2 style="margin-bottom:20px; color:inherit; font-weight:400;">AS Computer Science</h2>
  
  <input id="loginUser" placeholder="Username">
  <div class="error" id="loginUserError">Username required</div>

  <div style="position:relative;width:100%">
    <input id="loginPass" type="password" placeholder="Password">
    <span class="eye-toggle-container">
      <i class="fa-solid fa-eye-slash eye-toggle" onclick="togglePassword('loginPass',this)"></i>
    </span>
  </div>
  <div class="error" id="loginPassError">Password required</div>

  <button>Login</button>
  <button type="button" onclick="openSignUp()">Create Account</button>
</form>

<div id="signupModal">
  <form class="modal-content" onsubmit="return validateSignup()">
    <span class="close" onclick="closeSignUp()">&times;</span>
    <h2 style="text-align:center;margin-bottom:20px; color:inherit;">Join Us</h2>

    <input id="suUser" placeholder="Username">
    <div class="error" id="suUserError">Required</div>

    <input id="suEmail" placeholder="Email">
    <div class="error" id="suEmailError">Invalid email</div>

    <div style="position:relative;width:100%">
      <input id="suPass" type="password" placeholder="Password">
      <span class="eye-toggle-container">
        <i class="fa-solid fa-eye-slash eye-toggle" onclick="togglePassword('suPass',this)"></i>
      </span>
    </div>
    <div class="error" id="suPassError">Required</div>

    <button>Sign Up</button>
  </form>
</div>

<script>
const themeToggle=document.getElementById('themeToggle');
const themeIcon=document.getElementById('themeIcon');
const signupModal=document.getElementById('signupModal');
const loginUser=document.getElementById('loginUser');
const loginPass=document.getElementById('loginPass');
const suUser=document.getElementById('suUser');
const suEmail=document.getElementById('suEmail');
const suPass=document.getElementById('suPass');
const loginUserError=document.getElementById('loginUserError');
const loginPassError=document.getElementById('loginPassError');
const suUserError=document.getElementById('suUserError');
const suEmailError=document.getElementById('suEmailError');
const suPassError=document.getElementById('suPassError');

themeToggle.addEventListener('change', () => {
  document.body.classList.toggle('light-theme', themeToggle.checked);
  themeIcon.className = themeToggle.checked ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
});

function togglePassword(id,icon){
  const i=document.getElementById(id);
  i.type=i.type==='password'?'text':'password';
  icon.classList.toggle('fa-eye');
  icon.classList.toggle('fa-eye-slash');
}

function openSignUp(){signupModal.style.display='flex'}
function closeSignUp(){
  signupModal.style.display='none';
  [suUserError, suEmailError, suPassError].forEach(e => e.style.display='none');
  [suUser, suEmail, suPass].forEach(i => i.value='');
}

function validateLogin(){
  let v=true;
  if(!loginUser.value){loginUserError.style.display='block';v=false}else loginUserError.style.display='none';
  if(!loginPass.value){loginPassError.style.display='block';v=false}else loginPassError.style.display='none';
  return v;
}
function validateSignup(){
  let v=true;
  if(!suUser.value){suUserError.style.display='block';v=false}else suUserError.style.display='none';
  if(!suEmail.value.includes('@')){suEmailError.style.display='block';v=false}else suEmailError.style.display='none';
  if(!suPass.value){suPassError.style.display='block';v=false}else suPassError.style.display='none';
  return v;
}
</script>
</body>
</html>