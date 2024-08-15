head = None
nodes = []

while True:
    print("\nTrain Passenger Management")
    print("1. Add passenger")
    print("2. Remove passenger")
    print("3. View passengers")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter passenger name: ").strip()
        ticket_number = input("Enter ticket number: ").strip()
        new_node = {'name': name, 'ticket_number': ticket_number, 'next': None}
       
        if head is None:
            head = new_node
        else:
            current = head
            while current['next']:
                current = current['next']
            current['next'] = new_node
       
        nodes.append(new_node)
        print(f"Passenger '{name}' with ticket number '{ticket_number}' added.")

    elif choice == '2':
        if head is None:
            print("No passengers to remove.")
        else:
            name = input("Enter passenger name to remove: ").strip()
            current = head
            previous = None
            while current and current['name'] != name:
                previous = current
                current = current['next']
           
            if current is None:
                print(f"Passenger '{name}' not found.")
            else:
                if previous is None:
                    head = current['next']
                else:
                    previous['next'] = current['next']
               
                nodes.remove(current)
                print(f"Passenger '{name}' removed.")

    elif choice == '3':
        if head is None:
            print("No passengers on the train.")
        else:
            print("Passengers on the train:")
            current = head
            while current:
                print(f"Passenger: {current['name']}, Ticket Number: {current['ticket_number']}")
                current = current['next']

    elif choice == '4':
        print("Exiting the application.")
        break

    else:
        print("Invalid choice. Please try again.")