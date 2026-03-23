<?php
require_once 'templates/auth.php';
session_start();

if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true) {
    header("Location: login.php");
    exit;
}

$userId = $_SESSION['user_id'];
$status_msg = "";

// --- LOGIC: JOIN NEW TEAM VIA CODE ---
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['join_team'])) {
    $code = trim($_POST['join_code']);
    $stmt = $pdo->prepare("SELECT id, name FROM teams WHERE join_code = ?");
    $stmt->execute([$code]);
    $team = $stmt->fetch();

    if ($team) {
        // Create the link in the junction table
        $stmt = $pdo->prepare("INSERT IGNORE INTO user_teams (user_id, team_id) VALUES (?, ?)");
        if ($stmt->execute([$userId, $team['id']])) {
            $status_msg = "Successfully joined " . $team['name'] . "!";
        }
    } else {
        $status_msg = "Invalid Team Code.";
    }
}

// --- FETCH USER'S CURRENT TEAMS ---
$stmt = $pdo->prepare("
    SELECT t.id, t.name 
    FROM teams t 
    JOIN user_teams ut ON t.id = ut.team_id 
    WHERE ut.user_id = ?
");
$stmt->execute([$userId]);
$myTeams = $stmt->fetchAll(PDO::FETCH_ASSOC);
$myTeamNames = array_column($myTeams, 'name');
$isAdmin = in_array('Admin', $myTeamNames);

// --- ASSET ACTIONS (CLAIM/CONSUME/DELETE) ---
if (isset($_GET['claim']) && isset($_GET['id']) && isset($_GET['as_team'])) {
    if (in_array($_GET['as_team'], $myTeamNames) || $isAdmin) {
        $pdo->prepare("UPDATE assets SET status_team = ? WHERE id = ? AND status_team = 'Unassigned'")
            ->execute([$_GET['as_team'], $_GET['id']]);
    }
    header("Location: logged.php"); exit;
}

if (isset($_GET['consume']) && isset($_GET['id'])) {
    $stmt = $pdo->prepare("SELECT status_team FROM assets WHERE id = ?");
    $stmt->execute([$_GET['id']]);
    $asset = $stmt->fetch();
    if ($isAdmin || ($asset && in_array($asset['status_team'], $myTeamNames))) {
        $pdo->prepare("UPDATE assets SET quantity = GREATEST(0, quantity - 1) WHERE id = ? AND is_consumable = 1")->execute([$_GET['id']]);
    }
    header("Location: logged.php"); exit;
}

// --- LOGIC: ADD ASSET ---
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['add_asset'])) {
    $team = $_POST['target_team'];
    if (in_array($team, $myTeamNames) || ($isAdmin && $team === 'Unassigned')) {
        $stmt = $pdo->prepare("INSERT INTO assets (asset_name, serial_number, status_team, added_by, quantity, is_consumable) VALUES (?, ?, ?, ?, ?, ?)");
        $stmt->execute([$_POST['asset_name'], $_POST['serial_number'], $team, $userId, $_POST['quantity'], isset($_POST['is_consumable']) ? 1 : 0]);
    }
    header("Location: logged.php"); exit;
}

// --- FETCH ASSETS ---
$placeholders = count($myTeamNames) > 0 ? str_repeat('?,', count($myTeamNames) - 1) . '?' : "'#NONE#'";
$stmt = $pdo->prepare("SELECT * FROM assets ORDER BY (status_team IN ($placeholders)) DESC, status_team ASC, created_at DESC");
$stmt->execute(count($myTeamNames) > 0 ? $myTeamNames : []);
$assets = $stmt->fetchAll();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Inventory Portal</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'Poppins', sans-serif; background-color: #0f0f0f; color: #fff; padding: 40px 20px; }
        .container { max-width: 1200px; margin: auto; }
        header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255, 79, 135, 0.3); padding-bottom: 20px; margin-bottom: 30px; }
        
        /* Join Team Section */
        .join-box { background: rgba(255, 79, 135, 0.1); border: 1px solid #ff4f87; border-radius: 15px; padding: 15px; margin-bottom: 25px; display: flex; gap: 10px; align-items: center; }
        .join-box input { flex: 1; background: #000; border: 1px solid #333; color: #fff; padding: 10px; border-radius: 8px; }
        
        .asset-card { background: rgba(20, 20, 20, 0.6); border: 1px solid rgba(255, 79, 135, 0.3); border-radius: 20px; padding: 20px; }
        table { width: 100%; border-collapse: collapse; }
        th { text-align: left; color: #ff4f87; padding: 12px; font-size: 0.8rem; text-transform: uppercase; border-bottom: 1px solid #333; }
        td { padding: 12px; border-bottom: 1px solid #222; }
        
        .btn { padding: 10px 20px; border-radius: 10px; cursor: pointer; text-decoration: none; font-weight: 600; border: none; transition: 0.3s; }
        .btn-pink { background: #ff4f87; color: white; }
        .btn-pink:hover { background: #de3163; }
        .btn-sm { padding: 5px 10px; border-radius: 6px; font-size: 0.7rem; font-weight: bold; }
        
        .badge { padding: 4px 8px; border-radius: 5px; font-size: 0.7rem; background: #333; }
        .badge-mine { border: 1px solid #ff4f87; color: #ff4f87; }
        
        .claim-dropdown { position: relative; display: inline-block; }
        .dropdown-content { display: none; position: absolute; background: #1a1a1a; border: 1px solid #ff4f87; min-width: 160px; z-index: 10; border-radius: 8px; box-shadow: 0 10px 20px rgba(0,0,0,0.5); }
        .dropdown-content a { color: white; padding: 10px; text-decoration: none; display: block; font-size: 0.8rem; }
        .dropdown-content a:hover { background: #ff4f87; }
        .claim-dropdown:hover .dropdown-content { display: block; }

        #assetModal { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.8); justify-content: center; align-items: center; z-index: 1000;}
        .modal-body { background: #111; padding: 30px; border-radius: 20px; border: 1px solid #ff4f87; width: 400px; }
        input, select { background: #1a1a1a; border: 1px solid #333; color: #fff; padding: 10px; border-radius: 8px; width: 100%; margin-bottom: 10px;}
    </style>
</head>
<body>

<div class="container">
    <header>
        <div>
            <h1 style="color:#ff4f87;">Abingdon <span style="font-weight:200; opacity:0.5;">Inventory</span></h1>
            <p style="opacity:0.6;">Welcome, <strong><?php echo htmlspecialchars($_SESSION['username']); ?></strong></p>
        </div>
        <a href="logout.php" class="btn" style="border: 1px solid #ff4f87; color: #ff4f87;">Logout</a>
    </header>

    <form class="join-box" method="POST">
        <span style="font-size:0.9rem;">Join a Team:</span>
        <input type="text" name="join_code" placeholder="Enter Join Code: " required>
        <button type="submit" name="join_team" class="btn btn-pink">Join</button>
        <?php if($status_msg): ?>
            <span style="margin-left:10px; font-size:0.8rem; color:#ff4f87;"><?php echo $status_msg; ?></span>
        <?php endif; ?>
    </form>

    <div style="display:flex; gap:15px; margin-bottom: 20px;">
        <?php if(count($myTeams) > 0 || $isAdmin): ?>
            <button class="btn btn-pink" onclick="document.getElementById('assetModal').style.display='flex'">+ New Asset</button>
        <?php endif; ?>
        <input type="text" id="assetSearch" placeholder="Search resources..." style="margin:0; flex:1; background: rgba(20,20,20,0.6);">
    </div>

    <div class="asset-card">
        <table>
            <thead>
                <tr>
                    <th>Asset</th>
                    <th>Status / Owner</th>
                    <th>Stock</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody id="assetTable">
                <?php foreach($assets as $asset): ?>
                <?php $isMine = in_array($asset['status_team'], $myTeamNames); ?>
                <tr class="asset-row">
                    <td>
                        <strong><?php echo htmlspecialchars($asset['asset_name']); ?></strong><br>
                        <small style="opacity:0.4;"><?php echo htmlspecialchars($asset['serial_number']); ?></small>
                    </td>
                    <td>
                        <span class="badge <?php echo $isMine ? 'badge-mine' : ''; ?>">
                            <?php echo $asset['status_team']; ?>
                        </span>
                    </td>
                    <td><?php echo $asset['quantity']; ?></td>
                    <td>
                        <?php if($asset['status_team'] === 'Unassigned'): ?>
                            <?php if(count($myTeams) > 0): ?>
                                <div class="claim-dropdown">
                                    <button class="btn-sm btn-pink">Claim as...</button>
                                    <div class="dropdown-content">
                                        <?php foreach($myTeamNames as $tName): ?>
                                            <a href="?claim=1&id=<?php echo $asset['id']; ?>&as_team=<?php echo urlencode($tName); ?>">
                                                <?php echo $tName; ?>
                                            </a>
                                        <?php endforeach; ?>
                                    </div>
                                </div>
                            <?php else: ?>
                                <small style="opacity:0.3;">Join a team to claim</small>
                            <?php endif; ?>
                        <?php elseif($isMine || $isAdmin): ?>
                            <?php if($asset['is_consumable']): ?>
                                <a href="?consume=1&id=<?php echo $asset['id']; ?>" class="btn-sm btn-pink">Use 1</a>
                            <?php endif; ?>
                            <a href="?delete=<?php echo $asset['id']; ?>" style="color:#ff4f87; margin-left:10px;" onclick="return confirm('Delete?')"><i class="fa-solid fa-trash"></i></a>
                        <?php endif; ?>
                    </td>
                </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>
</div>

<div id="assetModal">
    <form class="modal-body" method="POST">
        <h2 style="color:#ff4f87; margin-bottom: 15px;">Add Asset</h2>
        <input type="text" name="asset_name" placeholder="Item Name" required>
        <input type="text" name="serial_number" placeholder="Serial / Tag">
        <input type="number" name="quantity" value="1" min="1">
        
        <label style="font-size:0.8rem; color:#aaa;">Assign to:</label>
        <select name="target_team">
            <?php if($isAdmin): ?><option value="Unassigned">Unassigned Pool</option><?php endif; ?>
            <?php foreach($myTeamNames as $tName): ?>
                <option value="<?php echo $tName; ?>"><?php echo $tName; ?></option>
            <?php endforeach; ?>
        </select>

        <label style="display:flex; align-items:center; gap:10px; font-size:0.8rem; margin-top:10px;">
            <input type="checkbox" name="is_consumable" style="width:auto; margin:0;" checked> Consumable?
        </label>

        <button type="submit" name="add_asset" class="btn btn-pink" style="width:100%; margin-top:20px;">Save Asset</button>
        <button type="button" class="btn" onclick="document.getElementById('assetModal').style.display='none'" style="width:100%; background:none; color:#aaa; margin-top:5px;">Cancel</button>
    </form>
</div>

<script>
    document.getElementById('assetSearch').addEventListener('input', function() {
        let term = this.value.toLowerCase();
        document.querySelectorAll('.asset-row').forEach(row => {
            row.style.display = row.innerText.toLowerCase().includes(term) ? "" : "none";
        });
    });
</script>

</body>
</html>