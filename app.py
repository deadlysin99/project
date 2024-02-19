import streamlit as st
st.title('apps')
username = st.text_input('Username')
password = st.text_input('Password',type='password')
if st.button('login'):
    if username=='megha' and password=='megha@192499':
        st.write('login granted')
        st.warning('login granted')
else:
    st.write('acess denied')
    st.warning('acess denied')


