Sammissi Shops – E-commerce Product API

Built by Samuel Chibuzor Uba

A Django & Django REST Framework (DRF) backend API for managing products in an e-commerce platform. This project demonstrates real-world backend development practices, including CRUD operations for products and categories, user authentication, filtering, search, and RESTful API design.

Features
Product Management (CRUD)

Full Create, Read, Update, Delete functionality for products.

Product attributes include:

Name

Description

Price

Category

Stock Quantity

Image URL

Created Date

Validation ensures required fields (Name, Price, Stock Quantity) are provided.

User Management

Authentication using Django’s built-in authentication system.

Only authenticated users can manage products.

Future enhancement: JWT token-based authentication for stateless API access.

Category Management

Create, Read, Update, Delete product categories.

Products are linked to categories for better organization and filtering.

Search & Filtering

Search products by name or category.

Filter products by category, price range, and stock availability.

Partial matching supported for flexible searches.

Pagination (Optional)

Configurable via DRF pagination settings.

API Endpoints
Endpoint	Method	Description
/playground/products/	GET	List all products
/playground/products/<id>/	GET	Retrieve product details
/playground/products/	POST	Create a new product (authenticated users only)
/playground/products/<id>/	PUT / PATCH	Update a product (owner only)
/playground/products/<id>/	DELETE	Delete a product (owner only)
/playground/categories/	GET	List all categories
/playground/categories/<id>/	GET	Retrieve category details
/playground/categories/	POST	Create a category (authenticated users only)
/playground/categories/<id>/	PUT / PATCH	Update a category (authenticated users only)
/playground/categories/<id>/	DELETE	Delete a category (authenticated users only)
