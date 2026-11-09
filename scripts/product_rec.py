
from shopify_settings import load_shopify_settings
from shopify_api import get_shopify_access_token, get_active_products
from product_export import prepare_product_for_csv, save_products_to_csv
from pathlib import Path


def main():
    # Load Shopify configuration
    shopify_settings = load_shopify_settings()

    # Authenticate with Shopify
    shopify_access_token = get_shopify_access_token(shopify_settings)

    print("Shopify authentication successful.")

    # Retrieve all active products from Shopify
    active_products = get_active_products(
        shopify_settings,
        shopify_access_token
    )
    # Prepare every product for the CSV file
    prepared_products = []

    for shopify_product in active_products:
        prepared_product = prepare_product_for_csv(shopify_product)
        prepared_products.append(prepared_product)

    # Save the CSV in the main project folder
    project_folder = Path(__file__).resolve().parent.parent
    csv_file_location = project_folder / "active_products.csv"

    saved_file_location = save_products_to_csv(
        prepared_products,
        csv_file_location,
    )

    print(f"CSV saved successfully: {saved_file_location}")
    print(f"Products exported: {len(prepared_products)}")
    print(f"Products retrieved: {len(active_products)}")


# Start the program when this file is run directly
if __name__ == "__main__":
    main()
