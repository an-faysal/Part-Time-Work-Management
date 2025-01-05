Part-Time Worker Management System

Overview

The Part-Time Worker Management System is a Python-based console application designed to streamline the management of part-time workers. This project divides functionalities between two user roles: Admin and Worker, enabling efficient handling of job applications, workplace management, and scheduling.

Features

Admin Features
Register and log in as an admin.
Manage job applications:
View applications.
Accept or deny applications.
Create and edit workplaces:
Add new workplaces with attributes like shifts, hourly rates, and locations.
Generate summary reports.
Worker Features
Register and log in as a worker.
View available job opportunities.
Apply for jobs.
Check application status.
Access assigned work schedules.
Database
Uses JSON files for data persistence, ensuring simplicity and portability.
Data includes:
Admins
Workers
Workplaces
Job applications
Schedules
System Architecture

Classes:
Admin: Handles admin-specific tasks such as managing applications and workplaces.
Worker: Manages worker-specific functionalities like job application and schedule viewing.
Database: Provides utility functions for loading, saving, and managing data.
Data Flow:
Inputs from Admin/Worker → Database Operations → Outputs to Admin/Worker.
Installation

Clone the Repository:
git clone https://github.com/yourusername/part-time-worker-management-system.git
cd part-time-worker-management-system
Ensure Python is Installed:
The project requires Python 3.6+.
Install dependencies if needed (e.g., json and os are built-in).
Run the Application:
python main.py
Usage

Admin Workflow:
Register or log in as an admin.
Manage job applications, create workplaces, and generate reports.
Worker Workflow:
Register or log in as a worker.
View and apply for jobs, check application status, and view schedules.
