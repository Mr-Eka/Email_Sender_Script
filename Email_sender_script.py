import smtplib  # Import the smtplib module to handle email sending via SMTP

# Prompt the user for sender email, receiver email, subject, and message
mail = input("SENDER EMAIL: ")
receiver_email = input("RECEIVER EMAIL: ")
subject = input("SUBJECT: ")
message = input("MESSAGE: ")

# Format the email content with subject and message body
text = f"Subject:{subject}\n\n{message}"

# Connect to Gmail's SMTP server on port 587
server = smtplib.SMTP("smtp.gmail.com", 587)

# Start TLS encryption for secure communication
server.starttls()

# Log in to the sender's email account using an app-specific password
server.login(mail, "uecc ngxy mqcg kmqw")  # Replace with your own Gmail App Password

# Send the email from the sender to the receiver with the message content
server.sendmail(mail, receiver_email, text)

# Print confirmation that the email has been sent
print("Email has been sent to " + receiver_email)
