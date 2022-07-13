import sys
STABLE = 0
QUAL = 2
CLOCK = 3
WIERD = 4
VALID = 1
INPUT = 0
OUTPUT = 1
INOUT = 2
NEITHER = 3

BUFSIZE =  1000

MAXPHASES  = 4
class Name:
    def __init__(self):
        self.name= None
        self.direction = None
        self.isvector = None
        self.index1 = None
        self.index2 = None
        self.controldir = None
        self.next = None
        self.ttype = None
        self.argnext = None
        self.next = None ; 
        self.controlname= None
        self.rsimname= None
        self.phase = None



numclocks = 0;

inlist = Name() 
outlist = Name()
bilist= Name()
arglist = Name()
arglistend = Name();
#Name *clock[MAXPHASES];
clock = [] ; 
for i in range(MAXPHASES) :
    Name1 = Name()
    clock.append(Name1)

def duplicate(string):
    tmp = '' ; 
    tmp = str(string)
    return tmp 

def addarg(name):
    tmp = name
    global arglist
    if(arglist==None):
        arglist = name ; 
        arglistend = name ; 
    else:
        tmp1 = arglist
        while(tmp1.argnext!=None):
            if (tmp1.name==name.name):
                return
            arglistend.argnext = name
            arglistend = name 
            tmp1 = tmp1.argnext
        

def parsettype(string):
    length = len(string)
    tmp = Name() ; 
    char = ''
    tmp.name = duplicate(string)

    try:
        c = string.index('_')
        c = c + 1
        if (string[c] == 's'):
            tmp.ttype = STABLE;
        elif (string[c] == 'v'):
            tmp.ttype = VALID;
        elif (string[c]== 'q') :
            tmp.ttype = QUAL;
    except:
        c = -1
        tmp.ttype = WIERD ; 
        print ("Warning: Can't determine timing type of %s\n", string);
    c = c+1 ; 
    tmp.phase = int(ord(string[c]) - ord('0')) ; 
    return tmp 

def parseindex(name):
    
    try:
        lbrackp = name.name.index('[')  
        lbrack = lbrackp
    except:
        lbrackp = ""
    if((name.name[0]=='\\') or (lbrackp=="")):
        name.isvector = 0 
        name.index1 = 0 
        name.index2 = 0
        return
    name.isvector = 1 ;
    name.index1 = int(name.name[lbrackp+1])
    name.index2 = int(name.name[lbrackp+3])
    name.name =name.name[0:lbrack]
def addInput(num, string1, string2):
    tmp = Name() ; 
    tmp.name = string1
    tmp.direction = INPUT 
    if(len(num)-4==3):
        tmp2 = Name()
        tmp.rsimname = tmp2  #(Name *)calloc(sizeof(Name), 1);
        tmp.rsimname.name = string2
    else:
        tmp.rsimname = tmp 
    global inlist ;
    tmp.next = inlist ; 
    inlist = tmp 
    addarg(tmp)
    parseindex(tmp)
def addOutput(num , string1 , string2):
    tmp = Name()
    tmp = parsettype(string1)
    tmp.direction = OUTPUT
    if(num==3):
        tmp.rsimname = Name()
        tmp.rsimname.name = duplicate(string2)
    else:
        tmp.rsimname = tmp 
    global outlist
    tmp.next = outlist 
    outlist = tmp 
    addarg(tmp)
    parseindex(tmp)

def addBidir(num , string1 , string2, string3 , string4):
    tmp = Name() 
    
   

    tmp = parsettype(string3)
    tmp.direction = INOUT ; 
    #print(num)
    if(len(num)-4==5):
        tmp1 = Name() 
        tmp.rsimname = tmp1 
        tmp.rsimname.name = duplicate(string4)
    else:
        tmp.rsimname = tmp
    tmp2 = Name() 
    tmp.controlname = tmp2 
    tmp.controlname.name = duplicate(string1)
    #print(string2[0] , "IIII")
    tmp.controldir = (string2[0]=='i')
    global bilist
    tmp.next = bilist ; 
    bilist = tmp 
    addarg(tmp)
    addarg(tmp.controlname)
    parseindex(tmp)
def addClock(num, string1, string2, string3):
    tmp = Name()
    length = len(string1)
    if ((string1[length-1]<'0')or(string1[length-1]>'9')) :
        print("Warning: Cannot determine phase of %s\n", string2);
    tmp.phase = ord(string1[length-1]) - ord('0')
    global numclocks
    if(tmp.phase > numclocks):
        numclocks = tmp.phase 
    tmp.name = duplicate(string1)
    if(num==4):
        temp2 = Name()
        tmp.rsimname = temp2 
        tmp.rsimname.name = duplicate(string2)

    else:
        tmp.rsimname = tmp 
    print(tmp.phase , "FFFFF")
    clock[tmp.phase-1] = tmp
    addarg(tmp)


def prolog(progname , filename):
    print("\n// Produced by %s from file %s\n", progname, filename);
    print("\n// Remember to run Verilog with -x");
    print(" if any variables are subscripted\n\n\n");
def commentout():
    tmp = Name()
    i = 1  ; 
    print("// %d Clock phases:"%(numclocks));
    for i in range(numclocks):
        print(" %s"%(clock[i].name));
    print("\n");
    tmp = inlist
    while(tmp.next!=None):
        print("// Input, Verilog: %s, irsim: %s"%(tmp.name, tmp.rsimname.name));
        if(tmp.isvector):
            print("vector[%d:%d], "%(tmp.index1, tmp.index2));
        else:
            print("\n");
        tmp = tmp.next
    tmp = outlist
    while(tmp.next!=None):
        print("// Output, Verilog: %s, irsim: %s, "%(tmp.name, tmp.rsimname.name));
        if(tmp.isvector):
            print("vector[%d:%d], "%(tmp.index1, tmp.index2));
        if(tmp.ttype==VALID):
            print("Valid phase %d\n"%(tmp.phase));
        elif (tmp.ttype == STABLE):
            print("Stable phase %d\n"%(tmp.phase));
        elif (tmp.ttype == QUAL):
            print("Qualified phase %d\n"%(tmp.phase));
        else:
            print(tmp.name)
            print("Wierd??\n");
        tmp = tmp.next 
    tmp = bilist
    while(tmp.next!=None):
        print("// Inout, Verilog: %s, irsim: %s, "%(tmp.name, tmp.rsimname.name));
        if (tmp.isvector):
            print("vector[%d:%d], "%(tmp.index1, tmp.index2));
        if (tmp.ttype==VALID):
            print("Valid phase %d\n"%(tmp.phase));
        elif(tmp.ttype==STABLE):
            print("Stable phase %d\n"%(tmp.phase));
        else: 
            print("Wierd??\n")
        tmp = tmp.next; 
def header():
    tmp = Name()
    brk = 0 
    print("\n\nmodule snooper(");
    tmp=arglist
    print(tmp.argnext , "Sdddd")
    while(tmp.argnext!=None):
        if (((brk+1)%4)==0):
            print("\n\t");
            print("%s"%(tmp.name));
        if(tmp.argnext):
            print("%s"%(tmp.name));
        tmp = tmp.argnext
    print(");\n\n")

    tmp = arglist 
    while(tmp.argnext!=None):
        print("input ");
        if (tmp.isvector) :
            print("[%d:%d] "%(tmp.index1, tmp.index2));
        print("%s;\n"%(tmp.name));
        tmp = tmp.argnext
def loginputs():
    tmp = Name()
    tmp = inlist
    while(tmp.next!=None):
        if (tmp.isvector):
            print("always @(%s)\nbegin\n"%(tmp.name));
            j = tmp.index1 
            i = tmp.index2
            for h in range(i , j+1):
                print("\t$rsim_log_input(%s[%d], \"%s[%d]\");\n"%(tmp.name, h, tmp.rsimname.name, h));
            print("end\n");
        else:
            print("always @(%s) $rsim_log_input(%s, \"%s\");\n"%(tmp.name, tmp.name, tmp.rsimname.name));
        tmp = tmp.next
    tmp = bilist
    while(tmp.next!=None):
        if (tmp.isvector):
            print("always @(%s or %s)\n\tif (%s == %d)\n\tbegin\n"%(tmp.name, tmp.controlname.name,tmp.controlname.name, tmp.controldir));
            for i in range(tmp.index1 , tmp.index2-1 , -1):
                print("\t$rsim_log_input(%s[%d], \"%s[%d]\");\n"%(tmp.name, i, tmp.rsimname.name, i));
            print("\tend\n");
        else:
            print("always @(%s or %s)\n\tif (%s == %d) "%(tmp.name, tmp.controlname.name,tmp.controlname.name, tmp.controldir));
            print("$rsim_log_input(%s, \"%s\");\n"%(tmp.name, tmp.rsimname.name));
        tmp = tmp.next
def letgo():
    tmp = Name()
    print("\n// Let go of inouts\n\n");
    tmp = bilist 
    while(tmp.next!=None):
        print("always @(%s %s)"%(tmp.controldir if "negedge" else "posedge", tmp.controlname.name));
        if(tmp.isvector):
            print("\nbegin\n");
            i1 = tmp.index1 
            j1 = tmp.index2 
            for i in range(i1 , j1-1 , -1):
                print("\t$rsim_update_value(\"%s[%d]\",\"x\");\n"%(tmp.rsimname.name, i));
            print("end\n");
        else:
            print(" $rsim_update_value(\"%s\",\"x\");\n"%(tmp.rsimname.name));
        tmp = tmp.next
def check():
    i = 0  
    c = 1  ;
    tmp = Name()
    print("\n// Check stable signals\n\n");
    for c in range (1,numclocks+1):
        print(numclocks)
        tmp = outlist 
        print("always @(%s)\nbegin\n"%(clock[c].name))
        while(tmp.next!=None):
            if ((tmp.ttype==STABLE)and(tmp.phase==c)):
                if (tmp.isvector):
                    i1 = tmp.index1
                    j1 = tmp.index2 
                    for i in range(i1, j1 , -1 ):
                        print("\t$rsim_log_output(%s[%d], \"%s[%d]\");\n"%(tmp.name, i, tmp.rsimname.name, i));
                else:
                    print("\t$rsim_log_output(%s, \"%s\");\n"%(tmp.name, tmp.rsimname.name));
            tmp = tmp.next
        tmp = bilist  
        while(tmp.next!=None):
            if((tmp.ttype==STABLE)and(tmp.phase==c)):
                if(tmp.isvector):
                    print("\tif (%s == %d)\n\tbegin\n"%(tmp.controlname.name, ~tmp.controldir));
                    i1 = tmp.index1  ; 
                    j1 = tmp.index2 ; 
                    for i in range(i1 , j1 , -1 ):
                        print("\t$rsim_log_output(%s[%d], \"%s[%d]\");\n"%(tmp.name, i, tmp.rsimname.name, i));
                    print("\tend\n");
                else:
                    print("\tif (%s == %d)\n"%(tmp.controlname.name, ~tmp.controldir));
                    print("\t\t$rsim_log_output(%s, \"%s\");\n"%(tmp.name, tmp.rsimname.name));
            tmp = tmp.next
        print("end\n\n")
    print("\n// Check valid signals\n\n");
    for c in range(1,numclocks+1):
        print("always @(negedge %s)\nbegin\n"%(clock[c].name));
        tmp = outlist ; 
        while(tmp.next!=None):
            if ((tmp.ttype==VALID)and(tmp.phase==c)):
                if (tmp.isvector):
                    i1 = tmp.index1 ; 
                    j1 = tmp.index2
                    for i in range(i1 , j1 , -1):
                        print("\t$rsim_log_output(%s[%d], \"%s[%d]\");\n"%(tmp.name, i, tmp.rsimname.name, i));
                else:
                    print("\t$rsim_log_output(%s, \"%s\");\n"%(tmp.name, tmp.rsimname.name));
            tmp= tmp.next
        tmp = bilist ; 

        while(tmp.next!= None):
            if ((tmp.ttype==VALID)and(tmp.phase==c)):
                if(tmp.isvector):
                    print("\tif (%s == %d)\n\tbegin\n"%(tmp.controlname.name, ~tmp.controldir));
                    i1 = tmp.index1 ; 
                    j1 = tmp.index2
                    for i in range(i1,j1,-1):
                        print("\t$rsim_log_output(%s[%d], \"%s[%d]\");\n"%(tmp.name, i, tmp.rsimname.name, i));
                        print("\tend\n")
                else:
                    print("\t\t$rsim_log_output(%s, \"%s\");\n"%(tmp.name, tmp.rsimname.name))
                    print("\tif (%s == %d)\n"%(tmp.controlname.name, ~tmp.controldir))
            tmp = tmp.next
    print("end\n\n")       
    print("\n// Check qualified signals\n\n");
    for c in range(1,numclocks+1):
        print("always @(%s)\nbegin\n"%(clock[c].name));
        tmp = outlist
        while(tmp.next!=None):
            if ((tmp.ttype == QUAL) and (tmp.phase == c)):
                if(tmp.isvector):
                    print("\tif (%s == %d)\n\tbegin\n"%(tmp.controlname.name, ~tmp.controldir));
                    i1 = tmp.index1 ; 
                    j1 = tmp.index2 ; 
                    for i in range(i1,j1,-1):
                        print("\t$rsim_log_output(%s[%d], \"%s[%d]\");\n"%(tmp.name, i, tmp.rsimname.name, i));
                    print("\tend\n");
                else:
                    print("\t\t$rsim_log_output(%s, \"%s\");\n"%(tmp.name, tmp.rsimname.name));
                    print("\tif (%s == %d)\n"%(tmp.controlname.name, ~tmp.controldir));
            tmp = tmp.next
        print("end\n\n");


with open("C:\\Users\\Mohammad Zeinalpour\\OneDrive\\Desktop\\snoopgen\\d.txt" , 'r') as infile:
    lines = infile.readlines();
    for line in lines:
        strings = line.split()
        strings.append('')
        strings.append('')
        strings.append('')
        strings.append('')
        if(strings[0]=='i'):
            addInput(strings ,strings[1], strings[2]);
        elif(strings[0]=='o'):
            addOutput(strings[0], strings[1], strings[2]);
        elif(strings[0]=='b'):
            addBidir(strings ,strings[1] ,  strings[2],strings[3],strings[4])
        elif(strings[0]=='c'):
            addClock(strings[0] , strings[1],strings[2],strings[3])
        elif(strings[0]==''):
            pass
        else:
            fprint(stderr, "%s: Expected c, i, o, or b at line %d: %s",argv[0], lineno, buffer);
            exit(1);
        strings = ""


commentout();
header();
print("\ninitial\nbegin\n\t$rsim_init();\n\t$rsim_check_on();\nend\n");
loginputs();
letgo();
check();
        









                   






    







     




        




    




    



     

    
        






