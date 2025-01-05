import random  # Import the random module
from admin import Admin
from worker import Worker
from database import Database


def admin_menu(admin):
    while True:
        print("\nAdmin Menu:")
        print("1. View Applications")
        print("2. Accept/Deny Application")
        print("3. Create Workplace")
        print("4. Edit Workplace")
        print("5. Generate Reports")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            applications = Database._load_data(Database.APPLICATION_FILE)
            if not applications:
                print("No applications found.")
            else:
                for app in applications:
                    print(
                        f"Application ID: {app['application_id']}, Worker ID: {app['Worker ID']}, Workplace ID: {app['Workplace ID']}, Status: {app['Status']}")

        elif choice == "2":
            application_id = input("Enter Application ID to accept/deny: ")
            status = input("Enter status (Accepted/Denied): ")
            admin.accept_or_deny_application(application_id, status)

        elif choice == "3":
            name = input("Enter workplace name: ")
            work_type = input("Enter work type: ")
            shifts = input("Enter available shifts (Morning/Evening): ")
            time_date = input("Enter time and date: ")
            hourly_rate = float(input("Enter hourly rate: "))
            evening_incentive = float(input("Enter evening incentive: "))
            positions = int(input("Enter number of available positions: "))
            location = input("Enter workplace location: ")

            workplace = {
                "Workplace ID": f"W{random.randint(1000, 9999)}",
                "Name": name,
                "Type": work_type,
                "Shifts": shifts,
                "Time and Date": time_date,
                "Hourly Rate": hourly_rate,
                "Evening Incentive": evening_incentive,
                "Positions": positions,
                "Location": location
            }

            workplaces = Database._load_data(Database.WORKPLACE_FILE)
            workplaces.append(workplace)
            Database._save_data(Database.WORKPLACE_FILE, workplaces)
            print(f"Workplace created successfully with ID {workplace['Workplace ID']}.")

        elif choice == "4":
            workplaces = Database._load_data(Database.WORKPLACE_FILE)
            for wp in workplaces:
                print(f"ID: {wp['Workplace ID']}, Name: {wp['Name']}")

            workplace_id = input("Enter Workplace ID to edit: ")
            updates = {}
            for key in ["Name", "Type", "Shifts", "Time and Date", "Hourly Rate", "Evening Incentive", "Positions",
                        "Location"]:
                value = input(f"Enter new {key} (leave blank to skip): ")
                if value:
                    updates[key] = value

            for workplace in workplaces:
                if workplace["Workplace ID"] == workplace_id:
                    workplace.update(updates)
                    break
            Database._save_data(Database.WORKPLACE_FILE, workplaces)
            print("Workplace updated successfully.")

        elif choice == "5":
            report = Database.generate_summary_report()
            for key, value in report.items():
                print(f"{key}: {value}")

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")


def worker_menu(worker):
    while True:
        print("\nWorker Menu:")
        print("1. View Available Jobs")
        print("2. Apply for a Job")
        print("3. View Application Status")
        print("4. View Messages")
        print("5. View Work Schedule")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            worker.view_available_jobs()

        elif choice == "2":
            workplace_id = input("Enter Workplace ID to apply for: ")
            worker.apply_for_job(workplace_id)

        elif choice == "3":
            statuses = worker.view_application_status()
            if not statuses:
                print("No applications found.")
            else:
                for status in statuses:
                    print(f"Workplace ID: {status['Workplace ID']}, Status: {status['Status']}")

        elif choice == "4":
            worker.messaging_system()

        elif choice == "5":
            worker.part_time_work_schedule()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    while True:
        print("\nMain Menu:")
        print("1. Admin Login")
        print("2. Worker Login")
        print("3. Admin Registration")
        print("4. Worker Registration")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            email = input("Enter admin email: ")
            password = input("Enter admin password: ")

            admins = Database._load_data(Database.ADMIN_FILE)
            admin_data = next((a for a in admins if a["email"] == email and a["password"] == password), None)

            if admin_data:
                logged_in_admin = Admin(
                    first_name=admin_data["first_name"],
                    last_name=admin_data["last_name"],
                    email=admin_data["email"],
                    password=admin_data["password"]
                )
                logged_in_admin.admin_id = admin_data["admin_id"]
                admin_menu(logged_in_admin)
            else:
                print("Invalid credentials.")

        elif choice == "2":
            email = input("Enter worker email: ")
            password = input("Enter worker password: ")

            workers = Database._load_data(Database.WORKER_FILE)
            worker_data = next((w for w in workers if w["email"] == email and w["password"] == password), None)

            if worker_data:
                logged_in_worker = Worker(
                    first_name=worker_data["first_name"],
                    last_name=worker_data["last_name"],
                    email=worker_data["email"],
                    password=worker_data["password"]
                )
                logged_in_worker.worker_id = worker_data["worker_id"]
                worker_menu(logged_in_worker)
            else:
                print("Invalid credentials.")

        elif choice == "3":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            password = input(
                "Enter password (min 8 characters, including uppercase, lowercase, digit, special character): ")

            try:
                admin = Admin.register(first_name, last_name, email, password)
                print(f"Admin registered successfully with ID {admin.admin_id}.")
            except ValueError as e:
                print(f"Error during registration: {e}")

        elif choice == "4":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            password = input(
                "Enter password (min 8 characters, including uppercase, lowercase, digit, special character): ")

            try:
                worker = Worker.register(first_name, last_name, email, password)
                print(f"Worker registered successfully with ID {worker.worker_id}.")
            except ValueError as e:
                print(f"Error during registration: {e}")

        elif choice == "5":
            break


if __name__ == "__main__":
    main()
