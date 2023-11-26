# SIE: SECURE INFORMATION EMBEDDING
It’s a steganography tool for securing files using watermark techniques.

GUI Initialization: Import necessary libraries such as cv2, os, string, stegano, and customtkinter. Set up the Tkinter GUI window with specified dimensions and title.

User Interface Elements: Create UI elements such as labels, buttons, textboxes, and tab views using customtkinter.Configure appearance settings like appearance mode and color theme.

File Handling: Implement functions for opening image files using the file dialog (openFile1 and openFile2).Display selected file paths in corresponding labels.

Encryption: Implement the encryption function (steganography_encryption) using stegano.lsb.hide.Save the encrypted image with a fixed filename ("Encryptedmsg2.png").Display the RGB values of certain pixels from the encrypted image.

Decryption: Implement the decryption function (steganography_decryption) using stegano.lsb.reveal.Read the selected image file for decryption. Display a password derived from specific pixel values and show it in a label.

User Input Handling: Create functions (userInput1 and userInput2) to capture user input from textboxes.

Message Display: Display the decrypted message if the password matches the calculated password.Provide feedback if the entered password is incorrect.

Overall Flow: Organize the code to ensure a logical flow of actions when the user interacts with the GUI.

Main Loop: Start the Tkinter main loop using root.mainloop().

