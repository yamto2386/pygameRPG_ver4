class Closet:
    def __init__(self, shirts, pants):
        self.shirts = shirts 
        self.pants = pants 

    def send(self):
        self.word = "ok"
        self.My_closet2 = closet2(My_closetM)

    def print(self):
        print(" シャツ：" + self.shirts, "パンツ：" + self.pants)

class closetM(Closet):
    def __init__(self):
        self.ryu  = "m"

    def tora(self):
        self.Tora = "m"


class closet2:
    
    def __init__(self, closet):
        self.closet = closet

    def status_ch(self):
        self.closet.shirts = "NIKE"
        self.closet.pants = "Levis"

    def status_ch2(self):
        self.closet.Tora = "mazikayo"
        print(self.closet.Tora)

    def takeover(self):
        self.closet.My_closet2.status_ch()
        self.closet.status_ch2()
        
        

My_closet = Closet("UNIQLO", "GU")
My_closet.print()
My_closetM = closetM


My_closet.print()
