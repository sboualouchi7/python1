#1
size = input("Enter the size of your shirt: ")
text = input("Enter the text of your shirt: ")
def make_shirt(size , text):
    print(f"The size of the shirt is {size} and the text is '{text}'.")
make_shirt(size, text)

#2
def make_shirt2(size="large" , text="I love python"):
    print(f"The size of the shirt is {size} and the text is '{text}'.")
make_shirt2()

#3
make_shirt(size="extra large", text="Keep Calm and Code On")
