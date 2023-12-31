# Restaurant Information Fetcher

This Python script allows you to fetch a list of restaurants based on a postal code using the Just Eat API. It provides information about the restaurant's name, rating, and cuisines.

## Usage

1. Make sure you have Python 3 installed on your system.

2. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   
3. Run the script:

    ```bash
    python main.py
   
4. Enter the postal code when prompted.

5. The script will fetch and display the list of restaurants in the specified area.

# Example:
Here's an example of what the output might look like:

Enter Post Code: E1 6AN

1. Restaurant One - Rating: 4.5, Cuisines: Italian, Pizza
2. Restaurant Two - Rating: 3.7, Cuisines: Chinese, Sushi
3. Restaurant Three - Rating: 4.2, Cuisines: Indian, Vegetarian


# Error Handling:
The script includes error handling for HTTP errors and request errors. 
If an error occurs, it will provide an appropriate error message.