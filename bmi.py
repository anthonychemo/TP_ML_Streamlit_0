import streamlit as st
st.title("Welcome to the BMI Calculator")

weight=st.number_input('Enter your weight in kgs')
height=st.radio('Select your height format:',('cms','meters','feet'))

try:

 if height == 'cms':
    height=st.number_input('cms')
    bmi=weight/((height/100)**2)
 elif status =='meters':
    height=st.number_input('meters')
    bmi=weight/((height)**2)

 else:
    height=st.number_input('feet')
    bmi=weight/((height/3.28)**2)
except:
    print("Zero Division Error")

if(st.button('Calculate BMI')):
   st.write('Your BMI index is {}'.format(round(bmi)))

   if bmi<16:
      st.error('You are extremely underweight')
   elif(bmi >=16 and bmi<18.5):
      st.warning('You are Underweight')
   elif(bmi >=18.5 and bmi<25):
      st.warning('You are Healthy')
   elif(bmi >=25 and bmi<30):
      st.warning('You are Overweight')
   elif(bmi>30):
      st.warning('You are Extremely Overweight')
   st.balloons()
