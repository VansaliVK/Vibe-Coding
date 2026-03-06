while True:
    # Task 03: Runs repeatedly until 'Exit' [cite: 85-87]
    name = input("\nEnter student's name (or type 'Exit' to stop): ")
    if name.lower() == 'exit':
        break

    # Task 01: Ask for 3 marks [cite: 68]
    mark1 = float(input("Enter mark 1: "))
    mark2 = float(input("Enter mark 2: "))
    mark3 = float(input("Enter mark 3: "))

    # Task 01: Calculate average [cite: 69]
    average = (mark1 + mark2 + mark3) / 3

    # Task 01 & 02: Determine Pass/Fail AND Grade [cite: 71, 81-84]
    if average >= 75:
        grade = "A (Pass)"
    elif average >= 60:
        grade = "B (Pass)"
    elif average >= 40:
        grade = "C (Pass)"
    else:
        grade = "Fail"

    # Task 04: Print clean formatted output [cite: 88-93]
    print("-" * 20)
    print(f"Name: {name}")
    print(f"Average: {average:.1f}")
    print(f"Result: {grade}")
    print("-" * 20)