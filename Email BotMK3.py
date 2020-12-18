import smtplib
while True:
    try:
        mailAddress = input("Enter recipient's mail address: " )
        text = input("Enter message to be sent: ")


        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('dehimangshu03@gmail.com', 'password#$34')
        server.sendmail('dehimangshu03@gmail.com', mailAddress, text)
        print("Voila! Your mail was sent successfully...")
        print()
        print('Would you like to send another mail?')
        print("Y\nN")
        inpt = input("Enter your choice: ")
        if "Y" in inpt:
            continue
        else:
            print("Have a good day ahead!!")
            break
    except Exception:
        print("Your mail was not \"Sent\" due to some potential errors...")
        break