import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression

df1=pd.read_csv("Semester1.csv")
df2=pd.read_csv("Semester2.csv")
df3=pd.read_csv("Semester3.csv")

p1=(df1['Percentage'].sum()/6)
p2=(df2['Percentage'].sum()/8)
p3=(df3['Percentage'].sum()/9)

st.title("📊RESULT DASHBOARD")
semester=st.radio(
    "Choose Semester",
    ['Semester1','Semester2','Semester3','All'],
    index=None,
)
st.write("📌you selected:",semester)

def show_sem1():
    fig1 = px.bar(df1, x ='Subject' ,y='Percentage',color='Subject',title='Result for Semester 1',
                  labels={'Subject':'Subjects','Percentage':'Percentage'}
                  
    )
    fig1.update_xaxes(showticklabels=False)
    st.plotly_chart(fig1)
    st.write(f'Percentage For Semester 1 : {p1:.2f}')

def show_sem2():
    fig2 = px.bar(df2, x ='Subject' ,y='Percentage',color='Subject',title='Result for Semester 2',
                  labels={'Subject':'Subjects','Percentage':'Percentage'}
                  
    )
    fig2.update_xaxes(showticklabels=False)
    st.plotly_chart(fig2)
    st.write(f'Percentage For Semester 2: {p2:.2f}')

def show_sem3():
    fig3 = px.bar(df3, x ='Subject' ,y='Percentage',color='Subject',title='Result for Semester 3',
                  labels={'Subject':'Subjects','Percentage':'Percentage'}
                  
    )
    fig3.update_xaxes(showticklabels=False)
    st.plotly_chart(fig3)
    st.write(f'Percentage For Semester 3 : {p3:.2f}')
     
if semester== 'Semester1':
     show_sem1()
elif semester=='Semester2':
     show_sem2()
elif semester=='Semester3':
     show_sem3()
elif semester=='All':
     

 col1, col2 ,col3= st.columns([33.33,33.33,33.33])
 with col1: 
    show_sem1()
 with col2:
    show_sem2()
 with col3:
     show_sem3()


#PREDICTION 

Data={
    'Sem':[1,2,3],
    'Percentage':[p1,p2,p3]
}

df4 = pd.DataFrame(Data)
X = df4[['Sem']]
y = df4['Percentage']

model = LinearRegression()
model.fit(X,y)

predicted = model.predict([[4]])
st.write(f'Predicted Percentage For Semester 4 : {predicted[0]:.2f}')
