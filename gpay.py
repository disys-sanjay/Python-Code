import Googlepaypack



class Phone_pe(Googlepaypack.Googlepay):                                                                                          #INHERITANCE
    def __init__(self,Email_ID,Phone_number,Name):
        super().__init__(Email_ID,Phone_number,Name)

    def open_phonepe(self):
        print("Phone pe")

Sanjay=Googlepaypack.Googlepay("Sanjay.Ghanshyam@gmail.com","9840075504","SanjayGhanshyam")
Sanjay.open_gpay()
Sanjay.email_verification()
Sanjay.mobile_verification()
Sanjay.name_verification()
Sanjay.otp_verification(15698,15698)
Sanjay.Bank_verification()
Sanjay.PanCard_Verification()
Sanjay.set_Pin("5384")
Sanjay.Enter_your_Pin(3465,3465)

class Phone_pe(Googlepaypack.Googlepay):                                                                                          #INHERITANCE
    def __init__(self,Email_ID,Phone_number,Name):
        super().__init__(Email_ID,Phone_number,Name)

    def open_phonepe(self):
        print("Phone pe")
        
Ghanshyam=Phone_pe("Sanjayss@gmail.com","9840075504","Sanjay")
Ghanshyam.open_phonepe()
Ghanshyam.mobile_verification()
Ghanshyam.name_verification()
Ghanshyam.otp_verification(780965,780965)
Ghanshyam.Bank_verification()
Ghanshyam.PanCard_Verification()
Ghanshyam.set_Pin("238790")
Ghanshyam.Enter_your_Pin(3564,3564)


        
googlepay=[{"name":"Sanjay","gpaynum":7708201277,"type":"personal","transaction":"regular"},                       
           {"name":"aarthi","gpaynum":9841763080,"type":"personal","transaction":"regular"},
           {"name":"abinaya","gpaynum":6381347949,"type":"personal","transaction":"rare"},
           {"name":"afrin","gpaynum":8825491723,"type":"personal","transaction":"never"},
           {"name":"ajay","gpaynum":7200636126,"type":"personal","transaction":"rare"},
           {"name":"ahmed","gpaynum":9597916931,"type":"personal","transaction":"rare"},
           {"name":"athai","gpaynum":8056469214,"type":"personal","transaction":"regular"},
           {"name":"anandh","gpaynum":9962454803,"type":"personal","transaction":"rare"},
           {"name":"anandhi","gpaynum":8015341851,"type":"personal","transaction":"rare"},
           {"name":"angamma","gpaynum":7305624091,"type":"personal","transaction":"rare"},
           {"name":"anitha","gpaynum":8939509826,"type":"personal","transaction":"rare"},
           {"name":"archana","gpaynum":6369121983,"type":"personal","transaction":"regular"},
           {"name":"ashwini","gpaynum":9833807044,"type":"personal","transaction":"regular"},
           {"name":"asma","gpaynum":9941297487,"type":"personal","transaction":"rare"},
           {"name":"bagavathi","gpaynum":7200001990,"type":"personal","transaction":"regular"},
           {"name":"balaji","gpaynum":6382880108,"type":"personal","transaction":"rare"},
           {"name":"belgin","gpaynum":9941656319,"type":"personal","transaction":"regular"},
           {"name":"beulah","gpaynum":9500075619,"type":"personal","transaction":"rare"},
           {"name":"bhuvan","gpaynum":8072512570,"type":"personal","transaction":"regular"},
           {"name":"chandru","gpaynum":6382761961,"type":"personal","transaction":"rare"}]


for i in googlepay:
    for j,k in i.items():                                                                                           
        print(f"{j}:{k}")
    

