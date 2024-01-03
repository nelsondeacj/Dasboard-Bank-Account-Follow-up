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

if __name__ == "__main__":
    main()
