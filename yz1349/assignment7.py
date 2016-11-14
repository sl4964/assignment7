import sys
from interval import interval,insert

if __name__=="__main__":
    while True:
        try:
            inputstring = raw_input("List of intervals? ")
            if inputstring == "quit":
                sys.exit()
            inputstring = inputstring.replace(" ","")
            stringlist  = inputstring.split(",")
            intervallist=[]
            for index in range(0,len(stringlist),2):              
                thisstring = stringlist[index]+","+stringlist[index+1]
                intervallist.append(interval(thisstring))
            break
        except KeyboardInterrupt:
            sys.exit()
        except Exception:
            print ('Invalid list input')
            pass
    while True:
        try:
            inputint = raw_input("Interval? ")
            if inputint =="quit":
                sys.exit()
            inputint = interval(inputint)
            intervallist = insert(intervallist,inputint)
            for thisint in intervallist:
                print(thisint), 
            print("")              
        except KeyboardInterrupt:
            sys.exit()
        except Exception:
            print ("Invalid interval")


