import random
from database import Database

class Admin:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.admin_id = f"A{random.randint(1000, 9999)}"

    @staticmethod
    def register(first_name, last_name, email, password):
        """Register a new admin with proper validation."""
        if len(password) < 8 or not any(c.isupper() for c in password) or \
           not any(c.islower() for c in password) or not any(c.isdigit() for c in password) or \
           not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
            raise ValueError("Password does not meet requirements")

        admin = Admin(first_name, last_name, email, password)
        admins = Database._load_data(Database.ADMIN_FILE)
        admins.append({
            "admin_id": admin.admin_id,
            "first_name": admin.first_name,
            "last_name": admin.last_name,
            "email": admin.email,
            "password": admin.password
        })
        Database._save_data(Database.ADMIN_FILE, admins)
        return admin

    def accept_or_deny_application(self, application_id, status):
        """Accept or deny a worker's job application."""
        applications = Database._load_data(Database.APPLICATION_FILE)
        workplaces = Database._load_data(Database.WORKPLACE_FILE)
        schedules = Database._load_data(Database.SCHEDULE_FILE)

        # Ensure schedules is a dictionary
        if not isinstance(schedules, dict):
            schedules = {}

        # Find the application by ID
        application = next((app for app in applications if app["application_id"] == application_id), None)
        if not application:
            print(f"No application found with ID {application_id}.")
            return

        # Update the application's status
        application["Status"] = status

        if status == "Accepted":
            # Find the corresponding workplace
            workplace = next((wp for wp in workplaces if wp["Workplace ID"] == application["Workplace ID"]), None)
            if workplace:
                if workplace["Positions"] > 0:
                    # Reduce available positions
                    workplace["Positions"] -= 1

                    # Assign a schedule to the worker
                    worker_id = application["Worker ID"]
                    schedules[worker_id] = {
                        "Workplace Name": workplace["Name"],
                        "Location": workplace.get("Location", "Not specified"),
                        "Time and Date": workplace.get("Time and Date", "Not specified"),
                        "Shift": workplace.get("Shifts", "Not specified")
                    }
                    print(f"Schedule assigned to Worker ID {worker_id}: {schedules[worker_id]}")
                    print(f"Application {application_id} accepted. Positions remaining: {workplace['Positions']}.")
                else:
                    print("No positions available to accept this application.")
                    application["Status"] = "Denied"
            else:
                print(f"No workplace found with ID {application['Workplace ID']}.")

        elif status == "Denied":
            print(f"Application {application_id} denied.")

        # Save updates back to the database
        Database._save_data(Database.APPLICATION_FILE, applications)
        Database._save_data(Database.WORKPLACE_FILE, workplaces)
        Database._save_data(Database.SCHEDULE_FILE, schedules)

