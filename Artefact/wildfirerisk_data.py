import pandas as pd
import serial

df = pd.read_csv("wildfirerisk_data.csv")
print(df)

# disaster risk modelling
def get_alert(score):
    if score > 30:
        return "High Wildfire Risk"
    return "No Wildfire Risk- Safe"

def check_wildfire_risk(x, z):
    risk = x * z
    if risk > 2000:
        return "High Wildfire Risk"
    return "No Wildfire Risk- Safe"


df['wildfire_risk'] = df['Temp'] * 6 + df['Moisture']
print(df)
print()

# What if 1: Drought (reduce moisture by 20)
df_drought = df.copy()
df_drought['Moisture'] -= 20
df_drought['wildfire_risk'] = df_drought['Temp'] * 6 + df_drought['Moisture']
df_drought['Alert'] = df_drought['wildfire_risk'].apply(get_alert)

print("What If Scenario 1: Drought")
print(df_drought[['Temp', 'Moisture', 'wildfire_risk', 'Alert']])
print()

# What if 2: Reduce sunlight
df_reduction = df.copy()
df_reduction['Light'] -= 5
df_reduction['wildfire_risk'] = df_reduction['Temp'] * 6 + df_reduction['Moisture']
df_reduction['Alert'] = df_reduction['wildfire_risk'].apply(get_alert)

print("What If Scenario 2: Reduction")
print(df_reduction[['Temp', 'Moisture', 'wildfire_risk', 'Alert']])
print()

#adaptive system 

threshold = 30
alert_flag = False

for risk in df['wildfire_risk']:
    if risk > threshold and not alert_flag:
        print("ALERT! HIGH WILDFIRE RISK!")
        alert_flag = True
        
    if risk <= threshold and alert_flag:
        print("CANCEL ALERT")
        alert_flag = False