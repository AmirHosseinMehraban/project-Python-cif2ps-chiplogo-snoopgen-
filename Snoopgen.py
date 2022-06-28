 STABLE	 = 0
 VALQUAL = 2
 CLOCK = 3
WIERD = 4

INPUT = 0
OUTPUT = 1
INOUT = 2
NEITHER = 3

BUFSIZE =  1000

MAXPHASES  = 4
class Name(object):
    __slots__ = ['name;', 'direction' , 'isvector' , 'index1' , 'index2' , 'controldir', 'next']
    self.argnext = None
    self.next = None ; 
    self.controlname, 
    self.rsimname;
    self.ttype ; 



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
    tmp = Name()
    name = name() ; 
    if(!isinstance(arglist , Name)):
        arglist = name ; 
        arglistend = name ; 
    else:
    while(tmp.next!=None):
        tmp = tmp.next
        if tmp.name==name.name :
            return
        arglistend.next = name
        arglistend = name ; ;

def parsettype(string):
    string = ''
    length = len(string)
    tmp = Name() ; 
    char = ''
    tmp.name = duplicate(string)
    c = string.rindex('_')
    c = c + 1  ; 
    if (*c == 's'):
        tmp.ttype = STABLE;
    else if (*c == 'v'):
        tmp.ttype = VALID;
    else if (*c == 'q') :
        tmp.ttype = QUAL;
    else:
        tmp.ttype = WIERD ; 
        fprintf (stderr, "Warning: Can't determine timing type of %s\n", string);
    c = c+1 ; 
    tmp.phase =  c - '0' ; 
    return tmp 

def parseindex(name):
    name = Name()
    lbrackp = name.name.index('[')  
    lbrackp = lbrackp - name.name 
    if((name.name[0]=='\\') or (!lbrackp)):
        name.isvector = 0 
        return
    name.isvector = 1 ;
    if()
    pass
def addInput(num, string1, string2):
    tmp = Name() ; 
    tmp.name = duplicate(string1)
    tmp.direction = INPUT 
    if(num==3):
        tmp2 = Name()
        tmp.rsimname = tmp2  #(Name *)calloc(sizeof(Name), 1);
        tmp.rsimname.name = duplicate(string2)
    else:
        tmp.rsimname = tmp 
    tmp.next = outlist ; 
    outlist = tmp 
    addarg(tmp)
    parsettype(tmp)
def addOutput(num , string1 , string2):
    tmp = Name()
    tmp = parsettype(string)
    tmp.direction = OUTPUT
    if(num==3):
        tmp.rsimname = Name()
        tmp.rsimname.name = duplicate(string2)
    else:
        tmp.rsimname = tmp 
    tmp.next = outlist 
    outlist = tmp 
    addarg(tmp)
    parseindex(tmp)

def addBidir(name , string1 , string2, string3 , string4):
    tmp = Name() 
    tmp = parsettype(string3)
    tmp.direction = INOUT ; 
    if(num==5):
        tmp1 = Name() 
        tmp.rsimname = tmp1 
        tmp.rsimname.name = duplicate(String4)
    else:
        tmp.rsimname = tmp
    tmp2 = Name() 
    tmp.controlname = tmp2 
    tmp.controlname.name = duplicate(string1)
    tmp.controldir = (string2[0]=='i'):
    tmp.next = bilist ; 
    bilist = tmp 
    addarg(tmp)
    addarg(tmp.controlname)
    parseindex(tmp)
def addClock(num, string1, string2, string3):
    temp = Name()
    length = len(string1)
    if ((string1[length-1]<'0')||(string1[length-1]>'9')) {
    fprintf("Warning: Cannot determine phase of %s\n", string2);
  }
    tmp.phase = string1[length-1] - '0'
    if(tmp.phase > numclocks):
        numclocks = tmp.phase 
    tmp.name = duplicate(string1)
    if(num==4):
        temp2 = Name()
        tmp.rsimname = temp2 
        tmp.rsimname.name = duplicate(string2)

    else:
        tmp.rsimname = tmp 
    clock[tmp.phase] = tmp
    addarg(tmp)


def prolog(progname , filename):
    printf("\n// Produced by %s from file %s\n", progname, filename);
    printf("\n// Remember to run Verilog with -x");
    printf(" if any variables are subscripted\n\n\n");
def commentout():
