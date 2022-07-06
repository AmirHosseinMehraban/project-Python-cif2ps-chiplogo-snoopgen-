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


