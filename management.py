from yahoo_fin.stock_info import get_live_price


#buying the found stocks





#selling the existing stocks


#data management



class myStocks:
    #creates stock object with no inputs
    def __init__(self,name ):
        #list
        self.amount = []

        #list
        self.priceBought = []
        #arbritaty until addstock function called
        self.current = -1
        self.total = 0
        self.net = 0

        #auto runs the setname code when making 
        #new onject so I don't need to take name input
        self.name =name

    #sets name
    def setName (self):
        thename = input ("what is the name of this\n")
        self.name= thename
        return thename
        
    


    def getAmount(self):
        return self.amount
    

    def getPriceBought(self):
        return self.priceBought
    
    def getCurrent(self):
        return self.current
    
    def getTotal(self):
        return self.total
    
    def getNet(self):
        return self.net

    def getName(self):
        return self.name

    #whenever you buy it adds to the list
    def addStock(self):
        priceb = get_live_price(self.name)
        amt = int(input ("how much do you want?"))
        self.amount.append(amt)
        self.priceBought.append(priceb)
        self.total += amt
        self.net = self.total *self.current


    def showStocks(self):

        self.updatePrice()

        print("   Name  |  Amount  |  Price Bought  |  current value")
        
        print ("  ",self.name, "     ",end="")
        print (self.amount, "    ",end="")
        print (self.priceBought, "      ",end="")
        print (self.current, "  ",end="")
        

        print("\n")
        print ("total current value", self.net)
    
    def updatePrice(self):
        
        self.current = get_live_price(self.name)
        self.net = self.total *self.current



#need to create a list of all the stocks
#will have a table where each value is an object
#and a corresponding table with the name of each
#stock object

def createPortfolio():
    names = []
    allstocks = []
    return allstocks,names


def addNewStock(portfolio,names):
    #before creating new stock in profile check
    #if there is already one in profile
    #if there is just add the details to the existing object
    thename = input ("what is the name of this\n")
    for i in range (0,len(names)):
        if (thename == names[i]):
            portfolio[i].addStock()
            return


    #not already in portfolio
    portfolio.append(myStocks(thename))
    newestAddition = (len(portfolio)-1)
    #add the newest added stock to names
    names.append(thename)
    portfolio[newestAddition].addStock()



def showPortfolio(portfolio):
    total = 0
    print("   Name  |  Amount  |   Price Bought   |  current value")
    for i in range (0, len(portfolio)):
        portfolio[i].updatePrice()
        print ("  ",(portfolio[i]).getName(),end="")
        #more times purchasing stock
        if(len((portfolio[i]).getAmount()) >1):
            print ("%8d"%(portfolio[i]).getAmount()[0],"    ",(portfolio[i]).getPriceBought()[0],"  ",end="")
            print ((portfolio[i]).getCurrent(), "  ")
            for j in range (1,(len((portfolio[i]).getAmount()))):
                print("%15d"%(portfolio[i]).getAmount()[j], "    ",(portfolio[i]).getPriceBought()[i])

        #one time purchasing stock
        else:
            print ("%8d"%(portfolio[i]).getAmount()[0],"    ",(portfolio[i]).getPriceBought()[0],"  ",end="")
            print ((portfolio[i]).getCurrent(), "  ")
        

        print("")
        total += (portfolio[i]).getNet()
    print ("total current value", total,"\n")