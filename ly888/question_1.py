class interval(object):
    
    def __init__(self,inter):
        #Remember the interval
        self.inter=inter;
        pre_check=list(inter);
        #Exclude the interval that does not contain '(' or '[' at the beginning or does not contain ')' or ']' at the end or does not contain ","
        if pre_check[0] in ('(','[') and pre_check[-1] in (')',']') and "," in pre_check:
            #Find the lower and upper value of the interval
            lower_str=inter[1:-1].split(",")[0];
            upper_str=inter[1:-1].split(",")[1];
            #If the lower value and upper value is not integer, the interval is not valid
            if lower_str.lstrip('-').isdigit() and upper_str.lstrip('-').isdigit():
                lower=int(lower_str);
                upper=int(upper_str);
            else:
                lower=1;
                upper=-1;
        else:
            lower=1;
            upper=-1;
            
        #Find the left and right bracket of the interval
        bracket=list(inter);
        b_left=bracket[0];
        b_right=bracket[-1];
        #Find the smallest and largest integers for the input interval according to left anf right bracket
        if b_left=='(' and b_right==')':
            self.lower=lower+1;
            self.upper=upper-1;
        elif b_left=='[' and b_right==']':
            self.lower=lower;
            self.upper=upper;    
        elif b_left=='(' and b_right==']':
            self.lower=lower+1;
            self.upper=upper;
        elif b_left=='[' and b_right==')':
            self.lower=lower;
            self.upper=upper-1;
        else:
            self.lower=1;
            self.upper=-1;
            
    def __repr__(self):
        #Define the output statement if the interval is valid
        str="%s represents the numbers" %self.inter
        str=str + " %d to" %self.lower
        str=str + " %d" %self.upper
        #If the interval is not valid, output "The interval is not valid"
        try: 
            if self.upper>=self.lower:
                return str
            else:
                raise ValueError('The interval is not valid')
            return str
        except:
            return 'The interval is not valid'
