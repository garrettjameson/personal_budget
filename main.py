# Main Script for calling functions in budget analyzer

# import modules necessary for main
import actions as act

# run and return
budget_data, networth = act.scrape()

# TODO: Append to a local dataframe so I can keep track month after month?

# pass returned values to plotter function
# budget_visuals = act.plot(budget_data, networth) TODO: build plotter function to plot budget data

if __name__ == '__main__':
    act.scrape()