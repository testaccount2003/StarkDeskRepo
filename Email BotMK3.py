import smtplib
while True:
    try:
        mailAddress = input("Enter recipient's mail address: " )
        print(" Please turn on /"Less Secure Apps/" in "/Security/" Tab in your "/Google Account/"") 
        text = input("Enter message to be sent: ")
        email = input(" Enter Your Email: ") 
        pass = input(" Enter your Password: ") 

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, pass)
        server.sendmail(email, mailAddress, text)
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
