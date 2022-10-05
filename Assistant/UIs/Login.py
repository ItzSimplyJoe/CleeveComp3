import customtkinter
import tkinter
import smtplib
import random
from email.message import EmailMessage
from tkinter.font import BOLD
theme = "light"
font = "helvetica"
customtkinter.set_appearance_mode(theme)
customtkinter.set_default_color_theme("blue")
class Login(customtkinter.CTk):
    WIDTH = 560
    HEIGHT = 330

    def __init__(self):
        super().__init__()

        self.title("Login")
        self.geometry(f"{Login.WIDTH}x{Login.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.closing)
        frame_1 = customtkinter.CTkFrame(master=self)
        frame_1.pack(pady=20, padx=60, fill="both", expand=True)


        label_1 = customtkinter.CTkLabel(master=frame_1,text = "Log in", justify=tkinter.LEFT)
        label_1.configure(font=(font, 20, tkinter.UNDERLINE, BOLD))
        label_1.grid(row=7, column=0, columnspan=3, pady=20, padx=20, sticky="we")

        self.entry = customtkinter.CTkEntry(master=frame_1,
                                            width=400,
                                            placeholder_text="Username")
        self.entry.grid(row=8, column=0, columnspan=3, pady=20, padx=20, sticky="we")
        self.entry2 = customtkinter.CTkEntry(master=frame_1,
                                            width=400,
                                            placeholder_text="Password", show='*')
        self.entry2.grid(row=10, column=0, columnspan=3, pady=20, padx=20, sticky="we")
        self.button_1 = customtkinter.CTkButton(master=frame_1,
                                                text="SignUp", width=40, height=40,
                                                command=self.opensignup)
        self.button_1.grid(row=11, column=0, columnspan=1, padx=20, pady=10, sticky="we")
        self.button_2 = customtkinter.CTkButton(master=frame_1,
                                                text="Forgotten Password", width=40, height=40,
                                                command=self.openforgottenpassword)
        self.button_2.grid(row=11, column=1, columnspan=1, padx=20, pady=10, sticky="we")
        self.button_3 = customtkinter.CTkButton(master=frame_1,
                                                text="Submit", width=40, height=40,
                                                command=self.loginbackend)
        self.button_3.grid(row=11, column=2, columnspan=1, padx=20, pady=10, sticky="we")




    def closing(self):
        self.destroy()

    def opensignup(self):
        self.destroy()
        signup = SignUp()
        signup.mainloop()
    def openforgottenpassword(self):
        self.destroy()
        forgottenpassword = ForgottenPassword()
        forgottenpassword.mainloop()
    def loginbackend(self):
        total = 0
        supplied_username = self.entry.get()
        supplied_password = self.entry2.get()
        with open(r"C:\Users\Owner\OneDrive\Desktop\CleeveComp3\Assistant\UIs\logincredentials.txt", 'r') as file:
            for line in file:
                email, username, password = line.rstrip("\n").split(",")
                if username == supplied_username and password == supplied_password:
                    total = 1
                    print("Successful Login")
            else:
                if total == 0:
                    self.errormsg()

    def errormsg(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("300x100")
        label = customtkinter.CTkLabel(window, text="Login Failed Please Try again")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

class SignUp(customtkinter.CTk):
    WIDTH = 560
    HEIGHT = 440

    def __init__(self):
        super().__init__()

        self.title("SignUp")
        self.geometry(f"{SignUp.WIDTH}x{SignUp.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.closing)
        frame_1 = customtkinter.CTkFrame(master=self)
        frame_1.pack(pady=20, padx=60, fill="both", expand=True)


        label_1 = customtkinter.CTkLabel(master=frame_1,text = "Sign Up", justify=tkinter.LEFT)
        label_1.configure(font=(font, 20, tkinter.UNDERLINE, BOLD))
        label_1.grid(row=7, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.entry = customtkinter.CTkEntry(master=frame_1,
                                            width=400,
                                            placeholder_text="Email")
        self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.entry2 = customtkinter.CTkEntry(master=frame_1,
                                            width=400,
                                            placeholder_text="Username")
        self.entry2.grid(row=10, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.entry3 = customtkinter.CTkEntry(master=frame_1,
                                            width=400,
                                            placeholder_text="Password", show='*')
        self.entry3.grid(row=11, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.entry4 = customtkinter.CTkEntry(master=frame_1,
                                            width=400,
                                            placeholder_text="Confirm Password", show='*')
        self.entry4.grid(row=12, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.button_1 = customtkinter.CTkButton(master=frame_1,
                                                text="Back", width=40, height=40,
                                                command=self.openlogin)
        self.button_1.grid(row=13, column=0, columnspan=1, padx=20, pady=10, sticky="we")
        self.button_2 = customtkinter.CTkButton(master=frame_1,
                                                text="SignUp", width=40, height=40,
                                                command=self.SignUpbackend)
        self.button_2.grid(row=13, column=1, columnspan=1, padx=20, pady=10, sticky="we")




    def closing(self):
        self.destroy()

    def SignUpbackend(self):
        total1 = 0
        email = self.entry.get()
        username = self.entry2.get()
        password = self.entry3.get()
        confirmpassword = self.entry4.get()

        if email == "" or username == "" or password == "" or confirmpassword == "":
            self.popup("Please Fill in all of the fields")
        else:
            if password == confirmpassword:
                if "@" in email:
                    with open(r"C:\Users\Owner\OneDrive\Desktop\CleeveComp3\Assistant\UIs\logincredentials.txt", 'r') as file:
                        for line in file:
                            email1,username1,password1 = line.rstrip("\n").split(",")
                            if email1 == email:
                                self.popup("Someone has already signed up with that email!")
                                total1 = total1 + 1
                                continue
                            elif username1 == username:
                                total1 = total1 + 1
                                self.popup("Someone has already signed up with that username!")
                                continue
                    if total1 == 0:
                        self.openlogin()
                        self.accountcreation(email,username,password)
                else:
                    self.popup("Input a valid email")
            else:
                self.popup("Your passwords dont match")

    def popup(self,textforfill):
        window = customtkinter.CTkToplevel(self)
        window.geometry("500x100")
        label = customtkinter.CTkLabel(window, text=textforfill)
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

    def accountcreation(self,email,username,password):
        file = open(r"C:\Users\Owner\OneDrive\Desktop\CleeveComp3\Assistant\UIs\logincredentials.txt", "a")
        file.write ((email) + "," + (username) + "," + (password) + "\n")
        file.close()

    def openlogin(self):
        self.destroy()
        login = Login()
        login.mainloop()

class ForgottenPassword(customtkinter.CTk):
    WIDTH = 300
    HEIGHT = 200

    def __init__(self):
        super().__init__()

        self.title("Forgotten Password")
        self.geometry(f"{ForgottenPassword.WIDTH}x{ForgottenPassword.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.closing)
        frame_1 = customtkinter.CTkFrame(master=self)
        frame_1.pack(pady=20, padx=60, fill="both", expand=True)


        label_1 = customtkinter.CTkLabel(master=frame_1,text = "Input Your email to have a OTP sent to you!", justify=tkinter.LEFT)
        label_1.configure(font=(font, 20, tkinter.UNDERLINE, BOLD))
        label_1.grid(row=7, column=0, columnspan=3, rowspan=2, pady=20, padx=20, sticky="we")

        self.entry = customtkinter.CTkEntry(master=frame_1,
                                            width=400,
                                            placeholder_text="Input Your Email")
        self.entry.grid(row=8, column=0, columnspan=3, pady=20, padx=20, sticky="we")
        self.button_1 = customtkinter.CTkButton(master=frame_1,
                                                text="Back", width=40, height=40,
                                                command=self.opensignup)
        self.button_1.grid(row=11, column=0, columnspan=1, padx=20, pady=10, sticky="we")
        self.button_2 = customtkinter.CTkButton(master=frame_1,
                                                text="Submit", width=40, height=40,
                                                command=self.forgottenpassword)
        self.button_2.grid(row=11, column=1, columnspan=1, padx=20, pady=10, sticky="we")

    def closing(self):
        self.destroy()

    def opensignup(self):
        self.destroy()
        signup = SignUp()
        signup.mainloop()
    def forgottenpassword(self):
        supplied_email = self.entry.get()
        total = 0
        with open(r"C:\Users\Owner\OneDrive\Desktop\CleeveComp3\Assistant\UIs\logincredentials.txt", 'r') as file:
            for line in file:
                email, username, password = line.rstrip("\n").split(",")
                if email == supplied_email:
                    total = total + 1
            if total > 0:
                self.OTP(supplied_email)
            elif total == 0:
                self.errormsg("That email does not have an account in the system, create an account instead!")

    def OTP(self,supplied_email):
        otp = random.randint(100000,999999)
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login('joesvirtualassistant@gmail.com' ,'kpflqtzddozqgjlj')

            subject = 'One Time Password'
            body = ('Your one time password is '+ str(otp))
            footer = ('This is an incredible virtual assistant created by Joe, the virtual assistant probably doesnt work very well. \n If this email is not for you please just ignore it. \n Thankyou very much,\n Joe')

            msg = f'Subject: {subject}\n\n{body}\n\n{footer}'

            smtp.sendmail('joesvirtualassistant@gmail.com', supplied_email, msg)
        self.otpchecks(supplied_email,otp)
    
    def otpchecks(self,supplied_email,otp):
        window = customtkinter.CTkToplevel(self)
        window.geometry("560x420")
        self.label = customtkinter.CTkLabel(window, text="Input Your OTP and New password")
        self.label.pack(side="top", fill="both", expand=True, padx=40, pady=40)
        self.entry = customtkinter.CTkEntry(window, placeholder_text="Enter Your OTP")
        self.entry.pack(side="top", fill="both", expand=True, padx=40, pady=40)
        self.entry2 = customtkinter.CTkEntry(window, placeholder_text="Enter New Password")
        self.entry2.pack(side="top", fill="both", expand=True, padx=40, pady=40)
        self.button = customtkinter.CTkButton(text="Submit", width=40, height=40,command=self.otpchecktwo(supplied_email,otp))
        self.button.pack(side="top", fill="both", expand=True, padx=40, pady=40)

    def otpchecktwo(self,supplied_email,otp):
        email = supplied_email
        inputted_otp = self.entry.get()
        password = self.entry2.get()
        inputted_otp = int(inputted_otp)
        otp = int(otp)
        finalList = []
        if inputted_otp == otp:
            with open(r"C:\Users\Owner\OneDrive\Desktop\CleeveComp3\Assistant\UIs\logincredentials.txt", 'r') as file:
                for line in file:
                    if line[-1] == "\n":
                        finalList.append(line[:-1].split(','))
                    else:
                        finalList.append(line.split(','))
                        data = finalList
                        for index in range(len(data)):
                            if supplied_email == data[index][0]:
                                data[index][2] = password
                                break
                        with open(r"C:\Users\Owner\OneDrive\Desktop\CleeveComp3\Assistant\UIs\logincredentials.txt", 'w') as file:
                            for line in data:
                                print(','.join(line), file=file)
                        self.opensignup()
        elif inputted_otp != otp:
            self.errormsg("One time password is not valid!")



    def errormsg(self,textforerror):
        window = customtkinter.CTkToplevel(self)
        window.geometry("700x100")
        label = customtkinter.CTkLabel(window, text=textforerror)
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

if __name__ == "__main__":
    login = Login()
    login.mainloop()