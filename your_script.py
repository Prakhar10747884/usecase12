import requests
import numpy as np

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Successfully fetched data!")
        return response.text
    else:
        print("Failed to fetch data.")
        return None

def main():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = fetch_data(url)
    
    if data:
        print("Here's a sample of the data:")
        print(data[:100])  # Print the first 100 characters of the data

    # Simple NumPy operation
    array = np.array([1, 2, 3, 4, 5])
    print("NumPy array:", array)
    print("Sum of array elements:", np.sum(array))

if __name__ == "__main__":
    main()
