import os
os.system("cls")
ls=[]
class Market:

    __summa=1000000
    balance=0
    def __init__(self):
       pass 
    def kirish(self):
        print("""Bo'limlardan birini tanlang:\n\n
1.Ichimliklar\n\n2.Go'sht mahsulotlari\n\n
3.Sut mahsulotlari\n\n
4.Non maxsulotlari""")
        tanlash=input("Bolimlardan birini tanlang: ")
        match tanlash:
            case "1":
                self.Ichimlik()
            case "2":
                self.Meat()
            case "3":
                self.Milk()
            case "4":
                self.Bread()
    def qaytish(self):
            answer=input("Hurmatli mijoz yana xarid qilasizmi (Ha,Yo'q)? ")
            if answer.upper()=="HA":
                self.kirish()
            else:
                print("Salomat bo'ling")
                print(ls)
    def Ichimlik(self):
        os.system("cls")
        self.suv_money=0
        self.suv_name=""
        print("""Ichimlilardan tanlang:\n\n
1.CocaCola1 - 15 000\n\n2.Pepsi-14 999\n\n3.Fanta - 12 899\n\n4.Dinay-14 000\n\n5.Sprite - 8 000""")
        tanla_suv=input("Ichimlilardan birini tanla: ")
        match tanla_suv:
            case "1":
                self.suv_money=15000
                self.suv_name="CocaCola"
                Market.__summa=Market.__summa-self.suv_money
                ls.append(self.suv_name)
            case "2":
                self.suv_money=14999
                self.suv_name="Pepsi"
                Market.__summa=Market.__summa-self.suv_money
                ls.append(self.suv_name)
            case "3":
                self.suv_money=12899
                self.suv_name="Fanta"
                Market.__summa=Market.__summa-self.suv_money
                ls.append(self.suv_name)
            case "4":
                self.suv_money=14000
                Market.__summa=Market.__summa-self.suv_money
                print(f"Qolgan summa {Market.__summa}")
            case "5":
                self.suv_money=8000
                Market.__summa=Market.__summa-self.suv_money
                print(f"Qolgan summa {Market.__summa}")
        self.qaytish()
    def Meat(self):
        os.system("cls")
        self.meat_narxi=0
        self.meat_name=""
        print("""Gosht mahsulotlaridan birini tanlang:\n\n1.Mol gosht - 80 000\n\n2.Quy goshti - 54 000\n\n3.Tovuq goshti - 23 000""")
        tanla_gosht=input("Gosht mahsulotlaridan birini tanlang: ")
        match tanla_gosht:
            case "1":
                self.meat_name="Mol goshti"
                self.meat_narxi=80000
                Market.__summa=Market.__summa-self.meat_narxi
                ls.append(self.meat_name)
            case "1":
                self.meat_name="Qoy goshti"
                self.meat_narxi=54000
                Market.__summa=Market.__summa-self.meat_narxi
                ls.append(self.meat_name)
            case "3":
                self.meat_name="Tovuq goshti"
                self.meat_narxi=23000
                Market.__summa=Market.__summa-self.meat_narxi
                ls.append(self.meat_name)
        self.qaytish()
    def Milk(self):
        os.system("cls")
        self.milk_litr=""
        self.milk_narxi=0
        print("Sut mahsulotlaridan ozizga keraklisini tanlang\n\n1.1 litr - 10 000\n\n2. 1,5 litr - 15 000")
        milk_tanla=input("Sut mahsulotlaridan birini tanlang: ")
        match milk_tanla:
            case "1":
                self.milk_litr="1 litr sut"
                self.milk_narxi=10000
                ls.append(self.milk_litr)
                Market.__summa=Market.__summa-self.milk_narxi
                
            case "2":
                self.milk_litr="1,5 litr sut"
                self.milk_narxi=15000
                ls.append(self.milk_litr)
                Market.__summa=Market.__summa-self.milk_narxi
        self.qaytish()
    def Bread(self):
        os.system("cls")
        self.bread_name=""
        self.bread_narxi=0
        print("""Non maxsulotlaridan birini tanlang\n\n
1.Buxonka-1400som\n\n
2.Liposhka-3000som\n\n
3.Patir_non-5000som""")
        tanla_non=input("Nonlardan birini kiriting: ")
        match tanla_non:
            case "1":
                self.bread_name="Buxonka"
                self.bread_narxi=1400
                Market.__summa=Market.__summa-self.bread_narxi                
                ls.append(self.bread_name)
            case "2":
                self.bread_name="Liposhka"
                self.bread_narxi=3000
                Market.__summa=Market.__summa-self.bread_narxi                
                ls.append(self.bread_name)
            case "3":
                self.bread_name="Patir_non"
                self.bread_narxi=5000
                Market.__summa=Market.__summa-self.bread_narxi                
                ls.append(self.bread_name)
        self.qaytish()
m=Market()
m.kirish()
