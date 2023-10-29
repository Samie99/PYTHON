noun = input("Noun: ")
animal = input("Animal: ")
propernoun = input("Proper Noun: ")
object = input("Object: ")
color = input("Color: ")
food = input("Food: ")

story = f"One day, a {noun} flew across the world and landed on a {animal}."
story += f"\nThe {animal} got scared and ran to the nearest {propernoun}."
story += f"\nThe animal ran so fast and jumped over a {color} {object}."
story += f"\nAfter running for hours, the {animal} stopped to eat a {food}."
story += "\nThe End."

print(story)