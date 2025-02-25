from assistant import generate_crypto_summary

def main():
    query = input("Enter the crypto project or token: ")
    summary = generate_crypto_summary(query)
    print("Summary:", summary)

if __name__ == "__main__":
    main()
