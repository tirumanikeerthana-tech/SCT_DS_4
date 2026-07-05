import pandas as pd
import matplotlib.pyplot as plt

# Sample Accident Dataset
data = {
    'Weather': ['Clear', 'Rain', 'Fog', 'Clear', 'Rain', 'Fog', 'Clear'],
    'Road_Condition': ['Dry', 'Wet', 'Wet', 'Dry', 'Wet', 'Wet', 'Dry'],
    'Time': ['Morning', 'Night', 'Evening', 'Afternoon', 'Night', 'Morning', 'Evening'],
    'Accidents': [20, 35, 15, 25, 40, 10, 30]
}

df = pd.DataFrame(data)

# Display Dataset
print(df)

# Weather Analysis
df.groupby('Weather')['Accidents'].sum().plot(kind='bar')
plt.title('Accidents by Weather')
plt.xlabel('Weather')
plt.ylabel('Number of Accidents')
plt.show()

# Road Condition Analysis
df.groupby('Road_Condition')['Accidents'].sum().plot(kind='bar')
plt.title('Accidents by Road Condition')
plt.xlabel('Road Condition')
plt.ylabel('Number of Accidents')
plt.show()

# Time Analysis
df.groupby('Time')['Accidents'].sum().plot(kind='bar')
plt.title('Accidents by Time of Day')
plt.xlabel('Time')
plt.ylabel('Number of Accidents')
plt.show()
