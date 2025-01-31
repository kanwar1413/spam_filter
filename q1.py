import os

# File paths for the lists
allowed_domains_file = "allowed_domains.txt"
restrict_words_file = "restricted_domain.txt"
bad_words_file = "bad_words.txt"

# Directories
email_dir = "email_dir/"
spam_dir = "spam_dir/"
non_spam_dir = "non_spam_dir/"

# Function to load lists from files
def load_list_from_file(file_path):
    with open(file_path, 'r') as f:
        return [line.strip().lower() for line in f.readlines()]

# Load the allow list, restrict list, and bad word list from files
allow_list = load_list_from_file(allowed_domains_file)
restrict_list = load_list_from_file(restrict_words_file)
bad_word_list = load_list_from_file(bad_words_file)

def extract_domain(email_header):
    # Extracts the domain from the "From" field in the email header.
    if "@" in email_header:
        return email_header.split('@')[-1].strip().lower()
    return ""

def read_email(file_path):
    # Reads the email and separates header from body
    with open(file_path, 'r') as email_file:
        lines = email_file.readlines()
        header = lines[0]
        body = ''.join(lines[1:])
    return header, body

def classify_email(header, body):
    # Extract the domain from the email header
    domain = extract_domain(header)
   
    # Check allow and restrict lists
    if domain in allow_list:
        return "non_spam"
    if domain in restrict_list:
        return "spam"
    
    # Check for bad words in the body
    bad_word_count = sum(word in body.lower() for word in bad_word_list)
    if bad_word_count > 5:
        return "spam"
    
    return "non_spam"

def move_file(src, dest):
    # Ensure the destination directory exists
    if not os.path.exists(dest):
        os.makedirs(dest)

    # Get the base filename
    filename = os.path.basename(src)
    
    # Construct the destination file path
    dest_path = os.path.join(dest, filename)
    
    # Move the file using os.rename (works within the same file system)
    os.rename(src, dest_path)

def process_emails():
    for filename in os.listdir(email_dir):
        if filename.endswith(".eml"):
            email_path = os.path.join(email_dir, filename)
            
            # Read the email
            header, body = read_email(email_path)
            
            # Classify the email
            classification = classify_email(header, body)
            
            # Move email to the appropriate directory
            if classification == "spam":
                move_file(email_path, spam_dir)
            else:
                move_file(email_path, non_spam_dir)

# Run the spam filter
process_emails()
