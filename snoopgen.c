#include <stdio.h>
#include <strings.h>

#define STABLE	0
#define VALID	1
#define QUAL	2
#define CLOCK	3
#define WIERD	4

#define INPUT	0
#define OUTPUT	1
#define INOUT	2
#define NEITHER	3

#define BUFSIZE 1000

#define MAXPHASES 4

typedef struct namestruct {
  char *name;
  int ttype, phase;
  int direction;
  int isvector, index1, index2;
  int controldir;
  struct namestruct *controlname, *rsimname;
  struct namestruct *next, *argnext;
} Name;

Name *inlist = 0, *outlist = 0, *bilist = 0, *arglist = 0, *arglistend = 0;
Name *clock[MAXPHASES];

int numclocks = 0;

char *duplicate(string)
char *string;
{
  char *tmp = (char *)malloc(strlen(string)+2);
  strcpy(tmp, string);
  return tmp;
}

addarg(name)
Name *name;
{
  Name *tmp = name;
  if (!arglist) {
    arglist = name;
    arglistend = name;
  } else {
    for (tmp=arglist; tmp; tmp=tmp->argnext)
      if (!strcmp(tmp->name,name->name)) return;
    arglistend->argnext = name;
    arglistend = name;
  }
}

Name *parsettype(string)
char *string;
{
  int length = strlen(string);
  Name *tmp = (Name *)calloc(sizeof(Name), 1);
  char *c;
  
  tmp->name = duplicate(string);
  c = rindex(string, '_');
  c++;
  if (*c == 's') tmp->ttype = STABLE;
  else if (*c == 'v') tmp->ttype = VALID;
  else if (*c == 'q') tmp->ttype = QUAL;
  else {
      tmp->ttype = WIERD;
      fprintf (stderr, "Warning: Can't determine timing type of %s\n", string);
  }
  c++;
  tmp->phase = *c - '0';
  return tmp;
}

parseindex(name)
Name *name;
{
  char *lbrackp = index(name->name, '[');
  int lbrack = lbrackp - name->name;

  if ((name->name[0]=='\\')||(!lbrackp)) {
    name->isvector = 0;
    return;
  }
  name->isvector = 1;
  if (sscanf(name->name+lbrack+1, "%d:%d",
	     &(name->index1), &(name->index2))!=2) {
    fprintf(stderr, "Warning: Cannot parse index for %s\n", name->name);
  }
  name->name[lbrack] = '\0';
}

addInput(num, string1, string2)
int num;
char *string1, *string2;
{
  Name *tmp = (Name *)calloc(sizeof(Name), 1);

  tmp->name = duplicate(string1);
  tmp->direction = INPUT;
  if (num==3) {
    tmp->rsimname = (Name *)calloc(sizeof(Name), 1);
    tmp->rsimname->name = duplicate(string2);
  } else {
    tmp->rsimname = tmp;
  }
  tmp->next = inlist;
  inlist = tmp;
  addarg(tmp);
  parseindex(tmp);
}

addOutput(num, string1, string2)
int num;
char *string1, *string2;
{
  Name *tmp = parsettype(string1);

  tmp->direction = OUTPUT;
  if (num==3) {
    tmp->rsimname = (Name *)calloc(sizeof(Name), 1);
    tmp->rsimname->name = duplicate(string2);
  } else {
    tmp->rsimname = tmp;
  }
  tmp->next = outlist;
  outlist = tmp;
  addarg(tmp);
  parseindex(tmp);
}

addBidir(num, string1, string2, string3, string4)
int num;
char *string1, *string2, *string3, *string4;
{
  Name *tmp = parsettype(string3);

  tmp->direction = INOUT;
  if (num==5) {
    tmp->rsimname = (Name *)calloc(sizeof(Name), 1);
    tmp->rsimname->name = duplicate(string4);
  } else {
    tmp->rsimname = tmp;
  }
  tmp->controlname = (Name *)calloc(sizeof(Name), 1);
  tmp->controlname->name = duplicate(string1);
  tmp->controldir = (string2[0]=='i');
  tmp->next = bilist;
  bilist = tmp;
  addarg(tmp);
  addarg(tmp->controlname);
  parseindex(tmp);
}

addClock(num, string1, string2, string3)
int num;
char *string1, *string2;
{
  Name *tmp = (Name *)calloc(sizeof(Name), 1);
  int length = strlen(string1);

  if ((string1[length-1]<'0')||(string1[length-1]>'9')) {
    fprintf("Warning: Cannot determine phase of %s\n", string2);
  }
  tmp->phase = string1[length-1] - '0';
  if (tmp->phase > numclocks) numclocks = tmp->phase;
  tmp->name = duplicate(string1);
  if (num==4) {
    tmp->rsimname = (Name *)calloc(sizeof(Name), 1);
    tmp->rsimname->name = duplicate(string2);
  } else {
    tmp->rsimname = tmp;
  }
  clock[tmp->phase] = tmp;
  addarg(tmp);
}

prolog(progname, filename)
char *progname, *filename;
{
  printf("\n// Produced by %s from file %s\n", progname, filename);
  printf("\n// Remember to run Verilog with -x");
  printf(" if any variables are subscripted\n\n\n");
}

commentout()
{
  Name *tmp;
  int i;

  printf("// %d Clock phases:", numclocks);
  for (i=1; i<=numclocks; i++) {
    printf(" %s", clock[i]->name);
  }
  printf("\n");
  for (tmp=inlist; tmp; tmp=tmp->next) {
    printf("// Input, Verilog: %s, irsim: %s",
	   tmp->name, tmp->rsimname->name);
    if (tmp->isvector)
      printf(", vector[%d:%d]\n", tmp->index1, tmp->index2);
    else
      printf("\n");
  }
  for (tmp=outlist; tmp; tmp=tmp->next) {
    printf("// Output, Verilog: %s, irsim: %s, ",
	   tmp->name, tmp->rsimname->name);
    if (tmp->isvector)
      printf("vector[%d:%d], ", tmp->index1, tmp->index2);
    if (tmp->ttype == VALID) printf("Valid phase %d\n", tmp->phase);
    else if (tmp->ttype == STABLE) printf("Stable phase %d\n", tmp->phase);
    else if (tmp->ttype == QUAL) printf("Qualified phase %d\n", tmp->phase);
    else printf("Wierd??\n");
  }
  for (tmp=bilist; tmp; tmp=tmp->next) {
    printf("// Inout, Verilog: %s, irsim: %s, ",
	   tmp->name, tmp->rsimname->name);
    if (tmp->isvector)
      printf("vector[%d:%d], ", tmp->index1, tmp->index2);
    if (tmp->ttype==VALID) printf("Valid phase %d\n", tmp->phase);
    else if (tmp->ttype==STABLE) printf("Stable phase %d\n", tmp->phase);
    else printf("Wierd??\n");
  }
}

header()
{
  Name *tmp;
  int brk = 0;

  printf("\n\nmodule snooper(");
  for (tmp=arglist; tmp; tmp=tmp->argnext) {
    if (!(brk++%4)) printf("\n\t");
    printf("%s", tmp->name);
    if (tmp->argnext) printf(", ");
  }
  printf(");\n\n");
  for (tmp=arglist; tmp; tmp=tmp->argnext) {
    printf("input ");
    if (tmp->isvector) printf("[%d:%d] ", tmp->index1, tmp->index2);
    printf("%s;\n", tmp->name);
  }
}

loginputs()
{
  Name *tmp;
  int i;

  printf("\n// One always block per input\n\n");
  for (tmp=inlist; tmp; tmp=tmp->next)
    if (tmp->isvector) {
      printf("always @(%s)\nbegin\n", tmp->name);
      for (i=tmp->index1; i>=tmp->index2; i--) {
      printf("\t$rsim_log_input(%s[%d], \"%s[%d]\");\n",
	     tmp->name, i, tmp->rsimname->name, i);
      }
      printf("end\n");
    } else {
      printf("always @(%s) $rsim_log_input(%s, \"%s\");\n",
	     tmp->name, tmp->name, tmp->rsimname->name);
    }
  printf("\n// One always block per inout\n\n");
  for (tmp=bilist; tmp; tmp=tmp->next)
    if (tmp->isvector) {
      printf("always @(%s or %s)\n\tif (%s == %d)\n\tbegin\n",
	     tmp->name, tmp->controlname->name,
	     tmp->controlname->name, tmp->controldir);
      for (i=tmp->index1; i>=tmp->index2; i--)
	printf("\t$rsim_log_input(%s[%d], \"%s[%d]\");\n",
	       tmp->name, i, tmp->rsimname->name, i);
      printf("\tend\n");
    } else {
      printf("always @(%s or %s)\n\tif (%s == %d) ",
	     tmp->name, tmp->controlname->name,
	     tmp->controlname->name, tmp->controldir);
      printf("$rsim_log_input(%s, \"%s\");\n",
	     tmp->name, tmp->rsimname->name);
    }
}

letgo()
{
  Name *tmp;
  int i;

  printf("\n// Let go of inouts\n\n");
  for (tmp=bilist; tmp; tmp=tmp->next) {
    printf("always @(%s %s)",
	   tmp->controldir ? "negedge" : "posedge", tmp->controlname->name);
    if (tmp->isvector) {
      printf("\nbegin\n");
      for (i=tmp->index1; i>=tmp->index2; i--)
	printf("\t$rsim_update_value(\"%s[%d]\",\"x\");\n",
	       tmp->rsimname->name, i);
      printf("end\n");
    } else {
      printf(" $rsim_update_value(\"%s\",\"x\");\n",
	     tmp->rsimname->name);
    }
  }
}

check()
{
    Name *tmp;
    int i,c;
    
    printf("\n// Check stable signals\n\n");
    for (c=1; c<=numclocks; c++) {
	printf("always @(%s)\nbegin\n", clock[c]->name);
	for (tmp=outlist; tmp; tmp=tmp->next)
	    if ((tmp->ttype==STABLE)&&(tmp->phase==c)) {
		if (tmp->isvector) {
		    for (i=tmp->index1; i>=tmp->index2; i--)
			printf("\t$rsim_log_output(%s[%d], \"%s[%d]\");\n",
			    tmp->name, i, tmp->rsimname->name, i);
	} else {
	    printf("\t$rsim_log_output(%s, \"%s\");\n",
		tmp->name, tmp->rsimname->name);
	}
	    }
	for (tmp=bilist; tmp; tmp=tmp->next)
	    if ((tmp->ttype==STABLE)&&(tmp->phase==c)) {
		if (tmp->isvector) {
		    printf("\tif (%s == %d)\n\tbegin\n",
			tmp->controlname->name, !tmp->controldir);
		    for (i=tmp->index1; i>=tmp->index2; i--)
			printf("\t$rsim_log_output(%s[%d], \"%s[%d]\");\n",
			    tmp->name, i, tmp->rsimname->name, i);
		    printf("\tend\n");
		} else {
		    printf("\tif (%s == %d)\n",
			tmp->controlname->name, !tmp->controldir);
		    printf("\t\t$rsim_log_output(%s, \"%s\");\n",
			tmp->name, tmp->rsimname->name);
		}
	    }
	printf("end\n\n");
    }
    printf("\n// Check valid signals\n\n");
    for (c=1; c<=numclocks; c++) {
	printf("always @(negedge %s)\nbegin\n", clock[c]->name);
	for (tmp=outlist; tmp; tmp=tmp->next)
	    if ((tmp->ttype==VALID)&&(tmp->phase==c)) {
		if (tmp->isvector) {
		    for (i=tmp->index1; i>=tmp->index2; i--)
			printf("\t$rsim_log_output(%s[%d], \"%s[%d]\");\n",
			    tmp->name, i, tmp->rsimname->name, i);
		} else {
		    printf("\t$rsim_log_output(%s, \"%s\");\n",
			tmp->name, tmp->rsimname->name);
		}
	    }
	for (tmp=bilist; tmp; tmp=tmp->next)
	    if ((tmp->ttype==VALID)&&(tmp->phase==c)) {
		if (tmp->isvector) {
		    printf("\tif (%s == %d)\n\tbegin\n",
			tmp->controlname->name, !tmp->controldir);
		    for (i=tmp->index1; i>=tmp->index2; i--)
			printf("\t$rsim_log_output(%s[%d], \"%s[%d]\");\n",
			    tmp->name, i, tmp->rsimname->name, i);
		    printf("\tend\n");
		} else {
		    printf("\tif (%s == %d)\n",
			tmp->controlname->name, !tmp->controldir);
		    printf("\t\t$rsim_log_output(%s, \"%s\");\n",
			tmp->name, tmp->rsimname->name);
		}
	    }
	printf("end\n\n");
    }
    
    printf("\n// Check qualified signals\n\n");
    for (c=1; c<=numclocks; c++) {
	printf("always @(%s)\nbegin\n", clock[c]->name);
	for (tmp = outlist; tmp; tmp = tmp->next)
	    if ((tmp->ttype == QUAL) && (tmp->phase == c)) {
		if (tmp->isvector) {
		    for (i = tmp->index1; i >= tmp->index2; i--)
			printf("\t$rsim_log_output(%s[%d], \"%s[%d]\");\n",
			    tmp->name, i, tmp->rsimname->name, i);
		} else {
		    printf("\t$rsim_log_output(%s, \"%s\");\n",
			tmp->name, tmp->rsimname->name);
		}
	    }
	for (tmp = bilist; tmp; tmp = tmp->next)
	    if ((tmp->ttype == QUAL) && (tmp->phase == c)) {
		if (tmp->isvector) {
		    printf("\tif (%s == %d)\n\tbegin\n",
			tmp->controlname->name, !tmp->controldir);
		    for (i = tmp->index1; i >= tmp->index2; i--)
			printf("\t$rsim_log_output(%s[%d], \"%s[%d]\");\n",
			    tmp->name, i, tmp->rsimname->name, i);
		    printf("\tend\n");
		} else {
		    printf("\tif (%s == %d)\n",
			tmp->controlname->name, !tmp->controldir);
		    printf("\t\t$rsim_log_output(%s, \"%s\");\n",
			tmp->name, tmp->rsimname->name);
		}
	    }
	printf("end\n\n");
    }
}


main(argc, argv)
int argc;
char *argv[];
{
  FILE *infile;
  int lineno;
  int strings;
  char buffer[BUFSIZE];
  char string0[BUFSIZE];
  char string1[BUFSIZE];
  char string2[BUFSIZE];
  char string3[BUFSIZE];
  char string4[BUFSIZE];

  if (argc!=2) {
    fprintf(stderr, "Usage: %s infile\n", argv[0]);
    exit(1);
  }
  if (!(infile=fopen(argv[1], "r"))) {
    fprintf(stderr, "%s: cannot open %s\n", argv[0], argv[1]);
    exit(1);
  }
  lineno = 0;
  while (!feof(infile)) {
    lineno++;
    if (!fgets(buffer, BUFSIZE, infile)) break;
    strings = sscanf(buffer, "%s%s%s%s%s",
		     string0, string1, string2, string3, string4);
    if (!strcmp(string0, "i")) addInput(strings, string1, string2);
    else if (!strcmp(string0, "o")) addOutput(strings, string1, string2);
    else if (!strcmp(string0, "b"))
      addBidir(strings, string1, string2, string3, string4);
    else if (!strcmp(string0, "c"))
      addClock(strings, string1, string2, string3);
    else if (!strcmp(string0, ""))
	;
/*      printf("Skipping line number %d, because it is empty.\n",lineno);*/
    else {
      fprintf(stderr, "%s: Expected c, i, o, or b at line %d: %s",
	      argv[0], lineno, buffer);
      exit(1);
    }

    /* re-initialize strings */
    strcpy(string0,"");
    strcpy(string1,"");
    strcpy(string2,"");
    strcpy(string3,"");
    strcpy(string4,"");


  }
  fclose(infile);
  prolog(argv[0], argv[1]);
  commentout();
  header();
  printf("\ninitial\nbegin\n\t$rsim_init();\n\t$rsim_check_on();\nend\n");
  loginputs();
  letgo();
  check();
  printf("\n\nendmodule\n");
}

