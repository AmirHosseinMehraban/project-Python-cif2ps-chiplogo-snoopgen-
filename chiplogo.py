def find_error(array,error,x,y,width,space):
    tmp=0
    k=0
    tmp1=0
    for i in range(ARRAY_XSIZE+1):
        for j in range(ARRAY_YSIZE+1):
            error[i][j]=0
def display_array(x,y):
  j=0
  row,column,j
  print("Here is an approximate view of what you will get!!\n\n")
  if(view_array==1000): 
    j=y/80+1
  else: 
    j=view_array
  for row in range(0,y,j):
    for column in range(0,x,j):
      if array[column][row] == 1:
        print("*")
      else: 
        print(" ")
    print('\n')
#define ARRAY_SIZE 1024
min_width=2
min_space=2
thresh_before=4
thresh_after=4
scale_factor=1
cif_choice=0
magic_choice=1
cif_lambda=50
error_correct=0
smooth_before=0
smooth_after=0
image_out[ARRAY_SIZE]
ARRAY_XSIZE=1
ARRAY_YSIZE=1
#char *input_file,*output_file,*cif_layer,*magic_layer,*magic_tech;
DEBUG=0
view_array=1000
array[ARRAY_SIZE]
array2[ARRAY_SIZE]
cif=0
magic=0
input=0
output=0
x_corner
y_corner
def main(argc,argv):#define main function for argc and argv
  cif_layer=""
  input_file=""
  output_file=""
  s=""
  magic_tech=""
  magic_layer=""
  tmp=""
  cif_layer+="CPG"
  magic_layer+="poly"
  magic_tech+="scmos"
  while ((argc-1) and (argv+1 ) and (argv == '-')):#maybe change after
    argc-=1
    argv+=1
    s=argv[0]+1
    if s=='m':
      magic=1;
      argv+=1
      magic_layer+=argv
      argc-=1
    elif s=='c':
      cif=1
      argv+=1
      output_file +="logo.cif"
      cif_layer +=argv
      argc-=1
    elif s=='t':
      argc-=1
      argv+=1
      magic_tech+=argv
    elif s=='v':
      view_array=int(argv+1)
      argc-=1
    elif s=='A':
      thresh_after=int(argv+1)
      smooth_after=1
      argc-=1
    elif s=='B':
      thresh_before=int(argv+1)
      smooth_before=1
      argc-=1
    elif s=='h':
      error_mess()
    elif s=='e':
      error_correct=1;
    elif s=='w':
      min_width=int(argv+1)
      argc-=1
    elif s=='s':
      scale_factor=float(argv+1)
      argc-=1
    else:
      break
  if (argc):
    input=1;
    argv+=1
    input_file+=argv
    argc-=1
    if((fpin=fopen(input_file,"r")) == NULL) {
      printf("cannot open input file \n");
      exit(1);
    }
    fclose(fpin);





