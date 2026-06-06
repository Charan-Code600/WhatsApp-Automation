


import os
import pywhatkit

print("""
====================
WhatsApp Automation
====================

Send Message        ---> 1
View History        ---> 2
Clear History       ---> 3
Exit                ---> 4
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
            try:
                pywhatkit.sendwhatmsg(phone, message, hour, minute)
                print(f"✅ Message {i+1} Scheduled!")
                with open("history.txt", "a") as f:
                    f.write(f"To: {phone} | Message: {message}\n")
            except Exception as e:
                print(f"❌ Error: {e}")

    elif option == "2":
        if os.path.exists("history.txt"):
            with open("history.txt", "r") as f:
                print(f.read())
        else:
            print("❌ No history found!")

    elif option == "3":
        if os.path.exists("history.txt"):
            os.remove("history.txt")
            print("✅ History cleared!")
        else:
            print("❌ No history found!")

    elif option == "4":
        print("Bye!")
        break

    else:
        print("❌ Invalid Option!")

        
