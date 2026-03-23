CREATE DATABASE if NOT EXISTS Task_List;
USE Task_List;
CREATE TABLE IF NOT EXISTS tasks (
    Task_Id INT AUTO_INCREMENT PRIMARY KEY,
    task_name VARCHAR(255)
    task_description VARCHAR(255) NOT NULL,
    task_status ENUM('Unopened', 'In Progress', 'Completed') DEFAULT 'Unopened',
    Date_Created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    catagory VARCHAR(50) DEFAULT 'General',
    Due_Date DATE,
    Date_Completed TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);