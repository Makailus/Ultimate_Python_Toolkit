# Ultimate_Python_Toolkit

This code creates a graphical user interface (GUI) application using Python's `tkinter` library. The application provides several functionalities through buttons. Here’s a detailed breakdown of what each function does:

1. **Computer Vision**:
    - Uses `cv2` (OpenCV) and `mediapipe` to capture video from the webcam.
    - Detects hand landmarks and draws them on the video feed.
    - Displays the video feed with the hand landmarks drawn.
    - Ends the video feed when 'q' is pressed.

2. **Location Finder**:
    - Uses `geocoder` to get the user's current geographical location based on their IP address.
    - Extracts latitude, longitude, city, and country information.
    - Displays this information in a message box.

3. **Boto3 Instances**:
    - Prompts the user for AWS credentials (Access Key ID, Secret Access Key, and Region).
    - Uses `boto3` to connect to AWS EC2 and retrieve information about running instances.
    - Displays the details of running instances in a message box.

4. **Containerization**:
    - Prompts the user for the public IP address of an AWS instance.
    - Constructs a URL using the provided IP address.
    - Opens this URL in the default web browser.

5. **Email Sender**:
    - Prompts the user for a recipient's email address.
    - Sets up an email with a predefined subject and message.
    - Uses `smtplib` to send the email via Gmail's SMTP server.
    - Displays a message box indicating whether the email was sent successfully or if an error occurred.

The main function initializes the `tkinter` root window and creates buttons for each of these functions, allowing the user to execute them by clicking the corresponding button. The GUI remains active, waiting for user interaction.
