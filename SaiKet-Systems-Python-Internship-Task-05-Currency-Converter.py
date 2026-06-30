"""
SaiKet Systems - Python Development Internship
Task 5: Currency Converter

Description:
Converts an amount between currencies using real-time exchange rates
fetched from a free public API (Frankfurter.app, which sources rates
from the European Central Bank and requires no API key). Includes
input validation and error handling.

Skills demonstrated: API Integration, User Input Handling,
Mathematical Operations

NOTE: Run `pip install requests` before executing this script if it is
not already installed. An active internet connection is required.
"""

import requests

API_URL = "https://api.frankfurter.app/latest"


def get_exchange_rate(base_currency, target_currency):
    params = {"from": base_currency.upper(), "to": target_currency.upper()}
    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        rates = data.get("rates", {})
        rate = rates.get(target_currency.upper())
        if rate is None:
            print("Error: Could not retrieve a rate for that currency pair.")
            print("Please check that you entered valid currency codes (e.g., USD, EUR, INR).")
            return None
        return rate
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the exchange rate service. Check your internet connection.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.HTTPError as e:
        print(f"Error: HTTP error occurred - {e}")
    except (ValueError, KeyError):
        print("Error: Received an unexpected response from the API.")
    return None


def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    if rate is None:
        return None
    return amount * rate, rate


def get_valid_amount():
    while True:
        amount_input = input("Enter the amount to convert: ").strip()
        try:
            amount = float(amount_input)
            if amount < 0:
                print("Amount cannot be negative. Please try again.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a numeric amount.")


def main():
    print("===== CURRENCY CONVERTER =====")
    print("Example currency codes: USD, EUR, GBP, INR, JPY, AUD, CAD\n")

    while True:
        base_currency = input("Enter the base currency code (e.g., USD): ").strip().upper()
        target_currency = input("Enter the target currency code (e.g., INR): ").strip().upper()

        if len(base_currency) != 3 or len(target_currency) != 3:
            print("Currency codes should be 3-letter ISO codes (e.g., USD, EUR). Try again.\n")
            continue

        amount = get_valid_amount()
        result = convert_currency(amount, base_currency, target_currency)

        if result is not None:
            converted_amount, rate = result
            print(f"\n{amount:.2f} {base_currency} = {converted_amount:.2f} {target_currency}")
            print(f"(Exchange rate: 1 {base_currency} = {rate:.4f} {target_currency})\n")

        again = input("Convert another amount? (y/n): ").strip().lower()
        if again != "y":
            print("Thank you for using the Currency Converter. Goodbye!")
            break


if __name__ == "__main__":
    main()
