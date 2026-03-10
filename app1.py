import streamlit as st
import joblib


model=joblib.load("pipe.joblib")
df=joblib.load("df.joblib")

st.title("laptop price predictor")
company_name=st.selectbox("Brand",df["Company"].unique())
Type=st.selectbox("Type",df["TypeName"].unique())

ram=int(st.selectbox("RAM",[2,4,6,8,12,16,32,64]))
weight=st.number_input("enter weight in kg: ")
Touch_Screen=st.selectbox("Touch Screen",[0,1])

Ips=st.selectbox("IPS",[0,1])
ppi=st.number_input("enter screen size:(in c.m) ")
cpu_brand=st.selectbox('CPU',df["Cpu brand"].unique())

HDD=st.selectbox("HDD in gb",[0,128,256,512,1024,2024])
SSD=st.selectbox("SSD in gb",[0,8,128,256,512])
gpu_brand=st.selectbox("GPU",df['Gpu brand'].unique())
os=st.selectbox("OS",df["os"].unique())

if st.button("Predict Price"):
    pred=model.predict([[company_name,Type,ram,weight,Touch_Screen,Ips,ppi,cpu_brand,HDD,SSD,gpu_brand,os]])
    st.title(f"Laptop price will be :  {pred}")
    