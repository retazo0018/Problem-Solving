// A simple Arithmetic Calculator which can process text or numeric inputs from the user.
// Eg 1. Input: 2+2 Output: 4
// Eg.2  Input 2 plus 2: 4
#include<stdio.h>
#include<ctype.h>
#include<string.h>
#include<stdlib.h>
int calculator()
{
    int i=0,x,num[100];
	int result_a=0,result_s=0,result_m=1,result_d;
	char inputstring[100],ch;
	FILE *fp;
	gets(inputstring);
	fp = fopen("file.txt","w");
	fputs(inputstring,fp);
	fclose(fp);
	fp = fopen("file.txt","r");
	while(ch!=EOF)
		{
			ch=fgetc(fp);
				if(isdigit(ch))
	 				{
						num[i]=(ch-48);
						while(isdigit(ch=fgetc(fp)))
							{		
								num[i]=((num[i]*10)+(ch%48));
							}
		
						i++;
	  				}
		}
	fclose(fp);
	if(strupr(inputstring))
	{
		strlwr(inputstring);
	}
	if((strstr(inputstring,"dont")!=NULL)||(strstr(inputstring,"do not")))exit(0);
	if((strstr(inputstring,"add")!=NULL)||(strstr(inputstring,"+")!=NULL)||(strstr(inputstring,"plus")!=NULL))
		{
		for(x=0;x<i;x++)
		{
			result_a+=num[x];
		}
		printf("%d",result_a);
		}
		if((strstr(inputstring,"sub")!=NULL)||(strstr(inputstring,"-")!=NULL)||(strstr(inputstring,"minus")!=NULL))
		{
		for(x=0;x<i;x++)
		{
			result_s=num[x]-result_s;
		}
		printf("%d",(0-result_s));
		}
		
		if((strstr(inputstring,"mul")!=NULL)||(strstr(inputstring,"*")!=NULL)||(strstr(inputstring,"product")!=NULL))
		{
		for(x=0;x<i;x++)
		{
			result_m*=num[x];
		}
		printf("%d",result_m);
		}
		
	if((strstr(inputstring,"div")!=NULL)||(strstr(inputstring,"/")!=NULL)||(strstr(inputstring,"divide")!=NULL))
		{
		result_d=num[0]/num[1];
		printf("%d",result_d);
		}
}
int main()
{
	calculator();
}
