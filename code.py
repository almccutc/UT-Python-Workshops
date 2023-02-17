import pandas as pd

df = pd.read_csv('WDB_DemonicPact4.csv') # create a dataframe of the data using pandas

thedemonicdataframe = df["Demonic_Type"].value_counts() # create variable for the counts of the different Demonic Types

thedemonicdataframe.plot.bar(x='Demonic Type', y='Count', color = "pink", rot=80, title= "Demonic Pact Frequency Chart") # create bar graph
thedemonicdataframe.plot.line(x='Demonic Type', y='Count', rot=80, title= "Demonic Pact Frequency Chart") # create line graph
thedemonicdataframe.plot.pie(x='Demonic Type', y='Count', rot=80, title= "Demonic Pact Frequency Chart") # create pie chart
thedemonicdataframe.plot.area(x='Demonic Type', y='Count', rot=80, title= "Demonic Pact Frequency Chart") # create area graph
