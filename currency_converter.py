import requests
import logging
import sys

def get_rates(base_currency):
    """
    Fetch exchange rates for the specified base currency from FloatRates API.
    Returns a dictionary mapping currency codes to rate data.
    Handles connection and HTTP errors robustly.
    """
    url = f"http://www.floatrates.com/daily/{base_currency}.json"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        logging.error("Connection error. Please check your internet connection.")
    except requests.exceptions.HTTPError:
        logging.error("HTTP error. The exchange rate source is unavailable or the currency code may be wrong.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    return {}

def prompt_base_currency():
    """
    Prompt user for a valid base currency.
    Repeats until a supported currency code returns a valid rates dictionary.
    """
    while True:
        base_currency = input("Enter the currency you have (enter 'exit' to exit): ").strip().lower()
        if base_currency == "exit":
            print("Thank you for using this Currency Converter program!")
            sys.exit()
        rates = get_rates(base_currency)
        if not rates:
            print(f"Sorry, '{base_currency.upper()}' is not a valid or supported base currency. Please try again.")
        else:
            return base_currency, rates  # Returns both for use in main()

def main():
    # Setup logging configuration for informative error messages
    logging.basicConfig(level=logging.INFO)

    # Prompt for and validate base currency, fetch initial rates
    base_currency, rates = prompt_base_currency()

    # Initialize cache with USD and EUR rates if available
    cache = {code: rates[code]["rate"] for code in ("usd", "eur") if code in rates}

    # Main loop for repeated conversions
    while True:
        # Prompt for target currency (currency to exchange to)
        target_currency = input("Enter the currency you want to exchange to (or 'exit' to leave): ").strip().lower()
        if target_currency == "exit":
            print("Thank you for using this Currency Converter program!")
            break

        print("Checking the cache...")
        if target_currency in cache:
            print("Oh! It is in the cache!")
            exchange_rate = cache[target_currency]  # Use cached rate
        elif target_currency in rates:
            print("Sorry, but it is not in the cache!")
            exchange_rate = rates[target_currency]["rate"]
            cache[target_currency] = exchange_rate  # Add to cache
        else:
            # Unsupported or misspelled currency code
            print(f"Sorry, '{target_currency.upper()}' is not available for exchange!")
            continue  # Prompt for new target currency

        # Prompt for the amount to exchange and validate input
        while True:
            try:
                have_amount = float(input(f"Enter the amount of {base_currency.upper()} you have: "))
                if have_amount <= 0:
                    print("Amount must be a positive number. Please try again.")
                    continue
                break  # Valid amount entered
            except ValueError:
                print("Invalid amount! Please enter a number.")

        # Perform conversion, rounding to two decimal places
        currency_received = round(have_amount * exchange_rate, 2)
        # Show result and exchange rate for transparency
        print(f"You received {currency_received} {target_currency.upper()} (rate: {exchange_rate}).")

if __name__ == "__main__":
    # Program entry point; allows code to be imported as a module elsewhere
    main()
