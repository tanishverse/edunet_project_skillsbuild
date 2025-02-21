import cv2
import os

# Load the image
img = cv2.imread("mypic.jpg")  # Make sure the image exists

if img is None:
    print("Error: Image not found!")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Encoding dictionary
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

height, width, _ = img.shape

if len(msg) > height * width:
    print("Error: Message too long for this image!")
    exit()

index = 0
for i in range(height):
    for j in range(width):
        if index < len(msg):
            img[i, j, 0] = d[msg[index]]  # Store ASCII value in the Blue channel
            index += 1

cv2.imwrite("encryptedImage.jpg", img)
print("Message successfully hidden in encryptedImage.jpg!")

# Decoding
pas = input("Enter passcode for Decryption: ")

if password == pas:
    decrypted_message = ""
    index = 0
    for i in range(height):
        for j in range(width):
            if index < len(msg):
                decrypted_message += c[img[i, j, 0]]  # Retrieve ASCII from Blue channel
                index += 1
    print("Decrypted message:", decrypted_message)
else:
    print("YOU ARE NOT AUTHORIZED!")


