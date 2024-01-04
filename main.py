import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
import seaborn as sns

# Function to simulate bank account follow-up
def bank_account_follow_up(account_balance, transactions):
    updated_balance = account_balance + sum(transactions)
    return updated_balance

def create_pie_chart(labels, sizes):
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
    return fig

# Streamlit app
def main():
    st.title("Bank Account Follow-Up App")

    # Sidebar for user input
    st.sidebar.header("User Input")
    uploaded_file = st.sidebar.file_uploader("Choose a file")
    account_limit = st.sidebar.number_input("Enter account limit to follwo (Not implemented):", min_value=0.0, step=1.0, value=1000.0)
    #transactions = st.sidebar.text_area("Enter transactions (comma-separated):", "100, -50, 200", key="transactions")



    # Bank account follow-up
    #updated_balance = bank_account_follow_up(account_balance, transactions)

    # Display results
    #st.write(f"Initial Account Balance: ${account_balance:.2f}")
    #st.write(f"Transactions: {transactions}")
    #st.write(f"Updated Account Balance: ${updated_balance:.2f}")


    if uploaded_file is not None:
        # To read file as bytes:
        #bytes_data = uploaded_file.getvalue()
        #st.write(bytes_data)

        # To convert to a string based IO:
        #stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        #st.write(stringio)

        # To read file as string:
        #string_data = stringio.read()
        #st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        df = pd.read_csv(uploaded_file)

        ### Data pretreatment (make a .py file for that to replace the functions)

        # Eliminate payment (negative values)
        df_expenses=df[df['amount']>0]

        bilan=df_expenses.groupby(["category"]).sum("amount").reset_index()
        bilan

        pie_chart = create_pie_chart(bilan['category'], bilan['amount'])

        st.pyplot(pie_chart)

        st.write(bilan)
        st.write(df)

    else:
        st.write(f"Upload a Nubank csv file to start the App")


if __name__ == "__main__":
    main()
