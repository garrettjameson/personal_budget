# Main Script for calling functions in budget analyzer

# import modules necessary for main
import actions as act

# run and return
budget_data, networth, accounts, transactions = act.scrape()


# TODO: Append to a local dataframe so I can keep track month after month?


# pass returned values to plotter function
act.save_data_frame("budget_data", budget_data)
act.save_data_frame("accounts", accounts)
act.save_data_frame("transactions", transactions)


if __name__ == '__main__':
    act.scrape()