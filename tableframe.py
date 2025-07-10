from tabulate import tabulate
class creatTable():
    def __init__(self,name,item1,item2):
        self.mlist=[]
        self.name=name
        self.a=list(item1)
        self.b=list(item2)
        if len(list(item1))>=len(list(item2)):
            self.item1=list(item1)
            self.item2=list(item2)
            for i in range(0,len(self.item1)):
                for j in range(0,len(self.item2)):
                    self.mlist.append([[self.item1[i],self.item2[j]],None])
        else:
            self.item1=list(item2)
            self.item2=list(item1)
            for i in range(0,len(self.item1)):
                for j in range(0,len(self.item2)):
                    self.mlist.append([[self.item2[j],self.item1[i]],None])
    def __del__(self):
        pass    
         #insert
    def remove_row(self,z):
        if self.b!=z:
            print("label not defined")
        else:
            self.b.remove(z)
            for i in self.mlist:
                if z==i[0][1]:
                    self.mlist.remove([[i[0][0],i[0][1]],i[1]])
    def remove_column(self,z):
        if z!=self.a:
            print("lable not defined")
        else:
            self.a.remove(z)
            for i in self.mlist:
                if z==i[0][0]:
                    self.mlist.remove([[i[0][0],i[0][1]],i[1]])
    def add_row(self,z):
        if z==self.b:
            print("label already exist")
        else:
            for i in self.a:
                self.mlist.append([[i,z],None])
            self.b.append(z)       
    def add_column(self,z):
        if z==self.b:
            print("label already exist")
        else:
            for i in self.b:
                self.mlist.append([[z,i],None])
            self.a.append(z)                          
    def insert_data(self,a,c,b):
        if (a in self.item1 and c in self.item2) or (c in self.item1 and a in self.item2):
            for i in self.mlist:
                if [a,c] in i:
                    i[1]=b
        else:
            print("label not defined")
    def insert_datalist(self,a,b):
        k=0
        for i in self.mlist:
            if a ==i[0][0]:
                if k>=len(b):
                    break
                i[1]=b[k]
                k=k+1
        for i in self.mlist:
            if a==i[0][1]:
                if k>=len(b):
                    break
                i[1]=b[k]
                k=k+1                
    def show_datalist(self,a):
        s=[self.name]+[a]
        l=[]
        k=0
        for i in self.a:
            for j in self.mlist:     
                if i==j[0][0] and a==j[0][1]:
                    k=1
                    l.append([j[0][0]]+[j[1]])
        for i in self.b:
            for j in self.mlist:     
                if i==j[0][1] and a==j[0][0]:
                    k=1
                    l.append([j[0][1]]+[j[1]])
        print(tabulate(l,headers=s,missingval="none",tablefmt="grid"))
        if k==0:
            print("label not defined")           
    def get_datalist(self,a):
        h=[]
        for i in self.mlist:
            if a == i[0][0]:
                k=1
                h.append(i[1])
        for i in self.mlist:
            if a == i[0][1]:
                k=1
                h.append(i[1])
        return h    
    def get_data(self,v,z):
        for i in self.mlist:
            if [v,z] in i:
                k=1
                return i[1]
        return "label not defined"
    def sum(self,a):
        k=0
        for i in self.mlist:
            if a == i[0][0]:
                if i[1]==None:
                    continue
                k=k+i[1]                
        for i in self.mlist:
            if a == i[0][1]:
                if i[1]==None:
                    continue
                k=k+i[1]   
        return k
    def average(self,a):
        k=0
        g=0
        for i in self.mlist:
            if a == i[0][0]:
                if i[1]==None:
                    continue
                k=k+i[1]
                g=g+1                
        for i in self.mlist:
            if a == i[0][1]:
                if i[1]==None:
                    continue
                k=k+i[1]
                g=g+1   
        return k/g                                             
    def __str__(self):
        headers=[self.name]+self.a
        table=[]
        for i in self.b:
            k=[]
            for j in self.mlist:
                if i==j[0][1]:
                    k.append(j[1])
            table.append([i]+k)         
        return tabulate(table,headers=headers,missingval="None",tablefmt="grid")
