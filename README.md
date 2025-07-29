# 📲 Student Result SMS Sender

This is a simple Flask web app that helps colleges or departments send students their results via SMS 📱 using Twilio. Just upload a CSV file, filter by year and branch, preview messages, and send with one click.

---

## 🔧 Features

- Upload CSV with student result data
- Filter students by year or branch
- Preview messages before sending
- Automatically formats messages based on result
- Built with Python, Flask, Pandas, and Twilio

---

## 📁 CSV Format (Sample)

Your CSV file should look like this:

| Name     | RegNo     | SGPA | Status | Phone       | Year | Branch | Failed_Subjects |
|----------|-----------|------|--------|-------------|------|--------|------------------|
| John Doe | 22CS001   | 7.2  | Pass   | 918888888888 | 2    | CSE    |                  |
| Jane Doe | 22EC002   | 5.6  | Fail   | 918877777777 | 2    | ECE    | Maths, Physics   |

---

## 🚀 How to Run Locally

1. **Clone the project:**
```bash
git clone https://github.com/yourusername/result-sms-sender.git
cd result-sms-sender
```

2. **Set up virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install required packages:**
```bash
pip install -r requirements.txt
```

4. **Add your Twilio credentials:**
Create a `.env` file and add:

```env
TWILIO_ACCOUNT_SID=your_sid_here
TWILIO_AUTH_TOKEN=your_token_here
TWILIO_NUMBER=your_twilio_number
```

5. **Run the app:**
```bash
python app.py
```

6. Open your browser:
```
http://127.0.0.1:5000
```

---


## 👨‍💻 Made with ❤️ by Eswar 

Feel free to fork or contribute!
