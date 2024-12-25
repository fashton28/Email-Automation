import smtplib
from email.message import EmailMessage
from gpt import GptResponse

emails={"Felipe":"felipeashton11@gmail.com",
        "Fabian":"fabianashton645@gmail.com"}

def SendEmail():
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("felipeashton11@gmail.com", "zenj zbnr cscc slhg")
        mess = input("What is your email about: ")
        message= GptResponse(mess)
        s.sendmail(f"{emails["Felipe"]}", f"{emails["Fabian"]}", message)
        s.quit()  
        
SendEmail()     
