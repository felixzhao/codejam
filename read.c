#include <stdio.h>
#include <stdlib.h>

int read(char *file)
{
  FILE *input;
  input = fopen(file,"r");
  if(input == NULL)
    {
      printf ("Cannot open file\n");
      exit(1);
    }
  else
    {
      printf("Open file success\n");
    }
  while(!feof(input))
    {
      int temp = 0;
      fscanf(input,"%d",&temp);
      printf("%d\n",temp);
    }
  fclose(input);
  return 0;
}

int main(int argc, char* argv[])
{
  read(argv[1]);

  return 0;
}
