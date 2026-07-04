import requests

BASE_URL = "https://world.openfoodfacts.net/api/v3.6/product/3274080005003.json"

def fetch_product(barcode):
    url = f"{BASE_URL}/{barcode}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        if "product" not in data:
            return None

        product = data["product"]

        return {
            "barcode": barcode,
            "product_name": product.get("product_name", "Unknown"),
            "brand": product.get("brands", "Unknown"),
            "ingredients": product.get("ingredients_text", "Not Available")
        }

    except requests.exceptions.RequestException:
        return None