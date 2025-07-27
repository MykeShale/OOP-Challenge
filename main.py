import pet
import time
"""
- This is a simple pet simulator program that allows users to create a pet and interact with it.
- The user can feed the pet, play with it, teach it tricks, and check its status.
- The program uses a class to represent the pet and its attributes, and it provides a simple text-based interface for user interaction.
- The program is designed to be easy to use and understand, making it suitable for beginners in programming.
- The program is written in Python and uses basic programming concepts such as classes, methods, and user input.
- The program is designed to be run in a terminal or command prompt, and it provides clear instructions for the user to follow.
"""

def loading(action, petName=""):
    """Simulate loading time for pet actions."""
    if action == "teach":
        print(f"Teaching {petName} the new trick", end="")
    else:
        print(f"{petName} is {action}ing", end="")
        for i in range(3):
            print(".", end="")
            time.sleep(1)
        print("")

# Main program starts here
print("==============================================")
print("Welcome to the Pet Simulator!")
print("You can create a pet and interact with it.")
print("Let's get started!")
name = input("Please enter the name of your pet: ")

userPet = pet.Pet(name)
# Try to load existing pet data
userPet.load_pet_data()
print("==============================================")
print(f"🐶 Congratulations! You have created a pet named {userPet.name}.")
time.sleep(2)
print("Now, let's see what you can do with your pet.")
time.sleep(3)

while True:
    print("\n==============================================")
    print("Available options:")
    print("1. 🍖 Feed your pet")
    print("2. ⚽ Play with your pet")
    print("3. ✍️  Teach your pet a trick")
    print("4. 📃 Check your pet's status")
    print("5. 😴 Allow your pet to sleep")
    print("6. 📃 Display all tricks your pet knows")
    print("7. 📁 Upload a document")
    print("8. 📋 View uploaded documents")
    print("9. 🗑️  Delete a document")
    print("10. Exit")
    print("==============================================")
    try:
        userChoice = int(input("Please choose an option (1-10): "))
        if userChoice < 1 or userChoice > 10:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 10.")
        time.sleep(2)  # Adding a delay for better readability
        continue

    # Processing user choice
    if userChoice == 1:
        loading("feed", userPet.name)
        userPet.eat()
        userPet.get_status()
    elif userChoice == 2:
        loading("play", userPet.name)
        userPet.play()
        userPet.get_status()
    elif userChoice == 3:
        trick = input("🎃 Please enter the trick you want to teach your pet: ")
        loading("teach", userPet.name)
        if trick == "":
            print("You didn't enter a trick. Please try again.")
            time.sleep(2)
            continue
        elif len(trick) > 20:
            print("Trick name is too long. Please keep it under 20 characters.")
            time.sleep(2)
            continue
        elif len(trick) < 3:
            print("Trick name is too short. Please provide a name with at least 3 characters.")
            time.sleep(2)
            continue
        elif not trick.isalpha():
            print("Trick name should only contain letters.")
            time.sleep(2)
            continue
        userPet.train(trick)
        userPet.get_status()
    elif userChoice == 4:
        userPet.get_status()
    elif userChoice == 5:
        loading("sleep", userPet.name)
        userPet.sleep()
        userPet.get_status()
    elif userChoice == 6:
        userPet.show_tricks()
        time.sleep(2)
    elif userChoice == 7:
        # Upload a document
        print("\n📁 Document Upload")
        print("Available document types:")
        print("1. Profile picture (for your pet)")
        print("2. Medical records")
        print("3. Training certificates")
        print("4. General document")
        
        try:
            doc_type_choice = int(input("Choose document type (1-4): "))
            doc_types = {1: "profile", 2: "medical", 3: "training", 4: "general"}
            if doc_type_choice not in doc_types:
                print("Invalid choice. Using 'general' as default.")
                doc_type = "general"
            else:
                doc_type = doc_types[doc_type_choice]
        except ValueError:
            print("Invalid input. Using 'general' as default.")
            doc_type = "general"
        
        file_path = input("Enter the path to your document: ").strip()
        if file_path:
            userPet.upload_document(file_path, doc_type)
        else:
            print("No file path provided.")
        time.sleep(2)
    elif userChoice == 8:
        # View uploaded documents
        userPet.list_documents()
        time.sleep(3)
    elif userChoice == 9:
        # Delete a document
        userPet.list_documents()
        if userPet.documents:
            doc_name = input("\nEnter the name of the document to delete: ").strip()
            if doc_name:
                userPet.delete_document(doc_name)
            else:
                print("No document name provided.")
        time.sleep(2)
    elif userChoice == 10:
        confirm = input("Are you sure you want to exit? (yes/no): ").strip().lower()
        if confirm == "yes":
            print("Thank you for using the Pet Simulator!")
            break
        else:
            print("Returning to the menu...")
            time.sleep(2)
    else:
        print("Try again.")
        time.sleep(2)

# Simulate closing the simulator
print("Closing the Pet simulator", end="")
for i in range(3):
    print(".", end="")
    time.sleep(1)
print("\nGoodbye!")
