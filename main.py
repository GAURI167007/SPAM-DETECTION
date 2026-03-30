import pandas as pd
import re
import random 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

#text cleaning
def clntxt(txt):
    txt=txt.lower()
    txt=re.sub(r'[^\w\s]','',txt)
    return txt

#loading data

data=pd.read_csv("spam.csv",encoding='latin-1')
if 'v1' in data.columns:
    data= data[['v1','v2']]
    data.columns=['label','messages']
elif 'label' in data.columns and 'messages' in data.columns:
    data=data[['label','messages']]
    data.columns =['label','messages']

data['label']=data['label'].map({'ham':0,'spam':1})
data['messages']=data['messages'].apply(clntxt)

#model training
Xtrn,Xtst,ytrn,ytst=train_test_split(data['messages'],data['label'],test_size=0.2,random_state=42)
vectorizer=TfidfVectorizer(ngram_range=(1,2))
Xtrn=vectorizer.fit_transform(Xtrn)
model=LogisticRegression()
model.fit(Xtrn,ytrn)

    #CYBER FACT ON SUSPICIOUS EMAILS
cyberfacts=[
    "97 Victims per Hour: A new individual falls victim to a cyber-related crime approximately every 37 seconds.",
    "20% Exposure Rate: One in five internet users has their personal email or password leaked every year.",
    "10 Daily Home Attacks: The average household network faces nearly ten hacking attempts every 24 hours.",
    "$19,372 Average Loss: Individual victims lose nearly $20,000 on average per reported cybercrime incident.",
    "10x Deepfake Surge: AI-generated scams, like fake voice calls from 'family,' have increased ten-fold recently."
    ]

# menu
def menu ():
    print("\n WELCOME TO YODHA ")
    print("1.Analyze messages")
    print("2.View cyber facts")
    print("3. About Yodha")
    print("4.Exit")



# analyze function
def anlyze():
    user_input=input("\n enter the message : ")
    if not user_input.strip():
        print("Please enter a valid message.")
        return
    user_input=clntxt(user_input)
    input_vec= vectorizer.transform([user_input])
    prediction=model.predict(input_vec)[0]
    probab=model.predict_proba(input_vec)[0][1]

    spamwords=['free','win','prize','urgent','offer','click','buy now','limited time,kyc,otp']
    found=[w for w in spamwords if w in user_input]

    print("\n result:")
    if prediction == 1:
        print("This message is classified as SPAM.")
        print(f"Confidence : {probab*100:.2f}%")
        print("FACTS:" , random.choice(cyberfacts))
    elif found:
        print("This message is classified as suspicious.")
        print("Keywords:" , "," .join(found))
    else:
        print("This message is classified as HAM (not spam).")
        print(f"Confidence : {(1-probab)*100:.2f}%")

    #tips
    Tips= [
   " Use Passkeys: Swap passwords for biometric passkeys to stop phishing dead in its tracks.",
   "Set a Family Safe Word: Establish a secret phrase to verify identity against AI voice-cloning scams.",
   "Isolate IoT Devices: Move smart home gadgets to a Guest Wi-Fi to protect your main laptop.",
   "Enable MFA Everywhere: Always use Multi-Factor Authentication—ideally an app, not a text message.",
   "Update Software Daily: Patching vulnerabilities immediately is the easiest defense against automated exploits.",
   "Freeze Your Credit: Lock your credit reports to prevent hackers from opening accounts in your name."
    "Trust Nothing Urgent: Treat any immediate action required email as a likely scam and verify manually."
    "Use a VPN on Public Wi-Fi: Encrypt your data whenever you connect to airport or cafe networks."
    "Audit App Permissions: Regularly delete apps and revoke access to your camera, mic, and location."
    ]
    print("\n Tips to avoid spam:")
    print("Tips:" , random.choice(Tips))

    #About Yodha
def Yodha():
    print("\n ABOUT YODHA")
    print("Yodha is an AI-powered spam detection system which has been designed to protect users from malicious emails and messages. It helps us realize that threat is just a click away and so is this safety checker.So, every person should take out a minute before replying or clicking on suspicious messages.Yodha is here fight those attackers in just 1 click!!")
    print("We dont claim 100 percent accuracy but we are here to make you aware of the possible threats and help you stay safe online.")
# main
while True:
    menu()
    choice=input("Enter your choice (1-4): ")
    if choice == '1':
        anlyze()
    elif choice == '2':
        print("\n CYBER FACTS:")
        for fact in cyberfacts:
            print("- " + fact)
    elif choice == '3':
        Yodha()
    elif choice == '4':
        print("Exiting the program. Stay safe online!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
