import random

def number_guessing_game():
    """Tool 1: A number guessing game with loops and conditionals."""
    print("\n--- Number Guessing Game ---")
    secret_number = random.randint(1, 10)
    guess = 0
    
    while guess != secret_number:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! The secret number was {secret_number}.")
        except ValueError:
            print("Please enter a valid integer.")

def todo_list_manager():
    """Tool 2: An interactive to-do list using a modifiable list."""
    print("\n--- Interactive To-Do List ---")
    tasks = ["Learn Python", "Build final project"]
    
    while True:
        print(f"\nCurrent Tasks: {tasks}")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Back to Main Menu")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == "1":
            new_task = input("Enter the task to add: ")
            tasks.append(new_task)
            print(f"✅ Added '{new_task}' to your list.")
        elif choice == "2":
            rem_task = input("Enter the task to remove: ")
            if rem_task in tasks:
                tasks.remove(rem_task)
                print(f"❌ Removed '{rem_task}' from your list.")
            else:
                print("Task not found in the list.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please pick 1, 2, or 3.")

def bill_splitter():
    """Tool 3: A tip and bill splitter utilizing conditionals and f-strings."""
    print("\n--- Tip & Bill Splitter ---")
    try:
        bill = float(input("Enter the total bill amount ($): "))
        tip_percent = int(input("Enter tip percentage (e.g., 10, 15, 20): "))
        people = int(input("Enter number of people splitting the bill: "))
        
        if bill < 0 or people <= 0:
            print("Bill and people count must be greater than zero.")
            return
            
        total_tip = bill * (tip_percent / 100)
        total_bill = bill + total_tip
        per_person = total_bill / people
        
        print(f"\n--- Bill Summary ---")
        print(f"Tip amount: ${total_tip:.2f}")
        print(f"Total with tip: ${total_bill:.2f}")
        print(f"Each person pays: ${per_person:.2f} 💸")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

def main():
    """Main function running the toolkit menu loop."""
    print("Welcome to your Personal Mini-Toolkit! 🛠️")
    
    while True:
        print("\n==============================")
        print("      MAIN TOOLKIT MENU       ")
        print("==============================")
        print("1. Number Guessing Game")
        print("2. Interactive To-Do List")
        print("3. Tip & Bill Splitter")
        print("4. Quit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            todo_list_manager()
        elif choice == "3":
            bill_splitter()
        elif choice == "4":
            print("\nThank you for using Personal Mini-Toolkit. Goodbye! 👋")
            break
        else:
            print("⚠️ Invalid choice! Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()