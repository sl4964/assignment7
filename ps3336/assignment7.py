import sys
from intervalclass import interval

if __name__=="__main__":
    while True:
        try:
            input_string = input("List of intervals? ")
            if input_string == "quit":
                sys.exit(1)
            input_string = input_string.replace(" ","")
            string_list = input_string.split(",")
            list_interval=[]
            for i in range(0,len(string_list),2):
                list_interval.append(interval(string_list[i]+','+string_list[i+1]))
            list_interval = interval.mergeOverlapping(list_interval)
            print (interval.to_string(list_interval))
            break
        except KeyboardInterrupt:
            sys.exit(1)
        except Exception:
            print ('Invalid list of intervals')
            pass
    while True:
        try:
            inp = input("Interval? ")
            if inp =="quit":
                sys.exit(1)
                break
            else:
                inp = interval(inp)
                list_interval = interval.insert(list_interval,inp)
                print (interval.to_string(list_interval))
        except KeyboardInterrupt:
            sys.exit(1)
        except Exception:
            print ("Invalid interval")
        