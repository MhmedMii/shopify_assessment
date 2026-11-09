# Shopify Developer Assessment

A technical assessment demonstrating Shopify theme customization and product data integration using the Shopify Admin GraphQL API.

## Technologies Used

- Shopify Dawn Theme
- Shopify Liquid, HTML, CSS
- Python
- Shopify Admin GraphQL API
- Git & GitHub

---

## Q1 — Discount Percentage Display

**Objective:** Improve the storefront by displaying discount percentages on products and making promotional pricing clearer to customers.

### Implementation

- Customized the Shopify Dawn theme using Liquid and CSS.
- Calculated discount percentages by comparing the original price with the current selling price.
- Added a styled percentage-based discount badge for discounted products.
- Updated the cart to display discount-related information.
- Preserved the existing Dawn theme structure and functionality.

### How It Works

The discount is calculated when the original price (`compare_at_price`) is higher than the current selling price (`price`).

**Discount % = ((Original Price − Sale Price) / Original Price) × 100**

For example, an item originally priced at 15 KWD and reduced to 12 KWD displays a **20% discount**.

**Main files:**
- `snippets/price.liquid`
- `assets/assessment-discount.css`
- `sections/main-cart-items.liquid`

---

## Q3 — Shopify Product Exporter (Python)

**Objective:** Develop a standalone Python script that retrieves active products from Shopify and exports the required information to CSV.

### Implementation

- Integrated Python with the Shopify Admin GraphQL API.
- Retrieved active products using GraphQL queries.
- Implemented cursor-based pagination to retrieve additional product pages.
- Extracted product IDs, titles, prices, collections, and tags.
- Determined sale status by comparing current and original variant prices.
- Generated a structured CSV file with the required columns.
- Added validation to detect incomplete variant or collection results.

### CSV Output

The generated `active_products.csv` contains:

| Column | Description |
|---|---|
| `Id` | Shopify product ID |
| `Title` | Product title |
| `Price` | Lowest retrieved variant price |
| `Collections` | Product collection names |
| `Tags` | Product tags |
| `Sale` | Yes or No, based on variant discount status |

### Code Organization

The Python implementation follows the Single Responsibility Principle (SRP) to keep the code organized and maintainable.

| File | Responsibility |
|---|---|
| `shopify_settings.py` | Configuration management |
| `shopify_api.py` | Shopify authentication and product retrieval |
| `product_export.py` | Product formatting and CSV generation |
| `product_rec.py` | Main workflow coordination |

### Testing Results

The exporter was successfully tested using Shopify sample product data:

- **10 active products retrieved**
- **10 products exported to CSV**
- **3 discounted products correctly identified**
- Product pagination and incomplete nested-data checks implemented

---

## Project Notes

This project focuses on Shopify theme customization, API integration, and maintainable Python development.

The implementation prioritizes clear code structure, separation of responsibilities, and compatibility with Shopify's existing architecture.

**Q2 — Reusable Media & Product Carousel** will be documented after implementation.
