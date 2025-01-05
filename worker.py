import random
from database import Database


class Worker:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.worker_id = f"E{random.randint(1000, 9999)}"

    @staticmethod
    def register(first_name, last_name, email, password):
        """Register a new worker with proper validation."""
        if len(password) < 8 or not any(c.isupper() for c in password) or \
                not any(c.islower() for c in password) or not any(c.isdigit() for c in password) or \
                not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
            raise ValueError("Password does not meet requirements")

        worker = Worker(first_name, last_name, email, password)

        workers = Database._load_data(Database.WORKER_FILE)
        workers.append({
            "worker_id": worker.worker_id,
            "first_name": worker.first_name,
            "last_name": worker.last_name,
            "email": worker.email,
            "password": worker.password
        })
        Database._save_data(Database.WORKER_FILE, workers)

        return worker

    def view_available_jobs(self):
        """Display all available jobs."""
        workplaces = Database._load_data(Database.WORKPLACE_FILE)

        if not workplaces:
            print("No jobs available.")
            return

        for workplace in workplaces:
            print(f"Workplace ID: {workplace['Workplace ID']}")
            print(f"Name: {workplace['Name']}")
            print(f"Type: {workplace['Type']}")
            print(f"Shifts: {workplace['Shifts']}")
            print(f"Time and Date: {workplace['Time and Date']}")
            print(f"Hourly Rate: {workplace['Hourly Rate']}")
            print(f"Evening Incentive: {workplace['Evening Incentive']}")
            print(f"Positions Available: {workplace['Positions']}")
            print(f"Location: {workplace['Location']}")
            print("-" * 50)

    def apply_for_job(self, workplace_id):
        """Apply for a job using the workplace ID."""
        application = {
            "application_id": f"A{random.randint(1000, 9999)}",
            "Worker ID": self.worker_id,
            "Workplace ID": workplace_id,
            "Status": "Pending"
        }

        Database.save_application(application)
        print("Your application has been submitted successfully.")

    def view_application_status(self):
        """Display the status of the worker's job applications."""
        applications = Database._load_data(Database.APPLICATION_FILE)

        # Filter applications belonging to this worker
        my_applications = [app for app in applications if app["Worker ID"] == self.worker_id]

        if not my_applications:
            print("No applications found.")
            return []

        # Display all applications with their statuses
        for app in my_applications:
            print(
                f"Application ID: {app['application_id']}, Workplace ID: {app['Workplace ID']}, Status: {app['Status']}")

        return my_applications

    def part_time_work_schedule(self):
        """Display the worker's assigned work schedule."""
        schedule = Database.get_schedule(self.worker_id)

        # Debugging: Print retrieved schedule
        print(f"DEBUG: Retrieved schedule for Worker ID {self.worker_id}: {schedule}")

        if not schedule:
            print("No schedule available.", schedule)
            return

        print("Your Work Schedule:")
        print(f"Workplace Name: {schedule.get('Workplace Name', 'Not specified')}")
        print(f"Location: {schedule.get('Location', 'Not specified')}")
        print(f"Time and Date: {schedule.get('Time and Date', 'Not specified')}")
        print(f"Shift: {schedule.get('Shift', 'Not specified')}")

    # def part_time_work_schedule(self):
    #     """Display the worker's assigned work schedule."""
    #     schedule = Database.get_schedule(self.worker_id)
    #
    #     if not schedule:
    #         print("No schedule available.", schedule)
    #         return
    #
    #     print("Your Work Schedule:")
    #     print(f"Workplace Name: {schedule.get('Workplace Name', 'Not specified')}")
    #     print(f"Location: {schedule.get('Location', 'Not specified')}")
    #     print(f"Time and Date: {schedule.get('Time and Date', 'Not specified')}")
    #     print(f"Shift: {schedule.get('Shift', 'Not specified')}")
    #
    #     return {}


