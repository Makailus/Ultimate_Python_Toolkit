import tkinter as tk
from tkinter import messagebox, simpledialog
import webbrowser
import geocoder
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import boto3
import cv2
import mediapipe as mp

# Function for computer vision
def computer_vision():
    # Initialize mediapipe hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

    # Initialize mediapipe drawing
    mp_drawing = mp.solutions.drawing_utils

    # Initialize video capture
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the image to RGB and process it with mediapipe
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        # Check if hands are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmark points on the image
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Display the resulting frame
        cv2.imshow('Hand Gesture Recognition', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Function for location finder
def location_finder():
    # Get the user's current location
    location = geocoder.ip('me')
    
    # Extract the location details
    latitude = location.latlng[0]
    longitude = location.latlng[1]
    city = location.city
    country = location.country
    
    # Format the location information
    location_info = f"Latitude: {latitude}\nLongitude: {longitude}\nCity: {city}\nCountry: {country}"
    
    # Show the location information in a message box
    messagebox.showinfo("Location Finder", location_info)

# Function for Boto3 instances
def boto3_instances():
    # Prompt the user to enter AWS credentials
    aws_access_key_id = simpledialog.askstring("AWS Credentials", "Enter AWS Access Key ID:")
    aws_secret_access_key = simpledialog.askstring("AWS Credentials", "Enter AWS Secret Access Key:")
    aws_region = simpledialog.askstring("AWS Credentials", "Enter AWS Region:")

    # Check if any of the fields are empty
    if not (aws_access_key_id and aws_secret_access_key and aws_region):
        messagebox.showerror("Error", "AWS credentials cannot be empty.")
        return

    try:
        # Connect to AWS using Boto3
        ec2 = boto3.resource('ec2', aws_access_key_id=aws_access_key_id,
                            aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

        # Get running instances
        instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

        # Display instance details
        instance_details = ""
        for instance in instances:
            instance_details += f"Instance ID: {instance.id}, Instance Type: {instance.instance_type}\n"

        if instance_details:
            messagebox.showinfo("Running Instances", instance_details)
        else:
            messagebox.showinfo("Running Instances", "No running instances found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        
# Function for containerization
def containerization():
    # Ask the user for the AWS instance public IP address
    aws_instance_public_ip = simpledialog.askstring("AWS Instance Public IP", "Enter the public IP address of your AWS instance:")
    
    # Check if the user provided an IP address
    if not aws_instance_public_ip:
        messagebox.showerror("Error", "Please provide the public IP address of your AWS instance.")
        return

    # Construct the URL using the public IP address of your AWS instance
    website_url = f'http://{aws_instance_public_ip}'
    
    # Open the web browser to display the website
    webbrowser.open(website_url)

# Function for email sending
def email_sender():
    # Set sender and recipient email addresses
    from_email = 'harshbro5080@gmail.com'
    to_email = simpledialog.askstring("Email Sender", "Enter recipient's email address:")
    if to_email:
        # Email content
        subject = 'Test Email'
        message = 'This is a test email sent from Python using Gmail SMTP.'

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Gmail SMTP server settings
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        # Connect to Gmail's SMTP server and send the email
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(from_email, 'lyap rgov xgrd uxsa')  # Replace 'your_password' with your Gmail password
            server.sendmail(from_email, to_email, msg.as_string())
            server.quit()
            messagebox.showinfo("Email Sender", "Email sent successfully.")
        except Exception as e:
            messagebox.showerror("Email Sender", f"Error sending email: {e}")

if _name_ == '_main_':
    root = tk.Tk()
    root.title("Function Buttons")

    # Create buttons
    btn1 = tk.Button(root, text="Computer Vision", command=computer_vision)
    btn1.pack()

    btn2 = tk.Button(root, text="Boto3 Instances", command=boto3_instances)
    btn2.pack()

    btn4 = tk.Button(root, text="Containerization", command=containerization)
    btn4.pack()

    btn5 = tk.Button(root, text="Location Finder", command=location_finder)
    btn5.pack()

    btn6 = tk.Button(root, text="Email Sender", command=email_sender)
    btn6.pack()

    # Run the main loop
    root.mainloop()


# In[ ]:
