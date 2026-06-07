





import os
import pandas as pd
from datetime import datetime
import pywhatkit

print("""
====================
WhatsApp Automation
====================

Send Message         ---> 1
Send to CSV contacts ---> 2
View History         ---> 3
Clear History        ---> 4
Exit                 ---> 5
""")

while True:
    option = input("Choose: ")

    if option == "1":
        count = int(input("How many contacts? : "))
        for i in range(count):
            phone = input("Enter Phone Number: ")
            message = input("Enter Message: ")
            hour = int(input("Send at Hour (24hr): "))
            minute = int(input("Send at Minute: "))
            confirm = input("Are you sure? (yes/no): ")
            if confirm == "yes":
                try:
                    pywhatkit.sendwhatmsg(phone, message, hour, minute)
                    print(f"✅ Message {i+1} Scheduled!")
                    with open("history.txt", "a") as f:
                        f.write(f"Date: {datetime.now()} | To: {phone} | Message: {message}\n")
                except Exception as e:
                    print(f"❌ Error: {e}")
            else:
                print("❌ Message Cancelled!")

    elif option == "2":
        if os.path.exists("contacts.csv"):
            df = pd.read_csv("contacts.csv")
            message = input("Enter Message: ")
            hour = int(input("Send at Hour (24hr): "))
            minute = int(input("Send at Minute: "))
            confirm = input("Are you sure? (yes/no): ")
            if confirm == "yes":
                for i, row in df.iterrows():
                    try:
                        pywhatkit.sendwhatmsg(str(row["Phone"]), message, hour, minute)
                        print(f"✅ Message sent to {row['Name']}!")
                        with open("history.txt", "a") as f:
                            f.write(f"Date: {datetime.now()} | To: {row['Phone']} | Message: {message}\n")
                    except Exception as e:
                        print(f"❌ Error: {e}")
            else:
                print("❌ Cancelled!")
        else:
            print("❌ contacts.csv not found!")

    elif option == "3":
        if os.path.exists("history.txt"):
            with open("history.txt", "r") as f:
                print(f.read())
        else:
            print("❌ No history found!")

    elif option == "4":
        if os.path.exists("history.txt"):
            os.remove("history.txt")
            print("✅ History cleared!")
        else:
            print("❌ No history found!")

    elif option == "5":
        print("Bye!")
        break

    else:
        print("❌ Invalid Option!")
