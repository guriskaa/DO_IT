# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: GrantTracker
def run_menu():
    while True:
        print("\n=== GrantTracker Menu ===")
        print("1. Add new grant application")
        print("2. List all applications")
        print("3. Filter by status or deadline")
        print("4. Update budget for an application")
        print("5. Exit")
        choice = input("Select option (1-5): ").strip()

        if choice == "1":
            app_id = input("Enter Application ID: ")
            title = input("Title: ")
            deadline_str = input("Deadline (YYYY-MM-DD): ")
            budget = float(input("Budget ($): "))
            status = input("Status (e.g., Pending, Approved): ")
            notes = input("Notes: ")

            grant = {
                "id": app_id,
                "title": title,
                "deadline": deadline_str,
                "budget": budget,
                "status": status,
                "notes": notes
            }
            grants[app_id] = grant
            print(f"Application '{title}' added successfully.")

        elif choice == "2":
            if not grants:
                print("No applications found.")
            else:
                for app_id, data in sorted(grants.items()):
                    print(f"\nID: {app_id}")
                    print(f"Title: {data['title']}")
                    print(f"Deadline: {data['deadline']}")
                    print(f"Budget: ${data['budget']:.2f}")
                    print(f"Status: {data['status']}")

        elif choice == "3":
            filter_type = input("Filter by 'status' or 'deadline'? (s/d): ").strip().lower()
            if filter_type not in ("s", "d"):
                print("Invalid filter type.")
                continue

            value = input(f"Enter {filter_type} value: ")
            results = []
            for app_id, data in grants.items():
                match = False
                if filter_type == "s":
                    if data["status"].lower() == value.lower():
                        match = True
                elif filter_type == "d":
                    if data["deadline"] == value:
                        match = True

                if match:
                    results.append(data)

            if not results:
                print("No matching applications found.")
            else:
                for app in results:
                    print(f"\nID: {app['id']}")
                    print(f"Title: {app['title']}")
                    print(f"Deadline: {app['deadline']}")
                    print(f"Budget: ${app['budget']:.2f}")
                    print(f"Status: {app['status']}")

        elif choice == "4":
            app_id = input("Enter Application ID to update budget: ")
            if app_id not in grants:
                print("Application not found.")
                continue
            new_budget = float(input("New Budget ($): "))
            grants[app_id]["budget"] = new_budget
            print(f"Budget for {grants[app_id]['title']} updated to ${new_budget:.2f}.")

        elif choice == "5":
            print("Exiting GrantTracker.")
            break

        else:
            print("Invalid option. Please choose 1-5.")
