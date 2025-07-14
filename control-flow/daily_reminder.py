# daily_reminder.py

def main():
    # Get task description
    task = input("Enter your task: ").strip()

    # Get and validate priority input
    while True:
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority in ("high", "medium", "low"):
            break
        else:
            print("Please enter a valid priority: high, medium, or low.")

    # Get and validate time sensitivity
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
        if time_bound in ("yes", "no"):
            break
        else:
            print("Please answer with yes or no.")

    # Generate reminder using match-case and if
    match priority:
        case "high":
            base_message = f"'{task}' is a high priority task"
        case "medium":
            base_message = f"'{task}' is a medium priority task"
        case "low":
            base_message = f"'{task}' is a low priority task"

    # Customize based on time-bound
    if time_bound == "yes":
        print(f"\nReminder: {base_message} that requires immediate attention today!")
    else:
        print(f"\nNote: {base_message}. Consider completing it when you have free time.")

if __name__ == "__main__":
    main()
