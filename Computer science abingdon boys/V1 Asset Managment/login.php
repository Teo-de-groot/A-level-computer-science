<?php
require_once 'db_config.php';

# Security of Cookies
session_set_cookie_params([
    'lifetime' => 0,            
    'path' => '/',              
    'domain' => '',             
    'secure' => false,         
    'httponly' => true,         
    'samesite' => 'Strict'      
]);

session_start();

$php_error = ""; 
$signup_message = "";

if (isset($_SESSION['loggedin']) && $_SESSION['loggedin'] === true) {
    header("Location: logged.php");
    exit;
}

# --- LOGIN LOGIC ---
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['login_submit'])) {
    $username = trim($_POST['username'] ?? '');
    $password = $_POST['password'] ?? '';

    if (!empty($username) && !empty($password)) {
        $stmt = $pdo->prepare("SELECT * FROM users WHERE username = ?");
        $stmt->execute([$username]);
        $user = $stmt->fetch();

        if ($user && password_verify($password, $user['password_hash'])) {
            session_regenerate_id(true); 
            $_SESSION['loggedin'] = true;
            $_SESSION['username'] = $user['username'];
            $_SESSION['user_id'] = $user['id'];
            header("Location: logged.php");
            exit;
        } else {
            $php_error = "Invalid username or password.";
        }
    }
}

# --- SIGNUP LOGIC (Simplified for post-creation team joining) ---
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['signup_submit'])) {
    $user = trim($_POST['su_username'] ?? '');
    $email = filter_var(trim($_POST['su_email'] ?? ''), FILTER_SANITIZE_EMAIL);
    $pass = $_POST['su_password'] ?? '';

    if (!empty($user) && !empty($email) && !empty($pass)) {
        $hashed_pass = password_hash($pass, PASSWORD_DEFAULT);
        try {
            $stmt = $pdo->prepare("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)");
            $stmt->execute([$user, $email, $hashed_pass]);
            $signup_message = "Account created! Log in to join your teams.";
        } catch (PDOException $e) {
            $php_error = ($e->getCode() == 23000) ? "Username or email already exists." : "Signup failed.";
        }
    } else {
        $php_error = "Please fill in all fields.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Asset Managment</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
    <style>
        *{box-sizing:border-box;margin:0;padding:0;}
        body{min-height:100vh;display:flex;justify-content:center;align-items:center;font-family:'Poppins', sans-serif;padding:10px;background-color: #0f0f0f;background-image:linear-gradient(rgba(255, 79, 135, 0.03) 1px, transparent 1px),linear-gradient(90deg, rgba(255, 79, 135, 0.03) 1px, transparent 1px);background-size: 30px 30px;color:#ff4f87;position: relative;overflow: hidden;transition: background-color 0.4s;}
        
        #gradientOverlay {position: fixed; inset: 0; z-index: 0; background-image: linear-gradient(135deg, rgba(253, 226, 226, 0.95), rgba(255, 225, 240, 0.95)); opacity: 0; transition: opacity 0.5s ease-in-out; pointer-events: none;}
        body.light-theme #gradientOverlay { opacity: 1; }
        body.light-theme { color: #333; }

        .page-title{position:fixed; top:30px; left:50%; transform:translateX(-50%);font-size:2.5rem; font-weight: 600; text-align:center; letter-spacing:1px; z-index: 10;background: linear-gradient(to right, #ff4f87, #de3163);-webkit-background-clip: text; -webkit-text-fill-color: transparent;filter: drop-shadow(0 0 15px rgba(255,79,135,0.3));}
        
        .container, .modal-content{width:90%; max-width:450px; padding:40px 30px;background: rgba(20, 20, 20, 0.6);backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);border: 1px solid rgba(255, 79, 135, 0.3);border-radius:24px;display:flex; flex-direction:column; align-items:center;position: relative; z-index: 1;box-shadow: 0 20px 50px rgba(0,0,0,0.5);}
        body.light-theme .container, body.light-theme .modal-content{background: rgba(255, 255, 255, 0.7); border-color: rgba(0,0,0,0.1); color: #333;}
        
        input{width:100%; padding:16px; margin:10px 0;background: rgba(0, 0, 0, 0.4); border: 1px solid rgba(255, 79, 135, 0.3);border-radius:12px; color:#fff; transition: 0.3s; font-size:1rem; outline: none;}
        body.light-theme input{ background: #fff; color:#333; border-color: #ddd; }
        
        .password-container { width: 100%; position: relative; }
        .toggle-password { position: absolute; right: 15px; top: 50%; transform: translateY(-50%); cursor: pointer; color: rgba(255, 79, 135, 0.7); z-index: 2; }
        
        button{width:100%; padding:16px; margin-top:15px;background: linear-gradient(135deg, #ff4f87, #de3163);border:none; border-radius:12px; cursor:pointer; font-size:1.1rem; font-weight: 600; color: white; box-shadow: 0 10px 20px rgba(255,79,135,0.3);}
        button[type="button"] { background: transparent; border: 2px solid rgba(255, 79, 135, 0.5); color: #ff4f87; margin-top: 10px; box-shadow: none;}
        
        .server-error { background: rgba(255, 79, 135, 0.15); border: 1px solid #ff4f87; color: #ff4f87; padding: 10px; border-radius: 8px; width: 100%; text-align: center; margin-bottom: 15px; }
        .server-success { background: rgba(79, 255, 135, 0.15); border: 1px solid #4fff87; color: #4fff87; padding: 10px; border-radius: 8px; width: 100%; text-align: center; margin-bottom: 15px; }
        
        #signupModal{ display:none; position:fixed; inset:0; background:rgba(0,0,0,0.8); backdrop-filter: blur(5px); justify-content:center; align-items:center; z-index:100; }

        /* Theme Toggle Button */
        .theme-btn {
            position: fixed;
            right: 30px;
            bottom: 30px;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: rgba(255, 79, 135, 0.1);
            border: 1px solid #ff4f87;
            color: #ff4f87;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            z-index: 100;
            transition: 0.3s;
            box-shadow: 0 5px 15px rgba(255, 79, 135, 0.2);
        }
        .theme-btn:hover { transform: scale(1.1); background: #ff4f87; color: #fff; }
        body.light-theme .theme-btn { background: #fff; border-color: #ddd; color: #333; }
    </style>
</head>
<body>

<div class="orb orb-1"></div>
<div class="orb orb-2"></div>
<div id="gradientOverlay"></div>

<h1 class="page-title">Asset Managment</h1>

<div class="theme-btn" id="themeBtn">
    <i id="themeIcon" class="fa-solid fa-moon"></i>
</div>

<form class="container" method="POST">
    <h2 style="margin-bottom:20px; font-weight:400;">Login</h2>
    
    <?php if(!empty($php_error)): ?>
        <div class="server-error"><?php echo htmlspecialchars($php_error); ?></div>
    <?php endif; ?>

    <?php if(!empty($signup_message)): ?>
        <div class="server-success"><?php echo htmlspecialchars($signup_message); ?></div>
    <?php endif; ?>

    <input type="text" name="username" placeholder="Username" required>
    
    <div class="password-container">
        <input type="password" name="password" id="loginPass" placeholder="Password" required>
        <i class="fa-solid fa-eye-slash toggle-password" onclick="togglePassword('loginPass', this)"></i>
    </div>

    <button type="submit" name="login_submit">Login</button>
    <button type="button" onclick="document.getElementById('signupModal').style.display='flex'">Create Account</button>
</form>

<div id="signupModal">
    <form class="modal-content" method="POST">
        <h2 style="margin-bottom:10px;">Sign Up</h2>
        <p style="font-size: 0.8rem; opacity: 0.6; margin-bottom: 20px;"></p>
        
        <input name="su_username" placeholder="Username" required>
        <input name="su_email" type="email" placeholder="Email" required>
        
        <div class="password-container">
            <input name="su_password" type="password" id="signupPass" placeholder="Password" required>
            <i class="fa-solid fa-eye-slash toggle-password" onclick="togglePassword('signupPass', this)"></i>
        </div>

        <button type="submit" name="signup_submit">Create Account</button>
        <button type="button" onclick="document.getElementById('signupModal').style.display='none'">Cancel</button>
    </form>
</div>

<script>
const themeBtn = document.getElementById('themeBtn');
const themeIcon = document.getElementById('themeIcon');
const body = document.body;

function setTheme(theme) {
    if (theme === 'light') {
        body.classList.add('light-theme');
        themeIcon.classList.replace('fa-moon', 'fa-sun');
    } else {
        body.classList.remove('light-theme');
        themeIcon.classList.replace('fa-sun', 'fa-moon');
    }
}

// Check saved theme
const savedTheme = localStorage.getItem('theme') || 'dark';
setTheme(savedTheme);

themeBtn.addEventListener('click', () => {
    const isLight = body.classList.toggle('light-theme');
    const newTheme = isLight ? 'light' : 'dark';
    localStorage.setItem('theme', newTheme);
    setTheme(newTheme);
});

function togglePassword(inputId, icon) {
    const passwordInput = document.getElementById(inputId);
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        icon.classList.remove('fa-eye-slash');
        icon.classList.add('fa-eye');
    } else {
        passwordInput.type = 'password';
        icon.classList.remove('fa-eye');
        icon.classList.add('fa-eye-slash');
    }
}
</script>
</body>
</html>