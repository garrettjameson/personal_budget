# Main Script for calling functions in budget analyzer

# import modules necessary for main
import actions as act

# run and return
budget_data, networth, accounts, transactions = act.scrape()

# pass returned values to plotter function
act.save_data_frame("budget_data", budget_data)
act.save_data_frame("accounts", accounts)
act.save_data_frame("transactions", transactions)


if __name__ == '__main__':
    act.scrape()