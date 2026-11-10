import csv
from decimal import Decimal

def prepare_product_for_csv(shopify_product):
    # Read the product variants
    product_variants = shopify_product["variants"]["nodes"]

    # Find the lowest selling price
    product_prices = [
        Decimal(variant["price"])
        for variant in product_variants
    ]

    lowest_product_price = min(product_prices) if product_prices else None

    # Check whether at least one variant is on sale
    product_is_on_sale = any(
        variant["compareAtPrice"] is not None
        and Decimal(variant["compareAtPrice"]) > Decimal(variant["price"])
        for variant in product_variants
    )

    # Get the names of the product's collections
    product_collection_names = [
        collection["title"]
        for collection in shopify_product["collections"]["nodes"]
    ]

    # Return the product information in CSV column format
    return {
        "Id": shopify_product["id"],
        "Title": shopify_product["title"],
        "Price": (
            f"{lowest_product_price:.3f}"
            if lowest_product_price is not None
            else ""
        ),
        "Collections": ", ".join(product_collection_names),
        "Tags": ", ".join(shopify_product["tags"]),
        "Sale": product_is_on_sale,
    }


def save_products_to_csv(prepared_products, file_location):
    # Keep the CSV columns in the order required by the assessment
    csv_column_names = [
        "Id",
        "Title",
        "Price",
        "Collections",
        "Tags",
        "Sale",
    ]

    # Create the CSV file and write the product information
    with open(
        file_location,
        "w",
        newline="",
        encoding="utf-8-sig",
    ) as csv_file:
        csv_writer = csv.DictWriter(
            csv_file,
            fieldnames=csv_column_names,
            lineterminator="\n",
            )
        csv_writer.writeheader()
        csv_writer.writerows(prepared_products)

    return file_location
