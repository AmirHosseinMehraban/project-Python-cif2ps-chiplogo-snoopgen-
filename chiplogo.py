from array import array
from ast import arg
from fileinput import close
import sys

from zmq import NULL

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
ARRAY_SIZE=1024
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
image_out=[]
ARRAY_XSIZE=1
ARRAY_YSIZE=1

DEBUG=0
view_array=1000
array=[]
array2=[]
cif=0
magic=0
input=0
output=0
x_corner
y_corner

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
  tmp_c=""
  width=1
  space=1
  scale=1
  tech=0
  x=0
  y=0
  base=1
  junk=0
  max_col=35
  max_row
  x_corner
  y_corner
  threshold_after=4
  threshold_before=4
  scale=scale_factor
  width=min_width
  space=min_space
  threshold_before=thresh_before
  threshold_after=thresh_after
  fpin=open(input_file,"r")
  if fpin == NULL: 
    print("cannot open input file\n")
    return
  
  if tmp==NULL:
    print("there is not enough memory\n")
    close(fpin)
    return
  
  i=0
  fpin.read(tmp)
  #check here
  if tmp=="P1":
    print("This doesn't seem like a pbm file, because it doesn't have the P1 header")
  fpin.read(tmp)
  while not tmp=="#":
    fpin.read("%*[^\n]")
    #getc(fpin) check later
    fpin.read(tmp)

  
  ARRAY_XSIZE = x = int(tmp)
  fpin.read(tmp)
  ARRAY_YSIZE = y = int(tmp)
  if(ARRAY_YSIZE == 0 or  ARRAY_XSIZE ==0):
    close(fpin)
    tmp=""
    print("array has a size of zero\n")
    return
  for i in range(ARRAY_SIZE):
  
    image_out.append(int(ARRAY_YSIZE+2*width+2))
    if image_out[i]==NULL:
      print("there is not enough memory\n")
      exit(0)
    array[i]=int(ARRAY_YSIZE+2*width+2)
    if array[i]==NULL:
      print("there is not enough memory\n")
      exit(0)
    array2.append(int(ARRAY_YSIZE+2*width+2))
    if array2[i]==NULL:
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
    print("before enlarge\n")
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
    fpout=open(output_file,"w")
    if fpout== NULL: 
        print("cannot open output file\n")
        return
      #check last
    row=0
    fpout.write("magic\ntech  %s\ntimestamp 777777777\n", magic_tech)
    fpout.write("<< %s >>\n", magic_layer)
    for row in range(x):
      if array[row][column] ==1:
        base=scale
        y_corner=y-column
        y_corner[0]=base
        x_corner=row*base
        fpout.write("rect %d %d %d %d\n",x_corner,y_corner,x_corner+base,y_corner+base)
      fpout.write("<< end >>\n")
    else:
      fpout=open(output_file,"w")
      if fpout== NULL:
        print("cannot open output file\n")
        return
      fpout.write("DS 1 %d 2;\n9 logo;\nL %s;\n", cif_lambda, cif_layer)


      column=0
      for column in range(y):
        row=0
        for row in range(x):
          if array[row][column] ==1:
            base=10*scale*width
            y_corner=y-column
            y_corner*=base
            x_corner=base*row-width
            fpout.write("B %d %d %d %d;\n",base+2*width,base,x_corner+(base/2),y_corner+(base/2))
      
      fpout.write("DF;\nC 1;\nEnd\n")
  if DEBUG==1:
    print("before free\n")
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
 
def shrink_array(array,x,y,width):
  for i in range(x+width-1):
    for j in range(y+width-1):
      if(i>width-1 or j>width-1 ):
        array[i][j]=array[i+width][j+width]
def smooth_array(array,x,y,threshold,width):
  array2=[]
  total=0
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
      tmp=0
      for i in range(-(width/2),width/2+1):
        for j in range(-(width/2),width/2+1):
          tmp+=array[row+i][column+j]*(width/2-max(abs(i),abs(j))+1)
      if 16*tmp>total*threshold:
         array2[row][column]=1
      else:
        array2[row][column]=0
        
  for column in range(y):
    for row in range(x):
      array[row][column]=array2[row][column]
  for i in range(ARRAY_SIZE):
    array2[i]=""


def max(i,j):
  if i<=j:
    return j
  return i

def enlarge_array(array,x,y,width):
  for i in range(x+2*width-1,0,-1):
    for j in range(y+2*width-1,0,-1):
      if(i<width) or (j<width) or (i>(x-1+width)) or (j>(y-1+width)): 
        array[i][j]=0
      
      else:
        array[i][j]=array[i-width][j-width]

def find_error(array,error,x,y,width,space):

  for i in range(ARRAY_XSIZE+1):
    for j in range(ARRAY_YSIZE+1):
      error[i][j]=0

  '''
  first find the horizontal width errors 
  note that the input array has been enlarged before

  ''' 
  for j in range(width,y+width+1):
    for i in range(width,x+width+1):
      tmp=0
      tmp1=0
      for k in range(width,1,-1):
        if (array[i-k][j]+error[i-k][j])>0:
          tmp +=1
          tmp1=1
        if (array[i-k][j]+error[i-k][j])==0 and tmp==1:
          tmp=2

      
      if tmp1<width and tmp1>0 and tmp==1 and array[i][j]==0:
          error[i][j]=1


  '''
  /** now find the vertical width errors **/
  /** note that the input array has been enlarged before **/
  '''
  for i in range(width,x+width+1):
    for j in range(width,width+y+1):
      tmp=0
      tmp1=0
      for k in range(width,1,-1):
        if(array[i][j-k]+error[i][j-k])>0:
          tmp1+=1
          tmp=1
        if(array[i][j-k]+error[i][j-k])==0 and tmp==1:
          tmp=2
 
      if(tmp1<width and tmp1>0 and tmp==1 and array[i][j]==0):
        error[i][j]=1



def display_array(x,y):
  j=0
  print("Here is an approximate view of what you will get!!\n\n")
  if(view_array==1000):
    j=y/80+1
  else: 
    j=view_array
  for row in range(0,y,j):
    for column in range(0,x,j):
      if(array[column][row] == 1):
        print("*")
      else: 
        print(" ")
    print("\n")



'''


  here is the main function


'''
cif=0
magic=0
input=0
output=0
x_corner=0
y_corner=0
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
argc=len(sys.argv)
current_argv=0

while ((argc==1) and current_argv>0 and (sys.argv == '-')):#maybe change after
  argc-=1
  s=sys.argv[current_argv+1]
  if s=='m':
    magic=1
    current_argv+=1
    magic_layer+=sys.argv[current_argv]
    argc-=1
  elif s=='c':
    cif=1
    current_argv+=1
    output_file +="logo.cif"
    cif_layer +=sys.argv[current_argv]
    argc-=1
  elif s=='t':
    argc-=1
    current_argv+=1
    magic_tech+=sys.argv[current_argv]
  elif s=='v':
    view_array=int(sys.argv[current_argv+1])
    argc-=1
  elif s=='A':
    thresh_after=int(sys.argv[current_argv+1])
    smooth_after=1
    argc-=1
  elif s=='B':
    thresh_before=int(sys.argv[current_argv+1])
    smooth_before=1
    argc-=1
  elif s=='h':
    error_mess()
  elif s=='e':
    error_correct=1
  elif s=='w':
    min_width=int(sys.argv[current_argv+1])
    argc-=1
  elif s=='s':
    scale_factor=float(sys.argv[current_argv+1])
    argc-=1
  else:
    break
if (argc):
  input=1
  argv+=1
  input_file+=sys.argv[current_argv]
  current_argv+=1
  argc-=1
  fpin=open(input_file,"r")
  if fpin == NULL:
      print("cannot open input file \n")
      exit(1)
  fpin.close()
if argc:
  output_file=sys.argv[current_argv]
  current_argv+=1
  argc-=1
  fpout=open(output_file,"w")
  if fpout == NULL:
    print("cannot open output file \n")
    exit(1)
  fpout.close()
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







