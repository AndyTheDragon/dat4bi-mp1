import pandas as pd
import os
import email
from email import policy

def biread_email(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r') as data_file:
        msg = email.message_from_file(data_file, policy=policy.default)
    # Extract fields
    email_data = {}
    for headerfield in msg.keys():
        email_data[headerfield] = msg.get(headerfield)


    # Extract the plain text body (if available)
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_content()
                break
    else:
        body = msg.get_content()

    email_data["Body"] = body

    # Create a DataFrame
    return pd.DataFrame([email_data])