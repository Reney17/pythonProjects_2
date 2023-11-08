# #for desktop notification
# toast = "ToastNotifier()"

# #definea function for sending email
# def sendEmail(to, sub, msg):
#     #connection to gmail
#     gmail_obj = smtplib.SMTP('smtp.gmail.com', 587)
    
#     #starting the session
#     gmail_obj.starttls()
    
#     #login using credentials
#     gmail_obj.login(GMAIL_ID, GMAIL_PWD)
    
#     #sending email
#     gmail_obj.sendemail(GMAIL_ID, to, f"Subject : {sub}\n\n{msg}")
    
    
#     #quit the session
#     gmail_obj.quit
    
#     print("Email sent to " + str(to) + "with subject " +str(sub) + " and message :" +str(msg))
    
#     toast.show_toast("Email Sent!" , 
#                      f"{name} was sent e-mail", 
#                      threaded = True, 
#                      icon_path =None, 
#                      duration = 6)
# #     while toast.notification_activate():
#     time.sleep(0.1)

# p = "Number"
# p2 = "Number2"
# n = 10
# print (p , p2)

# x = 10 
# float(x)
# bool(x)

# x = 10
# print(str(x))


# y = 0
# print(bool(y))

name = "Skhulile"
print(f"{name}")

