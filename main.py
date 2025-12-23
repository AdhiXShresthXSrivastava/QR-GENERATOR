import qrcode # Make sure to install the qrcode library using 'pip install qrcode[pil]'

user_input = input("Enter The URL or Text To Generate QR Code: ") # Get user input for QR code data

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,  
    box_size=10,
    border=4,
) # Create QR code instance
qr.add_data(user_input) # Add user input data to QR code
qr.make(fit=True) # Compile the QR code data
img = qr.make_image(fill_color="white", back_color="blue") # Generate the QR code image
img.save("qrcode.png") # Save the image as a PNG file
print("QR Code generated and saved as qrcode.png") # Notify user of completion
img.show() # Display the generated QR code image