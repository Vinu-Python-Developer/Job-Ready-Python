def move_puppy(direction, correct_direction):
    if direction == correct_direction:
        print(f"✅ Puppy moved {direction}")
        return True
    else:
        print(f"❌ Wrong move! Puppy tried to go {direction}, but got lost.")
        return False

print("🏠 Help the lost puppy get back home through the maze!")
print("Choose the correct directions: left, right, up, down")

# 🗺️ Define the secret correct path
correct_path = ["right", "up", "up"]

# Player has 3 steps
for i in range(3):
    user_move = input(f"Step {i+1} - Where should the puppy go? ").lower()
    if not move_puppy(user_move, correct_path[i]):
        print("💔 Puppy couldn't find the way home.")
        break
else:
    print("🎉 Hooray! Puppy is safely home! 🐾🏠")
