recorded_inputs = []
# Recording Phase
print("Recording Phase: Enter calculator operations (add/subtract x y) or 'stop' to end recording:")
while (user_input := input().strip().lower()) != "stop":
    recorded_inputs.append(user_input)

# Replay Phase
print("\nReplay Phase: Replaying recorded inputs...")
for user_input in recorded_inputs:
    parts = user_input.split()
    try:
        op, operand1, operand2 = parts[0].lower(), int(parts[1]), int(parts[2])
        result = operand1 + operand2 if op == "add" else operand1 - operand2
        print("Result:", result)
    except (ValueError, IndexError):
        print("Invalid input format:", user_input)

print("Test case replay complete. Goodbye!")
