from die import Die
from plotly import offline
from plotly.graph_objs import Bar, Layout

die1=Die(6)
die2=Die(10)
#roll the die
results=[]
for roll_num in range(50000):
	result=die1.roll()+die2.roll()
	results.append(result)
#print(results)

#Analyzing the result
frequencies=[]
max_result= die1.sides+die2.sides
for value in range(2, max_result+1):
	frequency=results.count(value)
	frequencies.append(frequency)
print(frequencies)

#visualize the result
x_values=list(range(2,max_result+1))
data=[Bar(x=x_values,y=frequencies)]
x_config = {'title':'Result', 'dtick':1}
y_config = {'title':'No of times the result occurs'}
my_layout= Layout(title='Result of rolling two D6 dice 1000 times', xaxis=x_config, yaxis=y_config)
offline.plot({'data':data, 'layout':my_layout}, filename='d6_d6.html')
