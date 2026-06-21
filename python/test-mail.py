import smtplib
sender = "enquiry.aniket23@gmail.com"
password = "Expertbook@123"

receiver = "aniketkorde780@gmail.com"

smtp = smtplib.SMTP("smtp.gmail.com",587)
smtp.starttls()

smtp.login(sender,password)
smtp.sendmail(
    sender,
    receiver,
    "Subject: TEst from wsl\n\nHello from python smtp"
)

smtp.quit()
print("Mail sent")