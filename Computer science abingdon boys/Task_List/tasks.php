<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Task Manager</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>

    <h2>Task Manager</h2>

    <form method="POST" style="margin-bottom: 20px;">
        <input type="text" name="task_name" placeholder="Task Name (e.g. Homework)" required>
        <input type="text" name="description" placeholder="Full Description..." required>
        <button type="submit" name="add_task">Add Task</button>
    </form>

    <div style="display: flex; justify-content: space-between; align-items: center;">
        <h3>Current Tasks:</h3>
        <form method="POST" onsubmit="return confirm('Delete all completed tasks?');">
            <button type="submit" name="delete_completed" style="background-color: #e74c3c; color: white; border: none; padding: 8px; cursor: pointer; border-radius: 4px;">
                Clear Completed Tasks
            </button>
        </form>
    </div>

    <table border="1" cellpadding="10" style="border-collapse: collapse; width: 100%;">
        <thead>
            <tr style="background: #f4f4f4;">
                <th>Task Name</th>
                <th>Status</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($rows as $row): 
                $isCompleted = ($row['task_status'] === 'Completed');
            ?>
                <tr>
                    <td class="task-row <?= $isCompleted ? 'completed-text' : '' ?>">
                        <strong><?= htmlspecialchars($row['task_name']) ?></strong>
                        
                        <div class="description-popup">
                            <strong>Full Description:</strong><br>
                            <?= htmlspecialchars($row['task_description']) ?>
                        </div>
                    </td>
                    <td><?= htmlspecialchars($row['task_status']) ?></td>
                    <td>
                        <?php if (!$isCompleted): ?>
                            <form method="POST" style="display:inline;">
                                <input type="hidden" name="complete_id" value="<?= $row['Task_Id'] ?>">
                                <button type="submit">Done</button>
                            </form>
                        <?php else: ?>
                            ✅
                        <?php endif; ?>
                    </td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>