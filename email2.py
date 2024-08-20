### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

class Email():

    # Declare the class variable, with default value, for emails. 
    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
 
    # Initialise the instance variables for emails.
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
            self.has_been_read = True
        
# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []

# --- Functions --- #
# Build out the required functions for your program.


def populate_inbox():
    sample_emails = [
        Email("example1@gmail.com", "subject1", "content1"),
        Email("example2@gmail.com", "subject2", "content2"),
        Email("example3@gmail.com", "subject3", "content3")
        ]

    for email in sample_emails:
        inbox.append(email)

# Create 3 sample emails and add it to the Inbox list.  



def list_emails():
    for index, email in enumerate(inbox):
        print("{} {}".format(index,email.subject_line))
    
    # Create a function which prints the email’s subject_line, along with a corresponding number.



def read_email(index):
    if 0 <= index < len(inbox):
        email = inbox[index]
        print("From: {}".format(email.email_address))
        print("Subject: {}".format(email.subject_line))
        print("Content: {}".format(email.email_content))
        email.mark_as_read()
    else:
        print("Invalid index")

    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.

populate_inbox()

list_emails()

read_email(1)