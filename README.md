# Sammissi Shops – E-commerce Product API - BUILT BY SAMUEL CHIBUZOR UBA 

A **Django & Django REST Framework (DRF)** backend API for managing products in an e-commerce platform. This project demonstrates real-world backend development tasks, including **CRUD operations for products and categories, user authentication, filtering, search, and RESTful API design**.

---

## **Features**

### Product Management (CRUD)
- Create, Read, Update, and Delete products
- Product attributes:  
  - Name  
  - Description  
  - Price  
  - Category  
  - Stock Quantity  
  - Image URL  
  - Created Date
- Validation for required fields (Name, Price, Stock Quantity)

### User Management
- Authentication using Django’s built-in auth system
- Only authenticated users can manage products
- Optional future enhancement: JWT token-based authentication

### Category Management
- Create, Read, Update, Delete product categories
- Products are linked to categories for better organization

### Search & Filtering
- Search products by **name** or **category**
- Filter products by **category**, **price range**, and **stock availability**
- Partial matching supported for flexible search

### Pagination (Optional)
- Can be configured via DRF pagination settings

### API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/playground/products/` | GET | List all products |
| `/playground/products/<id>/` | GET | Retrieve product details |
| `/playground/products/` | POST | Create a new product (authenticated users) |
| `/playground/products/<id>/` | PUT/PATCH | Update a product (owner only) |
| `/playground/products/<id>/` | DELETE | Delete a product (owner only) |
| `/playground/categories/` | GET | List all categories |
| `/playground/categories/<id>/` | GET | Retrieve category details |
| `/playground/categories/` | POST | Create a category (authenticated users) |
| `/playground/categories/<id>/` | PUT/PATCH | Update a category (authenticated users) |
| `/playground/categories/<id>/` | DELETE | Delete a category (authenticated users) |

> Filter example: `/playground/products/?category=Electronics&min_price=100&max_price=500&in_stock=True`  
> Search example: `/playground/products/?search=phone`

---

## **Installation**

### Prerequisites
- Python 3.10+  
- pip or pipenv  
- Git  

### Steps

1. Clone the repository:

```bash
git clone https://github.com/yourusername/sammissishops.git
cd sammissishops
