# Num = int(input("How Many Apples Should I Remove"))
# Num2 = 0
#
# while Num > 0:
#     print("Apple Removed")
#     Num = Num - 1
#     Num2 = Num2 + 1
#     print(f"{Num2} Apples Removed")

# obstacle = int(input("How Many Obstacles Should I Avoid? "))
# ob2 = 0
#
# while obstacle > 0:
#     obstacle = obstacle -1
#     ob2 = ob2 + 1
#     print(f"Avoiding . . . Done! {ob2} Obstacles Avoided. ")
#
# print("All Obstacles Avoided.")

Charge = int(input("How Many Bars Should Be Charged? "))
Charge2 = 0

while Charge > 0:
    Charge2 = Charge2 + 1
    Charge = Charge - 1
    print(f"Charging {"█ " * Charge2}")

print("The Battery Is Fully Charged")

