-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 06, 2025 at 09:25 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `drw`
--

-- --------------------------------------------------------

--
-- Table structure for table `client`
--

CREATE TABLE `client` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `client_master`
--

CREATE TABLE `client_master` (
  `id` int(11) NOT NULL,
  `client_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone_no` varchar(20) DEFAULT NULL,
  `address` text DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `company_phone` varchar(20) DEFAULT NULL,
  `company_email` varchar(255) DEFAULT NULL,
  `status` enum('Active','Inactive') DEFAULT 'Active'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `client_master`
--

INSERT INTO `client_master` (`id`, `client_name`, `email`, `phone_no`, `address`, `company_name`, `company_phone`, `company_email`, `status`) VALUES
(1, 'Tech Solutions Pvt Ltd', 'info@techsolutions.com', '9876543210', 'Bengaluru, Karnataka', 'Tech Solutions Pvt Ltd', '0801234567', 'contact@techsolutions.com', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `company_master`
--

CREATE TABLE `company_master` (
  `id` int(11) NOT NULL,
  `person_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone_no` varchar(20) DEFAULT NULL,
  `address` text DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `company_phone` varchar(20) DEFAULT NULL,
  `company_email` varchar(255) DEFAULT NULL,
  `status` enum('Active','Inactive') DEFAULT 'Active'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `company_master`
--

INSERT INTO `company_master` (`id`, `person_name`, `email`, `phone_no`, `address`, `company_name`, `company_phone`, `company_email`, `status`) VALUES
(1, 'Rajesh Kumar', 'rajesh@infotech.com', '9876001111', 'Hyderabad, Telangana', 'InfoTech Networks', '04022446677', 'admin@infotech.com', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `department_master`
--

CREATE TABLE `department_master` (
  `id` int(11) NOT NULL,
  `department_name` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `department_master`
--

INSERT INTO `department_master` (`id`, `department_name`, `description`) VALUES
(1, 'Networking', 'Handles setup and maintenance of networking devices'),
(2, 'Security Systems', 'Handles CCTV and surveillance systems');

-- --------------------------------------------------------

--
-- Table structure for table `designation_master`
--

CREATE TABLE `designation_master` (
  `id` int(11) NOT NULL,
  `designation_name` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `designation_master`
--

INSERT INTO `designation_master` (`id`, `designation_name`, `description`) VALUES
(1, 'Manager', 'Handles team management and approvals'),
(2, 'Executive', 'Executes assigned technical tasks');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(50) NOT NULL,
  `status` varchar(20) NOT NULL DEFAULT 'Active',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employees`
--

INSERT INTO `employees` (`id`, `name`, `password`, `role`, `status`, `created_at`) VALUES
(1, 'simran', '12345', 'Manager', 'Active', '2025-09-06 12:02:18'),
(2, 'Arya', '123', 'Executive', 'Active', '2025-09-06 12:02:18'),
(3, 'Sadik', '123', 'Executive', 'Active', '2025-09-06 12:02:18'),
(4, 'Sarthak', '123', 'Executive', 'Active', '2025-09-06 12:02:18');

-- --------------------------------------------------------

--
-- Table structure for table `employee_master`
--

CREATE TABLE `employee_master` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `street` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `pincode` varchar(20) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `designation_id` int(11) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  `role` enum('Manager','Executive') DEFAULT NULL,
  `status` enum('Active','Inactive') DEFAULT 'Active'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee_master`
--

INSERT INTO `employee_master` (`id`, `name`, `email`, `password`, `street`, `city`, `pincode`, `state`, `designation_id`, `department_id`, `role`, `status`) VALUES
(1, 'simran', 'simran@gmail.com', '12345', '80 feet road', 'sangli', '416416', 'maharashtra', 101, 1001, 'Manager', 'Active'),
(2, 'Simran@28', 'arya123@gmail.com', '123', 'Main Street', 'Pune', '411001', 'Maharashtra', 2, 1, 'Executive', 'Active'),
(3, 'Sadik', 'sadik123@gmail.com', '123', 'MG Road', 'Mumbai', '400001', 'Maharashtra', 2, 2, 'Executive', 'Active'),
(4, 'Sarthak', 'sarthak@example.com', '123', 'Central Avenue', 'Nagpur', '440001', 'Maharashtra', 2, 2, 'Executive', 'Active'),
(5, 'Saniya', 'saniya.as1155@edunetmail.com', '123456', '100 feet road', 'Mumbai', '400001', 'Maharashtra', 2, 2, 'Executive', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `leave_master`
--

CREATE TABLE `leave_master` (
  `id` int(11) NOT NULL,
  `emp_id` int(11) NOT NULL,
  `leave_type_id` int(11) NOT NULL,
  `from_date` date DEFAULT NULL,
  `to_date` date DEFAULT NULL,
  `reason` text DEFAULT NULL,
  `status` enum('Pending','Approved','Rejected') DEFAULT 'Pending',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `leave_master`
--

INSERT INTO `leave_master` (`id`, `emp_id`, `leave_type_id`, `from_date`, `to_date`, `reason`, `status`, `created_at`) VALUES
(4, 2, 2, '2025-09-09', '2025-09-11', 'Personal Reason', 'Approved', '2025-09-06 18:57:23');

-- --------------------------------------------------------

--
-- Table structure for table `leave_type`
--

CREATE TABLE `leave_type` (
  `id` int(11) NOT NULL,
  `type_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `leave_type_master`
--

CREATE TABLE `leave_type_master` (
  `id` int(11) NOT NULL,
  `leave_type` varchar(100) DEFAULT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `leave_type_master`
--

INSERT INTO `leave_type_master` (`id`, `leave_type`, `description`) VALUES
(1, 'Work From Home', 'Leave for working remotely'),
(2, 'Emergency Leave', 'Unexpected emergency leave');

-- --------------------------------------------------------

--
-- Table structure for table `task`
--

CREATE TABLE `task` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `task`
--

INSERT INTO `task` (`id`, `name`) VALUES
(1, 'WiFi Setup Task'),
(2, 'CCTV Installation Task');

-- --------------------------------------------------------

--
-- Table structure for table `task_assignment`
--

CREATE TABLE `task_assignment` (
  `id` int(11) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `task_category_id` int(11) DEFAULT NULL,
  `assign_to` int(11) DEFAULT NULL,
  `date_assign` date DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  `status` enum('Pending','In Progress','Completed') DEFAULT 'Pending',
  `priority` enum('Low','Medium','High') DEFAULT 'Medium'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `task_assignment`
--

INSERT INTO `task_assignment` (`id`, `title`, `description`, `task_category_id`, `assign_to`, `date_assign`, `due_date`, `status`, `priority`) VALUES
(1, 'Install WiFi in Client Office', 'Setup enterprise-grade Wi-Fi for client', 1, 2, '2025-09-05', '2025-09-07', 'In Progress', 'High'),
(2, 'CCTV Installation at Client Site', 'Install and configure CCTV cameras', 2, 3, '2025-09-05', '2025-09-08', 'Pending', 'Medium'),
(3, 'Review Reports', 'Manager review of completed reports', 1, 1, '2025-09-05', '2025-09-06', 'Pending', 'Low');

-- --------------------------------------------------------

--
-- Table structure for table `task_category`
--

CREATE TABLE `task_category` (
  `id` int(11) NOT NULL,
  `category_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `task_category`
--

INSERT INTO `task_category` (`id`, `category_name`) VALUES
(1, 'WiFi Installation'),
(2, 'CCTV Setup');

-- --------------------------------------------------------

--
-- Table structure for table `task_category_master`
--

CREATE TABLE `task_category_master` (
  `id` int(11) NOT NULL,
  `category_name` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `task_category_master`
--

INSERT INTO `task_category_master` (`id`, `category_name`, `description`) VALUES
(1, 'WiFi Installation', 'Setup and configure Wi-Fi routers and access points'),
(2, 'CCTV Setup', 'Install and maintain CCTV systems'),
(3, 'Client Meetings', 'Sets overall sales objectives, develops long-term strategies, and leads the entire sales function to align with company goals and growth plans.');

-- --------------------------------------------------------

--
-- Table structure for table `work_report`
--

CREATE TABLE `work_report` (
  `id` int(11) NOT NULL,
  `emp_id` int(11) NOT NULL,
  `task_id` int(11) NOT NULL,
  `client_id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `description` text DEFAULT NULL,
  `work_photo` varchar(255) DEFAULT NULL,
  `date` date NOT NULL,
  `report_date` date DEFAULT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  `status` enum('Completed','Pending','Partial') DEFAULT 'Pending',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `work_report`
--

INSERT INTO `work_report` (`id`, `emp_id`, `task_id`, `client_id`, `category_id`, `description`, `work_photo`, `date`, `report_date`, `latitude`, `longitude`, `status`, `created_at`) VALUES
(1, 2, 1, 1, 1, 'Wi-Fi installed successfully', NULL, '2025-09-05', NULL, NULL, NULL, 'Completed', '2025-09-06 12:02:18'),
(2, 3, 2, 1, 2, 'CCTV installation started', NULL, '2025-09-05', NULL, NULL, NULL, 'Pending', '2025-09-06 12:02:18'),
(3, 1, 3, 1, 1, 'Manager reviewed installation reports', NULL, '2025-09-06', NULL, NULL, NULL, 'Partial', '2025-09-06 12:02:18'),
(6, 2, 1, 1, 1, 'WiFi install successfully ', NULL, '2025-09-07', NULL, NULL, NULL, 'Completed', '2025-09-06 18:51:11'),
(7, 2, 1, 1, 1, 'WiFi install successfully', NULL, '2025-09-07', NULL, NULL, NULL, 'Completed', '2025-09-06 18:56:19');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `client_master`
--
ALTER TABLE `client_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `company_master`
--
ALTER TABLE `company_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `department_master`
--
ALTER TABLE `department_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `designation_master`
--
ALTER TABLE `designation_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `employee_master`
--
ALTER TABLE `employee_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `leave_master`
--
ALTER TABLE `leave_master`
  ADD PRIMARY KEY (`id`),
  ADD KEY `emp_id` (`emp_id`),
  ADD KEY `leave_type_id` (`leave_type_id`);

--
-- Indexes for table `leave_type`
--
ALTER TABLE `leave_type`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `leave_type_master`
--
ALTER TABLE `leave_type_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `task`
--
ALTER TABLE `task`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `task_assignment`
--
ALTER TABLE `task_assignment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `task_category`
--
ALTER TABLE `task_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `task_category_master`
--
ALTER TABLE `task_category_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `work_report`
--
ALTER TABLE `work_report`
  ADD PRIMARY KEY (`id`),
  ADD KEY `emp_id` (`emp_id`),
  ADD KEY `task_id` (`task_id`),
  ADD KEY `client_id` (`client_id`),
  ADD KEY `category_id` (`category_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `client`
--
ALTER TABLE `client`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `client_master`
--
ALTER TABLE `client_master`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `company_master`
--
ALTER TABLE `company_master`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `department_master`
--
ALTER TABLE `department_master`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `designation_master`
--
ALTER TABLE `designation_master`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `employees`
--
ALTER TABLE `employees`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `employee_master`
--
ALTER TABLE `employee_master`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `leave_master`
--
ALTER TABLE `leave_master`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `leave_type`
--
ALTER TABLE `leave_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `leave_type_master`
--
ALTER TABLE `leave_type_master`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `task`
--
ALTER TABLE `task`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `task_assignment`
--
ALTER TABLE `task_assignment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `task_category`
--
ALTER TABLE `task_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `task_category_master`
--
ALTER TABLE `task_category_master`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `work_report`
--
ALTER TABLE `work_report`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `leave_master`
--
ALTER TABLE `leave_master`
  ADD CONSTRAINT `leave_master_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `employee_master` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `leave_master_ibfk_2` FOREIGN KEY (`leave_type_id`) REFERENCES `leave_type_master` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `work_report`
--
ALTER TABLE `work_report`
  ADD CONSTRAINT `work_report_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `employee_master` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `work_report_ibfk_2` FOREIGN KEY (`task_id`) REFERENCES `task_assignment` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `work_report_ibfk_3` FOREIGN KEY (`client_id`) REFERENCES `client_master` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `work_report_ibfk_4` FOREIGN KEY (`category_id`) REFERENCES `task_category` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
