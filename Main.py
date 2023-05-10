import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

class PoliceKillings:

    def __init__(self, csv_file_path):
        self.df = pd.read_csv(csv_file_path, encoding='ISO-8859-1')

    def armed_ununarmed(self):
        armed_status = self.df["armed"].value_counts().sort_index()
        plt.bar(armed_status.index, armed_status)
        plt.xticks(armed_status.index,armed_status.index, rotation=90)
        plt.title('Whether the person who got killed was armed or not')
        plt.xlabel('How was the person armed')
        plt.ylabel('No of people killed')
        st.pyplot()
        st.set_option('deprecation.showPyplotGlobalUse', False)

    def cause_of_death(self):
        cause = self.df["cause"].value_counts().sort_index()
        my_explode = [0, 0.1, 0, 0, 0 ]
        # my_colors=['red', 'blue', 'green', 'black', 'red']
        plt.pie(cause, labels=cause.index, wedgeprops={'edgecolor':'black'}, autopct='%.1f%%')
        plt.title('Total Police Killings by Cause of Death')
        st.pyplot()
        st.set_option('deprecation.showPyplotGlobalUse', False)

    def race_ethnicity(self):
        kills_acc_to_race = self.df["raceethnicity"].value_counts().sort_index()
        my_explode = [0, 0.1, 0, 0, 0, 0]

        plt.pie(kills_acc_to_race, labels=kills_acc_to_race.index, wedgeprops={'edgecolor':'black'}, explode=my_explode, autopct='%.1f%%')
        plt.title('Total Police Killings by Race/Ethnicity')
        st.pyplot()
        st.set_option('deprecation.showPyplotGlobalUse', False)

    def killings_by_month(self):
        kill_in_each_month = self.df["month"].value_counts().sort_index()

        plt.bar(kill_in_each_month.index, kill_in_each_month.values)
        plt.title('Total Police Killings by Month')
        plt.xlabel('Month')
        plt.ylabel('Number of Killings')
        st.pyplot()
        st.set_option('deprecation.showPyplotGlobalUse', False)

    def killings_by_state(self):
        no_of_killings = self.df["state"].value_counts().sort_index()
        # x_label= no_of_killings.index,fontsize= 10
        plt.bar(no_of_killings.index, no_of_killings,width=1.5,align='center',edgecolor= 'black')
        plt.xticks(no_of_killings.index, no_of_killings.index, rotation=90,fontsize = 5)
        plt.title('Total Police Killings by State')
        plt.xlabel('State')
        plt.ylabel('Number of Killings')
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

if __name__ == '__main__':


    data = PoliceKillings('/Users/ishanknain/Desktop/Major Project/police_killings.csv')
    st.title('Where Police Have Killed Americans In 2015')
    st.sidebar.title('Select Visualisation from drop down menu')
    Visualisation_options = ['Armed/Unarmed', 'Cause of Death', 'Race/Ethnicity', 'Killings by Month', 'Killings by State']
    selected_visualisation = st.sidebar.selectbox('Select Visualisation', Visualisation_options)
    if selected_visualisation == 'Armed/Unarmed':
        data.armed_ununarmed()
    elif selected_visualisation == 'Cause of Death':
        data.cause_of_death()
    elif selected_visualisation == 'Race/Ethnicity':
        data.race_ethnicity()
    elif selected_visualisation == 'Killings by Month':
        data.killings_by_month()
    elif selected_visualisation == 'Killings by State':
        data.killings_by_state()
