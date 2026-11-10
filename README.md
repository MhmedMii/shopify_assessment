<img width="1441" height="410" alt="CSV_File_Export" src="https://github.com/user-attachments/assets/f822d350-171e-4201-9c42-8295f752e405" /># Shopify Developer Assessment

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
| `layout/theme.liquid` | Loads the custom discount stylesheet inside the HTML `<head>` |

### Screenshots

![Product discount example] <img width="482" height="483" alt="Classic_Shirt_Discount" src="https://github.com/user-attachments/assets/f17b52df-c117-48a0-9363-95ae796496ba" />


![Collection discount examples] <img width="569" height="594" alt="Products_Discount" src="https://github.com/user-attachments/assets/ef3285be-f0e7-4dfe-83d0-2b82ebbf80aa" />


![Additional product listings] <img width="1519" height="938" alt="All_Products_with_discount" src="https://github.com/user-attachments/assets/8efc7a60-b437-4d76-b0b0-916ea5cfe6b5" />


![Remaining collection products] <img width="907" height="432" alt="remaining_products_with_discount" src="https://github.com/user-attachments/assets/8e4f07ff-6383-40a5-9a7f-62d9967559f4" />


![Cart discount percentages] <img width="1382" height="813" alt="Cart_Discount" src="https://github.com/user-attachments/assets/24b2ef07-d901-4dce-8ce5-b98e92c75599" />


### Verification Results

- Verified the percentage badge on product listings, individual product pages, and the cart.
- Confirmed **20%** for Classic Black T-Shirt, **25%** for White Cotton Shirt, and **29%** (rounded) for Slim Fit Jeans.
- Confirmed regular-priced products remain without a percentage-discount badge.
- Moved the custom discount stylesheet reference inside the HTML `<head>`.
- Shopify Theme Check reported **0 errors and 9 existing warnings**; changes were committed and synchronized with GitHub.

---

## Q2 — Reusable Media & Product Carousel (Partially Completed)

**Objective:** Build a reusable Shopify section supporting Media and Product Carousel blocks with configurable settings.

### Implementation

- Created a custom reusable Shopify section with Media and Product Carousel block definitions (maximum two blocks, one of each type).
- Added configurable top padding, bottom padding, and spacing between blocks.
- Created a dedicated Media snippet for image and Shopify-hosted video rendering logic.
- Added image and video picker settings in the Shopify Theme Editor.
- Added responsive media sizing through a separate CSS asset.
- Added button label and link settings and conditional link markup in the Media snippet; complete styling and positioning were not implemented.

### Screenshots

![Media section rendering and settings] <img width="1488" height="813" alt="Media_rendering" src="https://github.com/user-attachments/assets/c11e8364-0f6f-49e9-a760-1b97156413dc" />


![Media block configuration in Theme Editor] <img width="237" height="457" alt="Media picker   button fields" src="https://github.com/user-attachments/assets/24df325f-7536-4560-aae7-cf1039aa7ac4" />


### Verification Results

- Added the custom section in Shopify's Theme Editor and selected a media image successfully.
- Verified the selected image renders on the storefront preview and checked its desktop layout.
- Confirmed the section's padding, spacing and Media settings appear in the editor.
- Shopify Theme Check reported **0 errors** with **9 existing warnings**.
- Video upload testing was blocked by the development store's account restrictions; video rendering remains unverified.

### Remaining Requirements

- Complete and test button colors, styling and left/center/right placement over media.
- Implement collection product selection, up to three pinned products, maximum carousel elements, duplicate prevention and product cards.
- Implement configurable visible-product counts (default 4 desktop / 2 mobile) and carousel navigation.
- Ensure Media renders before Product Carousel when both blocks exist.
- Ensure multiple instances are independently styled and implement first-instance media priority with lazy loading for later instances.
- Complete mobile, multiple-instance and video testing.

### Implementation Status

The remaining requirements were reviewed and the implementation approach was planned, but development was not completed within the assessment timeframe. Completed functionality is documented separately from outstanding requirements.

### Main Files

| File | Responsibility |
|---|---|
| `sections/assessment-media-carousel.liquid` | Section schema, block definitions, padding and spacing settings |
| `snippets/assessment-media.liquid` | Media rendering and conditional button link markup |
| `assets/assessment-media-carousel.css` | Desktop/mobile media dimensions and crop styling |

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

### Screenshot

![Product export CSV with Boolean Sale values] <img width="1441" height="410" alt="CSV_File_Export" src="https://github.com/user-attachments/assets/9b9333c3-de5c-4c06-b189-f6f9a2aa2637" />



### CSV Output

The generated `active_products.csv` contains:

| Column | Description |
|---|---|
| `Id` | Shopify product ID |
| `Title` | Product title |
| `Price` | Lowest retrieved variant price |
| `Collections` | Product collection names |
| `Tags` | Product tags |
| `Sale` | Boolean (`True` / `False`), based on variant discount status |

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
- **3 discounted products correctly identified** (`True`), with **7 regular-priced products** (`False`)
- Automated CSV validation passed: 10 products exported, 3 `True`, 7 `False`
- Pagination and incomplete nested-data checks implemented

---

## Project Structure

The following structure highlights the assessment-specific files and the relevant Shopify theme components.

```text
shopify-assessment/
│
├── assets/
│   ├── assessment-discount.css
│   └── assessment-media-carousel.css
│
├── layout/
│   └── theme.liquid
│
├── snippets/
│   ├── price.liquid
│   └── assessment-media.liquid
│
├── sections/
│   ├── main-cart-items.liquid
│   └── assessment-media-carousel.liquid
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

*The structure above highlights the assessment-specific files relevant to Q1, the partial Q2 implementation and Q3. Other standard Dawn theme files and directories are omitted for clarity.*

### Architecture

**Q1 — Storefront**

Shopify product pricing → Liquid discount calculation → Discount badge styling → Storefront and cart display.

**Q2 — Media Section**

Section schema and settings → Media block → Dedicated Liquid snippet → Responsive CSS → Storefront image rendering.

**Q3 — Product Export**

Environment configuration → Shopify authentication → GraphQL product retrieval → Product data formatting → CSV generation.

---

## Project Notes

The implementation focuses on readable code, separation of responsibilities, and compatibility with Shopify's existing theme and API architecture.

**Assessment status:** Q1 and Q3 are complete. Q2 has been partially implemented; verified behavior and remaining requirements are detailed above.
