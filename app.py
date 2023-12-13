import streamlit as st

st.write("""
# Largest Number

Outputs the largest of the given three numbers.
""")

st.header('User Input Parameters')

n1 = st.number_input("Input Number 1")
n2 = st.number_input("Input Number 2")
n3 = st.number_input("Input Number 3")
gv = 0
if n1 > n2:
  if n1 > n3:
    gv = n1
  else:
    gv = n3
else:
  if n2 > n3:
    gv = n2
  else:
    gv = n2
if st.button("Find Largest"):
  st.write('Largest Number : {0}'.format(gv))
