from queue import Queue

# Initialize patient queue
patient_queue = Queue()

# Menu-driven program
choice = ""
while choice == "4":
    print("Desk Manager - Patient Registration and Appointment System")
    print("1. Register Patient")
    print("2. Remove Patient after Meeting Doctor")
    print("3. Display Patient Queue")
    print("4. Exit")
    
    choice = input("Enter your choice(just enter the option number): ")
    
    if choice == '1':
        # Register Patient
        name = input("Enter patient's name: ")
        patient_queue.put(name)
        print(f"Patient '{name}' registered.")
    elif choice == '2':
        # Remove Patient after Meeting Doctor
        if patient_queue.empty():
            print("No patients in the queue.")
        else:
            removed_patient = patient_queue.get()
            print(f"Patient '{removed_patient}' removed after meeting the doctor.")
    elif choice == '3':
        # Display Patient Queue
        if patient_queue.empty():
            print("No patients in the queue.")
        else:
            print("Current Patient Queue:")
            for index, patient in enumerate(list(patient_queue.queue), start=1):
                print(f"{index}. {patient}")
    elif choice == '4':
        # Exit program
        print("Exiting program...")
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")