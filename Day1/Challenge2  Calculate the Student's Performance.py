class Student:
    def __init__(self , name , phy , chem , bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio
        # self.total = totalObtained()

    def totalObtained(self):
        total = self.chem + self.bio + self.phy
        return total

    def Percentage(self):
        percent = self.totalObtained()*100/300
        return percent
