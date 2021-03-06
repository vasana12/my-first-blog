class setCalckey3:
    def __init__(self, d1, d2 ,d3):
        self.dict1=dict(d1)
        self.dict2=dict(d2)
        self.dict3=dict(d3)

        sum1 = 0
        for d in self.dict1:
            sum1+=self.dict1[d]

        maxVal1=max(self.dict1.values())
        for d in self.dict1:
            #self.dict1[d] /= sum1
            self.dict1[d] /= maxVal1
        print(self.dict1)

        sum2 = 0
        for d in self.dict2:
            sum2+=self.dict2[d]

        maxVal2=max(self.dict2.values())
        for d in self.dict2:
            #self.dict2[d] /= sum2
            self.dict2[d] /= maxVal2
        print(self.dict2)

        sum3 = 0
        for d in self.dict3:
            sum3+=self.dict3[d]

        maxVal3=max(self.dict3.values())
        for d in self.dict3:
            #self.dict3[d] /= sum3
            self.dict3[d] /= maxVal3
        print(self.dict3)



    def getInterG(self):
        samekeys = self.dict1.keys()&self.dict2.keys()&self.dict3.keys()
        intersectg = {}
        for k in samekeys:
            v = min(self.dict1[k],self.dict2[k],self.dict3[k])
            intersectg[k]=v
        return intersectg

    def getInterD(self):
        interg=self.getInterG()
        samekeysAB = self.dict1.keys()&self.dict2.keys()
        intersectab = {}
        for k in samekeysAB:
            v = min(self.dict1[k],self.dict2[k])
            intersectab[k]=v
        intersectd=dict(intersectab)
        for i in interg:
            intersectd[i] -= interg[i]
        return intersectd


    def getInterE(self):
        interg=self.getInterG()
        samekeysAC = self.dict1.keys()&self.dict3.keys()
        intersectac = {}
        for k in samekeysAC:
            v = min(self.dict1[k],self.dict3[k])
            intersectac[k]=v
        intersecte=dict(intersectac)
        for i in interg:
            intersecte[i]-=interg[i]
        return intersecte

    def getInterF(self):
        interg=self.getInterG()
        samekeysBC = self.dict2.keys()&self.dict3.keys()
        intersectbc = {}
        for k in samekeysBC:
            v = min(self.dict2[k],self.dict3[k])
            intersectbc[k]=v
        intersectf=dict(intersectbc)
        for i in interg:
            intersectf[i]-=interg[i]
        return intersectf

    
    def getDiffA(self):
        interD=self.getInterD()
        interE=self.getInterE()
        interG=self.getInterG()
        interDEG={**interD,**interE,**interG}
        diffa = dict(self.dict1)
        for i in interDEG:
            diffa[i]-=interDEG[i]
        return diffa

    def getDiffB(self):
        interD=self.getInterD()
        interF=self.getInterF()
        interG=self.getInterG()
        interDFG={**interD,**interF,**interG}
        diffb = dict(self.dict2)
        for i in interDFG:
            diffb[i]-=interDFG[i]
        return diffb

    def getDiffC(self):
        interE=self.getInterE()
        interF=self.getInterF()
        interG=self.getInterG()
        interEFG={**interE,**interF,**interG}
        diffc = dict(self.dict3)
        for i in interEFG:
            diffc[i]-=interEFG[i]
        return diffc
