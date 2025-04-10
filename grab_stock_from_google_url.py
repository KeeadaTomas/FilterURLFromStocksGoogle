import re
import urllib.parse

url = "https://www.google.com/finance/quote/AXFO:STO?comparison=STO%3AAZA%2CSTO%3ASAVE%2CSTO%3AXACT-SVERIGE%2CSTO%3ASAAB-B&window=5D"

# Decode the URL to handle the encoded characters
decoded_url = urllib.parse.unquote(url)

# Capture the main ticker (before the colon)
main_ticker = re.search(r"quote/([^:]+)", decoded_url)

# Capture the tickers in the 'comparison' parameter (split by commas)
comparison_param = re.search(r"comparison=([^&]+)", decoded_url)

# Extract the tickers from the comparison parameter
if comparison_param:
    comparison_tickers = comparison_param.group(1).split(",")

    # Extract the actual stock tickers (after the colon)
    all_comparison_tickers = [ticker.split(":")[1] for ticker in comparison_tickers]
else:
    all_comparison_tickers = []

# If the main ticker exists, add it to the list of comparison tickers
if main_ticker:
    all_comparison_tickers.insert(0, main_ticker.group(1))

# Print all the tickers found
print("All Stock Tickers:", all_comparison_tickers)

#the reason is that i want to grab all the items to remove the first onee
