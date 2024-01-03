import streamlit as st

# Function to simulate bank account follow-up
def bank_account_follow_up(account_balance, transactions):
    updated_balance = account_balance + sum(transactions)
    return updated_balance

# Streamlit app
def main():
    st.title("Bank Account Follow-Up App")

    # Sidebar for user input
    st.sidebar.header("User Input")
    account_balance = st.sidebar.number_input("Enter initial account balance:", min_value=0.0, step=1.0, value=1000.0)
    transactions = st.sidebar.text_area("Enter transactions (comma-separated):", "100, -50, 200", key="transactions")

    # Convert transactions to a list of floats
    transactions = [float(x.strip()) for x in transactions.split(',')]

    # Bank account follow-up
    updated_balance = bank_account_follow_up(account_balance, transactions)

    # Display results
    st.write(f"Initial Account Balance: ${account_balance:.2f}")
    st.write(f"Transactions: {transactions}")
    st.write(f"Updated Account Balance: ${updated_balance:.2f}")

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)

        # To convert to a string based IO:
        #stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        #st.write(stringio)

        # To read file as string:
        #string_data = stringio.read()
        #st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)


if __name__ == "__main__":
    main()
