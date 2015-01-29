from turtle import *

def snowflake(lenghth,s):
	if s ==0:
		forward(lenghth)
	else:
		snowflake(lenghth/2,s-1)
		left(60)
		snowflake(lenghth/2,s-1)
		right(120)
		snowflake(lenghth/2,s-1)
		left(60)
		snowflake(lenghth/2,s-1)
		right(120)	
			
			
snowflake(100,4)
