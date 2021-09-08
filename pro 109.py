
import pandas as pd
import statistics

from pandas.core.algorithms import mode
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("StudentsPerformance.csv")
students_df=df["reading score"].tolist()


students_mean=statistics.mean(students_df)
students_median=statistics.median(students_df)
students_mode=statistics.mode(students_df)
students_stdev=statistics.stdev(students_df)

first_stdev_start,first_stdev_end=students_mean-students_stdev,students_mean+students_stdev
second_stdev_start,second_stdev_end=students_mean-(2*students_stdev),students_mean+(2*students_stdev)
third_stdev_start,third_stdev_end=students_mean-(3*students_stdev),students_mean+(3*students_stdev)


list_data_in_1stdev=[result for result in students_df if (result>first_stdev_start and result<first_stdev_end)]
list_data_in_2nddev=[result for result in students_df if (result>second_stdev_start and result<second_stdev_end)]
list_data_in_3rddev=[result for result in students_df if (result>third_stdev_start and result<third_stdev_end)]


print(f"Mean of the data is {students_mean} ")
print(f"Median of the data is {students_median} ")
print(f"Mode of the data is {students_mode} ")
print(f"Standard deviation of the data is {students_stdev} ")

print("{}% of data lies within 1 standard deviation".format(len(list_data_in_1stdev)*100.0/len(students_df))) 
print(f"{len(list_data_in_2nddev)*100.0/len(students_df)}% of data lies within 2 standard deviation")
print(f"{len(list_data_in_3rddev)*100.0/len(students_df)}% of data lies within 3 standard deviation")


fig=ff.create_distplot([students_df],["Reading Score"],show_hist=False)
fig.add_trace(go.Scatter(x=[students_mean,students_mean],y=[0,0.2],mode="lines",name="Mean"))

fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start], y=[0,0.17],mode="lines",name="1 standard deviation"))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end], y=[0,0.17],mode="lines",name="1 standard deviation"))

fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start], y=[0,0.17],mode="lines",name="2 standard deviation"))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end], y=[0,0.17],mode="lines",name="2 standard deviation"))

fig.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start], y=[0,0.17],mode="lines",name="3 standard deviation"))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end], y=[0,0.17],mode="lines",name="3 standard deviation"))

fig.show()








