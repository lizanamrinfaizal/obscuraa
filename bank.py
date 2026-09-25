class bank:
    def __init__(self,cid,accno,ifsccode,minbalence):
        self.cid=cid
        self.accno=accno
        self.ifsccode=ifsccode
        self.minbalence=minbalence

    def display(self):
        print("customerid=",self.cid)
        print("account number=",self.accno)
        print("ifsc code=",self.cid)
        print("min balence=",self.minbalence)
b1=bank("c1",1234,"ioba123",1222)
b1.display()