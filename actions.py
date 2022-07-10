# functions for the budget analyzer to download, process, and display data
import mintapi as mint
import mintapi as mint
import pandas as pd
import constants as const

def scrape():
    mint.Mint(
        email = const.username,
        password = const.password,
        # Optional parameters
        mfa_method='sms',  # See MFA Methods section
        # Can be 'sms' (default), 'email', or 'soft-token'.
        # if mintapi detects an MFA request, it will trigger the requested method
        # and prompt on the command line.
        mfa_input_callback=None,  # see MFA Methods section
        # can be used with any mfa_method
        # A callback accepting a single argument (the prompt)
        # which returns the user-inputted 2FA code. By default
        # the default Python `input` function is used.
        mfa_token=None,  # see MFA Methods section
        # used with mfa_method='soft-token'
        # the token that is used to generate the totp
        intuit_account=None,  # account name when multiple accounts are registered with this email.
        headless=False,  # Whether the chromedriver should work without opening a
        # visible window (useful for server-side deployments)
        # None will use the default account.
        session_path=None,  # Directory that the Chrome persistent session will be written/read from.
        # To avoid the 2FA code being asked for multiple times, you can either set
        # this parameter or log in by hand in Chrome under the same user this runs
        # as.
        imap_account=None,  # account name used to log in to your IMAP server
        imap_password=None,  # account password used to log in to your IMAP server
        imap_server=None,  # IMAP server host name
        imap_folder='INBOX',  # IMAP folder that receives MFA email
        wait_for_sync=False,  # do not wait for accounts to sync
        wait_for_sync_timeout=300,  # number of seconds to wait for sync
        fail_if_stale=True,  # True will raise an exception if Mint is unable to refresh your data.
        use_chromedriver_on_path=False,  # True will use a system provided chromedriver binary that
        # is on the PATH (instead of downloading the latest version)
        driver=None  # pre-configured driver. If None, Mint will initialize the WebDriver.
    )

   budget_data = mint.get_budgets(const.username, const.password)
    mint.Mint.close()
    return
