import streamlit as st
import pandas as pd
import base64
from datetime import datetime

def main():
    st.title('Upload CSV or Excel File')

    uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=['csv', 'xlsx'])

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            df = pd.read_excel(uploaded_file)

        df_head = df.head(5)
        st.write(df_head)

        csv = df_head.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        href = f'<a href="data:file/csv;base64,{b64}" download="data_{timestamp}.csv">Download csv file</a>'
        st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()