import streamlit as st


# Method 1

if "input_1" not in st.session_state:
    st.session_state.input_1 = ""

with st.container():
    col11, col12 = st.columns([1,1])

    with col11:
        st.session_state.input_1 = st.text_area("Text 1",value=st.session_state.input_1)

    with col12:
        st.markdown("**Display Text 1**")
        st.write(st.session_state.input_1)


# Method 2

if "input_2" not in st.session_state:
    st.session_state.input_2 = ""

def callback():
    st.session_state.input_2 = input_2_temp

with st.container():
    col21, col22 = st.columns([1,1])

    with col21:
       input_2_temp = st.text_area("Text 2",value=st.session_state.input_2,on_change=callback)

    with col22:
        st.markdown("**Display Text 2**")
        st.write(input_2_temp)


# Method 3
        
if "input_3" not in st.session_state:
    st.session_state.input_3 = ""

with st.container():
    col31, col32 = st.columns([1,1])

    with col31:
       input_3_temp = st.text_area("Text 3",value=st.session_state.input_3)
       if not input_3_temp == st.session_state.input_3:
           st.session_state.input_3 = input_3_temp
           st.rerun()

    with col32:
        st.markdown("**Display Text 3**")
        st.write(input_3_temp)