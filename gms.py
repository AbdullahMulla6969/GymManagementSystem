# Gym Management System - Version 2.0 (Added Status Tracking)
member_records = {}

while True:
    print("\n=== GYM MANAGEMENT SYSTEM (v2.0) ===")
    print("1. Add Member\n2. View Members\n3. Remove Member\n4. Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        m_id = input("Enter Member ID: ").strip()
        name = input("Enter Member Name: ").strip()
        plan = input("Enter Membership Plan (e.g., Monthly/Yearly): ").strip()
        # NEW FEATURE: Membership Status
        status = input("Enter Membership Status (Active/Expired): ").strip()
        
        member_records[m_id] = f"Name: {name}, Plan: {plan}, Status: {status}"
        print("Member saved successfully.")

        
    elif choice == "2":
        if not member_records:
            print("No members found.")
        for m_id, details in member_records.items():
            print(f"ID: {m_id} -> {details}")
            
    elif choice == "3":
        m_id = input("Enter Member ID to remove: ").strip()
        if m_id in member_records:
            del member_records[m_id]
            print("Member removed successfully.")
        else:
            print("Member ID not found.")
            
    elif choice == "4":
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
