from typing import List

import requests

URL = "https://uk.api.just-eat.io/restaurants/bypostcode/"


class Restaurant:
    def __init__(self, name: str, rating: float, cuisines: List[str]):
        """
        Represents a restaurant.

        Args:
            name (str): The name of the restaurant.
            rating (float): The rating of the restaurant.
            cuisines (List[str]): A list of cuisines offered by the restaurant.
        """
        self.name = name
        self.rating = rating
        self.cuisines = cuisines


def get_restaurants(post_code: str) -> List[Restaurant]:
    """
    Fetches a list of restaurants based on the provided postal code.

    Args:
        post_code (str): The postal code to search for restaurants.

    Returns:
        List[Restaurant]: A list of Restaurant instances.
    """
    try:
        response = requests.get(URL + post_code)
        response.raise_for_status()

        list_of_restaurants = []

        data = response.json()
        restaurants = data.get("Restaurants", [])

        for restaurant in restaurants:
            list_of_restaurants.append(
                Restaurant(
                    restaurant["Name"],
                    restaurant["Rating"]["RatingStars"],
                    [cusine["Name"] for cusine in restaurant["Cuisines"]],
                )
            )

        return list_of_restaurants

    except requests.exceptions.HTTPError as http_err:
        raise Exception(f"HTTP error occurred: {http_err}")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Request error: {str(e)}")


if __name__ == "__main__":
    code = input("Enter Post Code: ")
    get_restaurants(code)
