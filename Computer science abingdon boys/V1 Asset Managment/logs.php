<?php
require_once 'db_config.php';
session_start();

// Strict security: Only Admins allowed
if (!isset($_SESSION['loggedin']) || $_SESSION['team'] !== 'Admin') {
    header("Location: logged.php");
    exit;
}

// Fetch logs (most recent first)
$stmt = $pdo->query("SELECT * FROM logs ORDER BY created_at DESC LIMIT 200");
$logs = $stmt->fetchAll();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Audit Logs</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'Poppins', sans-serif; background-color: #0f0f0f; color: #fff; padding: 40px 20px; }
        .container { max-width: 1000px; margin: auto; }
        header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255, 79, 135, 0.3); padding-bottom: 20px; margin-bottom: 30px; }
        .log-card { background: rgba(20, 20, 20, 0.6); backdrop-filter: blur(20px); border: 1px solid rgba(255, 79, 135, 0.3); border-radius: 24px; padding: 25px; }
        table { width: 100%; border-collapse: collapse; }
        th { text-align: left; color: #ff4f87; padding: 15px; font-size: 0.8rem; text-transform: uppercase; }
        td { padding: 15px; border-bottom: 1px solid rgba(255,255,255,0.05); font-size: 0.9rem; }
        .action-tag { padding: 4px 8px; border-radius: 6px; font-weight: bold; font-size: 0.75rem; }
        .tag-claim { background: #ff4f87; color: white; }
        .tag-return { background: #aaa; color: black; }
        .tag-add { background: #00f2ff; color: black; }
        .btn-back { padding: 10px 20px; text-decoration: none; color: #ff4f87; border: 1px solid #ff4f87; border-radius: 12px; font-weight: 600; }
    </style>
</head>
<body>

<div class="container">
    <header>
        <h1 style="color:#ff4f87;">Audit Logs</h1>
        <a href="logged.php" class="btn-back"><i class="fa-solid fa-arrow-left"></i> Back to Inventory</a>
    </header>

    <div class="log-card">
        <table>
            <thead>
                <tr>
                    <th>Time</th>
                    <th>User</th>
                    <th>Team</th>
                    <th>Action</th>
                    <th>Asset</th>
                    <th>Qty</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach($logs as $log): ?>
                <tr>
                    <td style="opacity:0.6;"><?php echo date('M d, H:i', strtotime($log['created_at'])); ?></td>
                    <td><strong><?php echo htmlspecialchars($log['user_name']); ?></strong></td>
                    <td><span style="opacity:0.7; font-size:0.8rem;"><?php echo $log['team']; ?></span></td>
                    <td>
                        <span class="action-tag <?php 
                            echo strpos($log['action_type'], 'Claim') !== false ? 'tag-claim' : 
                                (strpos($log['action_type'], 'Add') !== false ? 'tag-add' : 'tag-return'); 
                        ?>">
                            <?php echo $log['action_type']; ?>
                        </span>
                    </td>
                    <td><?php echo htmlspecialchars($log['asset_name']); ?></td>
                    <td><strong><?php echo $log['quantity']; ?></strong></td>
                </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>
</div>
</body>
</html>