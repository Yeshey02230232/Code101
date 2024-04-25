class pets:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color=color
Nima = pets("Nima",7,"black")
Dawa = pets("Dawa",8,"white")
Blacky = pets("Blacky",10,"Red")
print("[Pets Name]:",Nima.name, "[Pets age]: ",Nima.age ,"[Pets color ]:", Nima.color)
print("[Pets Name]:",Dawa.name, "[Pets age]: ",Dawa.age ,"[Pets color ]:", Dawa.color)
print("[Pets Name]:",Blacky.name ,"[Pets age]: ",Blacky.age ,"[Pets color ]:" ,Blacky.color)