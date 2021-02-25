class Category:
    #name = "placeholder"
    #ledger = [{ "amount": 0, "description": "0" }]
    #empty = True

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
        self.empty = True
        self.balance = 0
        self.ledger = []
        #print("create: " + name)
    def deposit(self, val, msg = ""):
        if self.empty:
            self.ledger = [{ "amount": val, "description": msg }]
            self.empty = False
            #print("d new")
        else:
            self.ledger.append({ "amount": val, "description": msg })
            #print("d append")
        self.balance += val
    def get_balance(self):
        return self.balance
    def get_name(self):
        return str(self.name)
    def withdraw(self, val, msg = ""):
        if not self.check_funds(val):
            return False
        self.balance -= val
        if self.empty:
            self.ledger = [{ "amount": -val, "description": msg }]
            self.empty = False
            #print("w new")
        else:
            self.ledger.append({ "amount": -val, "description": msg })
            #print("w append")
        return True
    def transfer(self, val, other):
        #print("REEE" + other.get_name() + "REEE")
        on = "" + other.get_name()
        n = "" + self.get_name()
        #print("zEEE" + self.get_name() + "zEEE")
        if self.withdraw(val,("Transfer to " + on)):
            #print("4")
            other.deposit(val,("Transfer from " + n))
            #print("3")
            return True
        else:
            return False
    def check_funds(self, val):
        #print("T: " + str(val < self.balance))
        return (val <= self.balance)
    def get_spendings(self):
        v = 0
        for i in self.ledger:
            if i["amount"] < 0:
                v += i["amount"]
        return v
    def __str__(self):
        v = 30 - len(self.name)
        v = v * .5
        pos = 0
        s = ""
        while pos < v:
            s += "*"
            pos += 1
        pos = 0
        s += self.get_name()
        while pos < v:
            s += "*"
            pos += 1
        pos = 0
        while pos < len(self.ledger):
            s+= "\n"
            pos2 = 0
            while pos2 < 23 and pos2 < len(self.ledger[pos]["description"]):
                s += self.ledger[pos]["description"][pos2]
                pos2 += 1
            while pos2 < 23:
                s += " "
                pos2 += 1
            width = len(str(self.ledger[pos]["amount"]))
            a = str(self.ledger[pos]["amount"])
            #if self.ledger[pos]["amount"] < 0:
            #    width += 1
            #    a = "-" + a
            if(self.ledger[pos]["amount"] % 1 == 0):
                a += ".00"
                width += 3
            pos3 = 0
            while pos3 < (7 - width):
                s += " "
                pos3 += 1
            pos3 = 0
            while pos3 < len(a):
                s += a[pos3]
                pos3 += 1
            pos += 1
        s += "\nTotal: "
        v = 0
        pos = 0
        while pos < len(self.ledger):
            v += self.ledger[pos]["amount"]
            pos += 1
        s += str(v)
        if v % 1 == 0:
            s += ".00"
        return s;

def create_spend_chart(categories):
    pos = 10
    s = "Percentage spent by category\n"
    totalWidthdraw = 0
    divider = "    -"
    for c in categories:
        totalWidthdraw += c.get_spendings()
        divider += "---"

    while pos >= 0:
        v = pos * 10
        width = len(str(v))
        i = 0
        while i < (3 - width):
            s += " "
            i += 1
        s += str(v) + "| "

        for c in categories:
            if (c.get_spendings() / totalWidthdraw) >= (pos * .1):
                s += "o  "
            else:
                s += "   "

        s += "\n"
        pos -= 1
    s += divider
    #s+="\n     "
    pos = 0
    leng = 0
    for c in categories:
        if len(c.get_name()) > leng:
            leng = len(c.get_name())
    while pos < leng:
        s+="\n     "
        for c in categories:
            if pos < len(c.get_name()) and c.get_name()[pos] != None:
                s += c.get_name()[pos]
            else:
                s += " "
            s += "  "
        #s += "\n"
        pos += 1

    return s
    #print("deez")
