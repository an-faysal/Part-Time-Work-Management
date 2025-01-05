import json
import os


class Database:
    ADMIN_FILE = "admins.json"
    WORKER_FILE = "workers.json"
    WORKPLACE_FILE = "workplaces.json"
    APPLICATION_FILE = "applications.json"
    MESSAGE_FILE = "messages.json"
    SCHEDULE_FILE = "schedules.json"

    @staticmethod
    def _load_data(file_path):
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                return json.load(file)
        return []

    @staticmethod
    def _save_data(file_path, data):
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def save_application(application):
        applications = Database._load_data(Database.APPLICATION_FILE)
        applications.append(application)
        Database._save_data(Database.APPLICATION_FILE, applications)

    @staticmethod
    def get_schedule(worker_id):
        """Retrieve the schedule for a specific worker."""
        schedules = Database._load_data(Database.SCHEDULE_FILE)

        # Debugging: Print all schedules loaded from file
        print(f"DEBUG: Loaded schedules from file: {schedules}")

        if not isinstance(schedules, dict):  # Ensure schedules is a dictionary
            schedules = {}

        return schedules.get(worker_id, {})



