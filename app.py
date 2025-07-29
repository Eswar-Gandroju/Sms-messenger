from flask import Flask, render_template, request
import pandas as pd
from twilio.rest import Client

app = Flask(__name__)

# Twilio credentials (replace with your actual values)
account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'          # Your Account SID
auth_token = '  xxxxxxxxxxxxxx'           # Your Auth Token
twilio_number = '+xxxxxxxxxx '        # Your Twilio Number (e.g., '+12357891245')
client = Client(account_sid, auth_token)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if not file:        
            return "No file uploaded", 400

        df = pd.read_csv(file)

        # Get filters
        year = request.form.get('year')
        branch = request.form.get('branch')

        if year and year != 'All':
            df = df[df['Year'] == int(year)]
        if branch and branch != 'All':
            df = df[df['Branch'] == branch]

        results = []

        for _, row in df.iterrows():        
            name = str(row['Name']).strip()
            phone = str(row['Phone']).strip()
            reg_no = str(row['RegNo']).strip()
            sgpa = str(row['SGPA']).strip()
            status = str(row['Status']).strip()

            # Clean phone number (remove leading 0s, ensure 10 digits)
            digits_only = ''.join(filter(str.isdigit, phone))[-10:]
            if len(digits_only) != 10:
                results.append((name, phone, "Failed: Invalid number length"))
                continue

            phone = '+91' + digits_only

            # Build message
            if status.lower() == 'fail' and 'Failed_Subjects' in row:
                failed_subjects = str(row['Failed_Subjects']).strip()
                message_body = (
                    f"Hi {name}, your result is out!\n"
                    f"Reg No: {reg_no}\n"
                    f"SGPA: {sgpa}\n"
                    f"Status: {status}\n"
                    f"Failed Subjects: {failed_subjects}"
                )
            else:
                message_body = (
                    f"Hi {name}, your result is out!\n"
                    f"Reg No: {reg_no}\n"
                    f"SGPA: {sgpa}\n"
                    f"Status: {status}"
                )

            try:
                message = client.messages.create(
                    body=message_body,
                    from_=twilio_number,
                    to=phone
                )
                results.append((name, phone, "Success"))
            except Exception as e:
                results.append((name, phone, f"Failed: {str(e)}"))

        return render_template('result.html', results=results)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
