# Secure Data Hiding in Image Using Steganography!

## Description
This project implements an image steganography technique using Python and OpenCV. It allows users to hide a secret message inside an image by modifying pixel values. The encoded image can then be shared and later decrypted using a passcode.

## Features
- **Message Encoding**: Hide a secret message in an image.
- **Password Protection**: Ensures that only authorized users can decrypt the message.
- **Pixel-based Encoding**: Uses the blue channel of an image to store ASCII values.
- **Simple & Lightweight**: Requires only OpenCV and standard Python libraries.

## Installation

To run this project, ensure you have Python installed along with OpenCV.

### Install dependencies:
```bash
pip install opencv-python

# Image Steganography using OpenCV

### Encoding a message into an image
python steganography.py
```
- Enter the secret message when prompted.
- Provide a passcode for security.
- The script will generate `encryptedImage.jpg`.

### Decoding a message from an image
Run the script again and enter the correct passcode to retrieve the hidden message.

## Requirements
- Python 3.x
- OpenCV (`cv2` library)

## Example
1. Load an image (e.g., `mypic.jpg`).
2. Enter a secret message.
3. Provide a passcode.
4. The script encodes the message and saves `encryptedImage.jpg`.
5. To retrieve the message, enter the correct passcode when running the script again.

## Future Enhancements
- Add support for multiple encryption layers.
- Implement a GUI for ease of use.
- Improve security by adding more encryption techniques.

## GitHub Repository
https://github.com/tanishverse/edunet_project_skillsbuild.git

---
**Note**: Unauthorized access to an encoded image will not reveal the hidden message.


