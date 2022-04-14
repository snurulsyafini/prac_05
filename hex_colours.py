NAME_TO_CODE = {"Aliceblue": "#f0f8ff", "Aqua": "#00ffff", "Bone": "#e3dac9", "Celeste": "#b2ffff",
                "Citrine": "#e4d00a", "Ebony": "#555d50", "Emerald": "#50c878", "Fulvous": "#e48400", "Gray": "#bebebe",
                "Iris": "#5a4fcf"}
print(NAME_TO_CODE)

colour_name = input("Enter colour name: ").title()
while colour_name != "":
    if colour_name in NAME_TO_CODE:
        print(colour_name, "is", NAME_TO_CODE[colour_name])
    else:
        print("Invalid colour")
    colour_name = input("Enter colour name: ").title()
