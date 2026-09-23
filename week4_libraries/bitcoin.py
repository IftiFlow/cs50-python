import requests
import sys

def main():
    
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit("Missing command-line argument")

    
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=YOUR_API_KEY")
        price = float(response.json()["data"]["priceUsd"])
        amount = n * price
    except requests.RequestException:
        sys.exit(1)

    print(f"${amount:,.4f}")

if __name__ == "__main__":
    main()