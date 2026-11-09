
import os
from pathlib import Path
from dotenv import load_dotenv


def load_shopify_settings():
    # Locate the .env file in the main project folder
    project_folder = Path(__file__).resolve().parent.parent
    environment_file = project_folder / ".env"

    # Load environment variables from .env
    load_dotenv(environment_file)

    # Read Shopify configuration
    shopify_store = os.getenv("shopify_store")
    shopify_api_version = os.getenv("shopify_api_version")
    shopify_client_id = os.getenv("shopify_client_id")
    shopify_client_secret = os.getenv("shopify_client_secret")

    # Make sure all required settings exist
    if not all([
        shopify_store,
        shopify_api_version,
        shopify_client_id,
        shopify_client_secret,
    ]):
        raise ValueError("Missing required Shopify settings.")

    return {
        "shopify_store": shopify_store,
        "shopify_api_version": shopify_api_version,
        "shopify_client_id": shopify_client_id,
        "shopify_client_secret": shopify_client_secret,
    }
