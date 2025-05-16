def show_path(path):
    for i, word in enumerate(path, 1):
        print(f"Step {i}: {word}")

def guess_treasure():
    for i in range(3):
        guess = input("Where do you think the treasure is? ").lower()
        if guess == "treasure":
            print("🏆 You found it!")
            return
        elif i == 2:
            print("❌ That's not the treasure.")
        else:
            print("❌ That's not the treasure. Try again!")

# Main Program
path = ["start", "forest", "river", "mountain", "treasure"]
show_path(path)
guess_treasure()
