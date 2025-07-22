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

    # Match-case for base message
    match priority:
        case "high":
            priority_text = "high"
        case "medium":
            priority_text = "medium"
        case "low":
            priority_text = "low"

    # Final reminder using exact print format expected by test
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a {priority_text} priority task that requires immediate attention today!")
    else:
        print(f"Note: '{task}' is a {priority_text} priority task. Consider completing it when you have free time.")

if __name__ == "__main__":
    main()