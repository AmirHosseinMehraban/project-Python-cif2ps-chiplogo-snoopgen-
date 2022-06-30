import sys
STABLE = 0
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
    __slots__ = ['name', 'direction' , 'isvector' , 'index1' , 'index2' , 'controldir', 'next']
    self.ttype ; 
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
    tmp = Name()
    i = 1  ; 
    printf("// %d Clock phases:", numclocks);
    for i in range(numclocks):
        printf(" %s", clock[i].name);
    printf("\n");
    while(tmp.next!=None):
        printf("// Input, Verilog: %s, irsim: %s",
	    tmp.name, tmp.rsimname.name);
        tmp.next = tmp
        if (tmp.isvector):
            printf(", vector[%d:%d]\n", tmp.index1, tmp.index2);
        else:
            printf("\n");
    tmp = outlist
    while(tmp.next!=None):
        printf("// Output, Verilog: %s, irsim: %s, ",tmp->name, tmp->rsimname->name);
        if(tmp.isvector):
            printf("vector[%d:%d], ", tmp->index1, tmp->index2);
        if(tmp.ttype==VALID):
            printf("Valid phase %d\n", tmp->phase);
        elif (tmp.ttype == STABLE) printf("Stable phase %d\n", tmp->phase);
        elif (tmp.ttype == QUAL) printf("Qualified phase %d\n", tmp->phase);
        else printf("Wierd??\n");
        tmp.outlist = tmp 
    tmp = bilist
    while(tmp.next!=None):
        printf("// Inout, Verilog: %s, irsim: %s, ",
	    tmp->name, tmp->rsimname->name);
        if (tmp.isvector):
            printf("vector[%d:%d], ", tmp->index1, tmp->index2);
        if (tmp.ttype==VALID):
            printf("Valid phase %d\n", tmp->phase);
        elif(tmp.ttype==STABLE):
            printf("Stable phase %d\n", tmp->phase);
        else: 
            printf("Wierd??\n")
        tmp.next = tmp ; 
def header():
    tmp = Name()
    brk = 0 
    printf("\n\nmodule snooper(");
    tmp=arglist
    while(tmp.argnext!=None):
        if (!(brk++%4)):
        printf("\n\t");
        printf("%s", tmp.name);
        if(tmp.argnext):
            printf("%s", tmp->name);
    printf(");\n\n");
    tmp = arglist 
    while(tmp.argnext!=None):
        printf("input ");
        if (tmp.isvector) :
            printf("[%d:%d] ", tmp->index1, tmp->index2);
        printf("%s;\n", tmp->name);
def loginputs():
    tmp = Name()
    i = 0 ; 
    printf("\n// One always block per input\n\n");
    tmp = inlist ;
    while(tmp.next!=None):
        if (tmp->isvector) {
            printf("always @(%s)\nbegin\n", tmp.name)
            i1 = tmp.index1 
            j1 = tmp.index2
            for i1 in range(i1 , j1 , -1):
                printf("\t$rsim_log_input(%s[%d], \"%s[%d]\");\n",tmp->name, i, tmp->rsimname->name, i);
            printf("\tend\n");
        else:
            printf("always @(%s or %s)\n\tif (%s == %d) ",tmp->name, tmp->controlname->name,tmp->controlname->name, tmp->controldir);
            printf("$rsim_log_input(%s, \"%s\");\n",tmp->name, tmp->rsimname->name);
def letgo():
    tmp = Name()
    printf("\n// Let go of inouts\n\n");
    tmp = bilist 
    while(tmp.next!=None):
        printf("always @(%s %s)",tmp->controldir ? "negedge" : "posedge", tmp->controlname->name);
        if(tmp.isvector):
            printf("\nbegin\n");
            i1 = tmp.index1 
            j1 = tmp.index2 
            for i in range(i1 , j1 , -1):
                printf("\t$rsim_update_value(\"%s[%d]\",\"x\");\n",tmp->rsimname->name, i);
            printf("end\n");
        else:
            printf(" $rsim_update_value(\"%s\",\"x\");\n",tmp->rsimname->name);
def check():
    i = 0  , c = 1  ;
    tmp = Name()
    printf("\n// Check stable signals\n\n");
    for c in range (1,numclocks):
	    printf("always @(%s)\nbegin\n", clock[c]->name);
        tmp = outlist ; 
        while(tmp.next!=None):
            if ((tmp.ttype==STABLE)and(tmp.phase==c)):
                if (tmp->isvector):
                    i1 = tmp.index1
                    j1 = tmp.index2 
                    for i in range(i1, j1 , -1 ):
                        printf("\t$rsim_log_output(%s[%d], \"%s[%d]\");\n",tmp->name, i, tmp->rsimname->name, i);
                else:
                    printf("\t$rsim_log_output(%s, \"%s\");\n",tmp->name, tmp->rsimname->name);
        tmp = bilist  
        while(tmp.next!=None):
            if((tmp.ttype==STABLE)and(tmp.phase==c)):
                if(tmp.isvector):
                    printf("\tif (%s == %d)\n\tbegin\n",tmp->controlname->name, !tmp->controldir);
                    i1 = tmp.index1  ; 
                    j1 = tmp.index2 ; 
                    for i in range(i1 , j1 , -1 ):
                        printf("\t$rsim_log_output(%s[%d], \"%s[%d]\");\n",tmp->name, i, tmp->rsimname->name, i);
                    printf("\tend\n");
                else:
                    printf("\tif (%s == %d)\n",tmp->controlname->name, !tmp->controldir);
                    printf("\t\t$rsim_log_output(%s, \"%s\");\n",tmp->name, tmp->rsimname->name);
        printf("end\n\n")
    printf("\n// Check valid signals\n\n");
    for c in range(1,numclocks+1):
        printf("always @(negedge %s)\nbegin\n", clock[c]->name);
        tmp = outlist ; 
        while(tmp.next!=None):
            if ((tmp.ttype==VALID)and(tmp.phase==c)):
                if (tmp->isvector):
                    i1 = tmp.index1 ; 
                    j1 = tmp.index2
                    for i in range(i1 , j1 , -1):
                        printf("\t$rsim_log_output(%s[%d], \"%s[%d]\");\n",tmp->name, i, tmp->rsimname->name, i);
                else:
                    printf("\t$rsim_log_output(%s, \"%s\");\n",tmp->name, tmp->rsimname->name);
        tmp = bilist ; 

        while(tmp.next!= None):
            if ((tmp.ttype==VALID)and(tmp.phase==c)):
                if(tmp.isvector):
                    printf("\tif (%s == %d)\n\tbegin\n",tmp->controlname->name, !tmp->controldir);
                    i1 = tmp.index1 ; 
                    j1 = tmp.index2
                    for i in range(i1,j1,-1):
                        printf("\t$rsim_log_output(%s[%d], \"%s[%d]\");\n",tmp->name, i, tmp->rsimname->name, i);
                        printf("\tend\n")
                else:
                    printf("\tif (%s == %d)\n",tmp->controlname->name, !tmp->controldir);
		            printf("\t\t$rsim_log_output(%s, \"%s\");\n",tmp->name, tmp->rsimname->name);
    	printf("end\n\n");        
    printf("\n// Check qualified signals\n\n");
    for c in range(1,numclocks):
        printf("always @(%s)\nbegin\n", clock[c]->name);
        tmp = outlist
        while(tmp.next!=None):
            if ((tmp.ttype == QUAL) and (tmp.phase == c)):
                if(tmp.isvector):
                    printf("\tif (%s == %d)\n\tbegin\n",tmp->controlname->name, !tmp->controldir);
                    i1 = tmp.index1 ; 
                    j1 = tmp.index2 ; 
                    for i in range(i1,j1,-1):
                        printf("\t$rsim_log_output(%s[%d], \"%s[%d]\");\n",tmp->name, i, tmp->rsimname->name, i);
                    printf("\tend\n");
                else:
                    printf("\tif (%s == %d)\n",tmp->controlname->name, !tmp->controldir);
		            printf("\t\t$rsim_log_output(%s, \"%s\");\n",tmp->name, tmp->rsimname->name);
        printf("end\n\n");

if(len(sys.argv)!=2):
    fprintf(stderr, "Usage: %s infile\n", argv[0]);
    exit()
try:
    infile = open(sys.argv[1] , "r")
except:
    fprintf(stderr, "%s: cannot open %s\n", argv[0], argv[1]);
    exit()
lineo = 0 














                   






    







     




        




    




    



     

    
        






