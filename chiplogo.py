from array import array
from fileinput import close


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
    if fpin==open(input_file,"r") == NULL:
      print("cannot open input file \n")
      exit(1)
    
    close(fpin)
  if argc:
    output_file=argv+1
    argv+=1 
    argc-=1
    if (fpout==open(output_file,"w")) == NULL:
      print("cannot open output file \n")
      exit(1)
    close(fpout)
  if argc:  
    error_mess()
    exit(0)
  if input == 0:  
    error_mess()
  if cif ==1 and magic ==1:
    print("\n you can not have both cif and magic options active, just select one\n")
    exit(1)
  if min_width < 1:
    print("\n the minimum width should be an integer grater than '1'\n")
    exit(1)
  chiplogo()
  print("\n   Logo successfully generated \n")
 
  exit(0)
def error_mess():
  print("\n USAGE :\n chiplogo [-c cif_layer_name] [-m magic_layer_name] [-w width] [-s scale] [-t tech_name] [-e] [-v view_array] [-B  threshold_before] [-A threshold_after] input_file [output_file]\n\n")
  print("The options are: \n")
  print(" cif_layer_name   => the cif layer name that you like\n")
  print(" magic_layer_name => the magic layer name\n")
  print(" width            => the minimum width of the layer \n")
  print(" scale            => the scale factor \n")
  print(" tech_name        => the technology name for magic \n")
  print(" e                => toggles the error detection and correction option \n")
  print(" view_factor      => sets the viewing option. 0=NO view, a value greater than or ")
  print("                    equal to one means view with the scaling set at this value \n")
  print(" threshold_before => the threshold value used in the smoothing before error ")
  print("                         correction (from 4 to 16)\n")
  print(" threshold_after  => the threshold value used in the smoothing after error ")
  print("                         correction (from 4 to 16)\n")
  print(" NOTE: The input file should be in the ascii bit map format\n\n")

  print("\n the defaults are as follows:\n\n")
  print("          magic_tech_name   = scmos \n")
  print("          magic_layer_name  = poly \n")
  print("          minimum_width     = 1\n")
  print("          scale             = 1\n")
  print("          error_correct     = 1\n")
  print("          threshold_before  = 4 (max=16) \n")
  print("          magic_output_file = logo.mag \n")
  print("          cif_output_file   = logo.cif \n")
  exit(1)

def chiplogo():
  FILE	*fpin,*fpout
  char	tmp_c
  width=1
  space=1
  scale=1
  tech=0
  x=0
  y=0
  base=1
  junk=0
  int  j,row,column
  max_col=35
  int 	max_row
  int	x_corner,y_corner
  threshold_after=4
  threshold_before=4
  scale=scale_factor
  width=min_width
  space=min_space
  threshold_before=thresh_before
  threshold_after=thresh_after

  if (fpin==open(input_file,"r")) == NULL: 
    print("cannot open input file\n")
    return
  
  
  
  ##tmp= (char *)malloc(2048*sizeof(char));
  if tmp==NULL:
    print("there is not enough memory\n")
    close(fpin)
    return
  
  i=0
  fpin.read(temp)
  if(strcmp(tmp,"P1")):
    print("This doesn't seem like a pbm file, because it doesn't have the P1 header")
  fpin.read(tmp)
  while not strncmp(tmp,"#",1):
    fpin.read("%*[^\n]")
    getc(fpin)
    fpin.read(tmp)

  
  ARRAY_XSIZE = x = int(tmp)
  fpin.read(tmp)
  ARRAY_YSIZE = y = int(tmp)
  if(ARRAY_YSIZE == 0 or  ARRAY_XSIZE ==0):
    close(fpin)
    tmp=""
    print("array has a size of zero\n")
    return
  for k in range(ARRAY_SIZE):
  
    image_out[k]=int(ARRAY_YSIZE+2*width+2)
    if image_out[k]==NULL:
      print("there is not enough memory\n")
      exit(0)
    array[k]=int(ARRAY_YSIZE+2*width+2)
    if array[k]==NULL:
      print("there is not enough memory\n")
      exit(0)
    array2[k]=int(ARRAY_YSIZE+2*width+2)
    if array2[k]==NULL:
      print("there is not enough memory\n")
      exit(0)
    
  max_row=x*y
  max_row+=1
  max_row=max_row/35
  max_row+=1
  row=0
  column=0
  for k in range(x*y):
    fpin.read(array[k-((k/x)*x)][k/x])
    
	#print(k-((k/x)*x),(k/x),array[k-((k/x)*x)][k/x])
  #i have to correct print 
  if DEBUG==1:
    print("before enlarge\n");
  enlarge_array(array,x,y,width+2)
  if(DEBUG==1):
    print("after enlarge\n")
  if(smooth_before==1):
    smooth_array(array,x,y,threshold_before,width)
  
 
  if(error_correct==1):
    if(DEBUG==1):
      print("before error\n")
    find_error(array,array2,x,y,width,space)
    if(DEBUG==1):
      print("after error\n")
    column=0
    for column in range(y):
      row=0
      for row in range(x):
	    array[row][column]=array2[row][column]+array[row][column]
 
  if smooth_after==1:
    smooth_array(array,x,y,threshold_after,width)
  

  if DEBUG==1:
    print("before shrink\n")
  shrink_array(array,x,y,width+2)
  if DEBUG==1:
    print("after shrink\n")
  i=0
  for i in range(ARRAY_XSIZE):
    j=0
    for j in range(ARRAY_YSIZE):
      image_out[i][j]=array[i][j]
    
  
  if(DEBUG==1):
    print("after copy\n")
 
  if magic_choice==1 and cif_choice ==0:
    if (fpout==fopen(output_file,"w")) == NULL: 
        print("cannot open output file\n")
	  #return

      #fprintf(fpout,"magic\ntech  %s\ntimestamp 777777777\n", magic_tech);
      #fprintf(fpout,"<< %s >>\n", magic_layer);
      #for(column=0;column<y;column++){
  row=0
  for row in range(x):
	  if array[row][column] ==1:
	    base=scale
	    y_corner=y-column
	    y_corner=base
	    x_corner=row*base
	    #fprintf(fpout,"rect %d %d %d %d\n",x_corner,y_corner,x_corner+base,y_corner+base);

      #fprintf(fpout,"<< end >>\n");
    else:
      if((fpout=fopen(output_file,"w")) == NULL) {
        print("cannot open output file\n")
        return
    
    #fprintf(fpout,"DS 1 %d 2;\n9 logo;\nL %s;\n", cif_lambda, cif_layer);
    column=0
    for column in range(y):
      row=0
      for row in range(x):
	if array[row][column] ==1:
	  base=10*scale*width;
	  y_corner=y-column;
	  y_corner*=base;
	  x_corner=base*row-width;
 
	  #fprintf(fpout,"B %d %d %d %d;\n",base+2*width,base,x_corner+(base/2),y_corner+(base/2));
    #fprintf(fpout,"DF;\nC 1;\nEnd\n");
  
  if DEBUG==1:
    printf("before free\n")
  display_array(x,y)
  
  i=0
  for i in range(ARRAY_SIZE):
    array[i]=""
    array2[i]=""
  if(DEBUG==1):
    print("after free\n")
  tmp=""
  close(fpin)
  close(fpout)
  if(DEBUG==1):
    print("after close\n")
 
def shrink_array(array,x,y,width)
  for i in range(x+width-1):
    for j in range(y+width-1):
      if(i>width-1 or j>width-1 ):
        array[i][j]=array[i+width][j+width]:
def smooth_array(array,x,y,threshold,width):
  int column,row,*array2[ARRAY_SIZE],tmp,i,j,total=0;
  array2[]
  for i in range(ARRAY_SIZE):
    array2.append(int(ARRAY_YSIZE+2*width))
  for column in range(y):
    for row in range(x):
      array2[row][column]=0
  for i in range(-(width/2),i<width/2+1):
    for j in range(-(width/2),width/2+1):
      total+=(width/2-max(abs(i),abs(j))+1)
  for column in range(width,y+width-1):
    for row in range(width,x+width):
      tmp=0;
      for i in range(-(width/2),width/2+1):
  for j in range(-(width/2),width/2+1):
	  tmp+=array[row+i][column+j]*(width/2-max(abs(i),abs(j))+1);
  if(16*tmp>total*threshold):
     array2[row][column]=1
  else:
    array2[row][column]=0
  for column in range(y):
    for row in range(x):
      array[row][column]=array2[row][column]
  for i in range(ARRAY_SIZE):
    array2[i]=""




