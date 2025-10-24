# Python Currency Converter

A currency converter written in Python, this tool fetches up-to-date rates from the [FloatRates API](http://www.floatrates.com/json-feeds.html) and lets you quickly convert between currencies with input validation, error handling, and smart caching.

## Features

- **Live exchange rates** for your selected base currency from FloatRates.
- **Intelligent caching:** Common rates (USD, EUR) and all requested rates are cached for fast, repeated conversions.
- **Clear input validation:** Prompts you until you enter valid currency codes and amounts.
- **Graceful error handling:** Handles network issues, unsupported currencies, invalid user entries, and negative amounts.
- **Transparent conversion:** Shows the used exchange rate with each conversion.

## Usage

1. Run the script:
    ```
    python currency_converter.py
    ```

2. Enter your base currency code (e.g., `usd`, `eur`, `sgd`). Type `exit` to quit.

3. Enter the target currency code to convert to (or `exit` to quit).

4. Enter the amount of money to convert (must be a positive number).

5. View the result and exchange rate. Caching ensures that subsequent conversions for the same currency are fast.

## Example Session (do note that the rates in this example are subject to changes when you use this program)

Enter the currency you have (enter 'exit' to exit): usd

Enter the currency you want to exchange to (or 'exit' to leave): eur

Checking the cache...

Oh! It is in the cache!

Enter the amount of USD you have: 50

You received 47.12 EUR (rate: 0.9424).

Enter the currency you want to exchange to (or 'exit' to leave): gbp

Checking the cache...

Sorry, but it is not in the cache!

Enter the amount of USD you have: 50

You received 38.25 GBP (rate: 0.765).

## Dependencies

- Python 3.x
- [`requests`](https://docs.python-requests.org/en/latest/): Install with  
    ```
    pip install requests
    ```

## Code Structure

- `get_rates(base_currency)`: Fetches conversion rates from FloatRates and handles errors.
- `prompt_base_currency()`: Ensures only valid base currencies are used.
- `main()`: Runs the whole interactive loop for currency conversion.

## Notes

- Some currency codes may not be supported by FloatRates (see [currency codes](http://www.floatrates.com/daily/sgd.json) for examples).
- For faster and repeated conversions, rates are cached during runtime.
- If you have network issues or API downtime, the tool will prompt and retry smoothly.
