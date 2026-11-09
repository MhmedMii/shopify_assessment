
import requests


def get_shopify_access_token(shopify_settings):
    # Read the settings needed for authentication
    shopify_store = shopify_settings["shopify_store"]
    shopify_client_id = shopify_settings["shopify_client_id"]
    shopify_client_secret = shopify_settings["shopify_client_secret"]

    # Build the Shopify authentication URL
    shopify_authentication_url = (
        f"https://{shopify_store}/admin/oauth/access_token"
    )

    # Request an access token from Shopify
    authentication_response = requests.post(
        shopify_authentication_url,
        data={
            "grant_type": "client_credentials",
            "client_id": shopify_client_id,
            "client_secret": shopify_client_secret,
        },
        timeout=30,
    )

    # Stop if Shopify returns an HTTP error
    authentication_response.raise_for_status()

    # Return the token to the main program
    return authentication_response.json()["access_token"]


def get_active_products(shopify_settings, shopify_access_token):
    # Read the store information needed for GraphQL
    shopify_store = shopify_settings["shopify_store"]
    shopify_api_version = shopify_settings["shopify_api_version"]

    # Define which product fields Shopify should return
    active_products_query = """
    query GetProducts($cursor: String) {
        products(first: 50, after: $cursor, query: "status:active") {
            nodes {
                id
                title
                tags

                collections(first: 50) {
                    nodes {
                        title
                    }
                    pageInfo {
                        hasNextPage
                    }
                }

                variants(first: 50) {
                    nodes {
                        price
                        compareAtPrice
                    }
                    pageInfo {
                        hasNextPage
                    }
                }
            }

            pageInfo {
                hasNextPage
                endCursor
            }
        }
    }
    """

    # Build the Shopify GraphQL API URL
    shopify_graphql_url = (
        f"https://{shopify_store}/admin/api/{shopify_api_version}/graphql.json"
    )

    # Start without a bookmark and prepare an empty product list
    where_to_continue = None
    all_active_products = []

    # Keep requesting pages until Shopify has no more products
    while True:
        shopify_graphql_response = requests.post(
            shopify_graphql_url,
            headers={
                "Content-Type": "application/json",
                "X-Shopify-Access-Token": shopify_access_token,
            },
            json={
                "query": active_products_query,
                "variables": {"cursor": where_to_continue},
            },
            timeout=30,
        )

        # Stop if the HTTP request failed
        shopify_graphql_response.raise_for_status()

        # Convert the JSON response into Python data
        shopify_response_data = shopify_graphql_response.json()

        # Shopify can report GraphQL errors even with HTTP 200
        if shopify_response_data.get("errors"):
            raise RuntimeError(shopify_response_data["errors"])

        # Separate products from pagination information
        product_information = shopify_response_data["data"]["products"]

        products_on_this_page = product_information["nodes"]

        # Prevent incomplete exports if product details have more pages
        for shopify_product in products_on_this_page:
            more_collections_available = (
                shopify_product["collections"]["pageInfo"]["hasNextPage"]
            )

            more_variants_available = (
                shopify_product["variants"]["pageInfo"]["hasNextPage"]
            )

            if more_collections_available or more_variants_available:
                raise RuntimeError(
                    "A product has additional variants or collections. "
                    "Nested pagination is required before exporting."
                )

        page_information = product_information["pageInfo"]

        # Add the products from this page to our complete list
        all_active_products.extend(products_on_this_page)

        # Check whether another page exists
        more_products_available = page_information["hasNextPage"]

        if not more_products_available:
            break

        # Save the bookmark for the next request
        where_to_continue = page_information["endCursor"]

        if not where_to_continue:
            raise RuntimeError(
                "Shopify did not provide the next page position."
            )

    # Return every product retrieved from Shopify
    return all_active_products
