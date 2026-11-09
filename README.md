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

**Objective:** Improve the storefront by displaying discount percentages and making promotional pricing clearer to customers.

### Implementation

- Customized the Shopify Dawn theme using Liquid and CSS.
- Calculated discount percentages by comparing original and current product prices.
- Added a styled percentage-based discount badge for discounted products.
- Updated the cart to display discount-related information.
- Preserved the existing Dawn theme structure and functionality.

### How It Works

The discount is calculated when the original price (`compare_at_price`) exceeds the current selling price (`price`).

**Discount % = ((Original Price − Sale Price) / Original Price) × 100**

For example, an item originally priced at 15 KWD and reduced to 12 KWD has a **20% discount**.

### Main Files

| File | Responsibility |
|---|---|
| `snippets/price.liquid` | Product pricing and discount percentage display |
| `assets/assessment-discount.css` | Discount badge styling |
| `sections/main-cart-items.liquid` | Cart discount information |
| `layout/theme.liquid` | Loads the custom discount stylesheet |

---

## Q3 — Shopify Product Exporter (Python)

**Objective:** Develop a standalone Python script that retrieves active Shopify products and exports their information into a structured CSV file.

### Implementation

- Integrated Python with Shopify's Admin GraphQL API.
- Retrieved active products using GraphQL queries.
- Implemented cursor-based pagination for product retrieval.
- Extracted product IDs, titles, prices, collections, and tags.
- Determined sale status by comparing variant prices.
- Generated a CSV file containing the required columns.
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
| `shopify_api.py` | Shopify authentication, product retrieval, and pagination |
| `product_export.py` | Product formatting and CSV generation |
| `product_rec.py` | Main workflow coordination |

### Testing Results

- **10 active products retrieved**
- **10 products successfully exported**
- **3 discounted products correctly identified**
- Pagination and incomplete nested-data checks implemented

---

## Project Structure

The following structure highlights the assessment-specific files and the relevant Shopify theme components.

```text
shopify-assessment/
│
├── assets/
│   └── assessment-discount.css
│
├── layout/
│   └── theme.liquid
│
├── snippets/
│   └── price.liquid
│
├── sections/
│   └── main-cart-items.liquid
│
├── scripts/
│   ├── shopify_settings.py
│   ├── shopify_api.py
│   ├── product_export.py
│   └── product_rec.py
│
├── active_products.csv
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

*The structure above highlights the files relevant to Q1 and Q3. Other standard Dawn theme files and directories are omitted for clarity.*

### Architecture

**Q1 — Storefront**

Shopify product pricing → Liquid discount calculation → Discount badge styling → Storefront and cart display.

**Q3 — Product Export**

Environment configuration → Shopify authentication → GraphQL product retrieval → Product data formatting → CSV generation.

---

## Project Notes

The implementation focuses on readable code, separation of responsibilities, and compatibility with Shopify's existing theme and API architecture.

**Q2 — Reusable Media & Product Carousel** will be documented once implemented.