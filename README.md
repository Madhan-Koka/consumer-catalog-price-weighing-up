# 🛍️ Consumer Catalog Price Weighing Up

A Django-based web application that compares product prices across **Amazon, Flipkart, Myntra, and Ajio** in real-time. Users can search for products, save them, track price history, and set price alerts to get notified when prices drop.


---

## 🚀 Features

- **Multi-Site Price Comparison** - Search across Amazon, Flipkart, Myntra, and Ajio simultaneously
- **Real-Time Web Scraping** - Get live product prices sorted from low to high
- **User Authentication** - Secure registration and login system
- **Save Products** - Track your favorite products
- **Price History Tracking** - Monitor price changes over time
- **Price Alerts** - Get notified when prices drop below your target
- **Responsive Design** - Works seamlessly on desktop and mobile
- **Clean UI** - Modern, intuitive interface with Bootstrap

---

## 🛠️ Tech Stack

### Backend
- **Python 3.12**
- **Django 5.x** - Web framework
- **MySQL** - Database
- **BeautifulSoup4** - Web scraping
- **Requests** - HTTP library

### Frontend
- **HTML5 & CSS3**
- **Bootstrap 4** - Responsive design
- **JavaScript** - Interactive features


---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- MySQL Server
- Git
- Django==5.0.1
- mysqlclient==2.2.4
- beautifulsoup4==4.12.3
- requests==2.31.0

---

## ⚙️ Installation

### 1. Clone the Repository

### 2. Create Virtual Environment

### 3. Install Dependencies

### 4. Set Up MySQL Database

### 5. Configure Database Settings
Edit `consumer_catalog_price_weighing_up/settings.py`:

### 6. Run Migrations

### 7. Create Superuser (Optional)

### 8. Run Development Server
## 📁 Project Structure

consumer-catalog-price-weighing-up/
│
├── catalog/ # Main application
│ ├── management/
│ │ └── commands/
│ │ └── scrape_prices.py # Management command for scraping
│ ├── templates/
│ │ └── catalog/ # HTML templates
│ ├── models.py # Database models
│ ├── views.py # View functions
│ ├── forms.py # Django forms
│ ├── urls.py # URL routing
│ ├── scraper.py # Web scraping logic
│ └── utils.py # Utility functions
│
├── consumer_catalog_price_weighing_up/ # Project settings
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── manage.py
└── README.md

---

## 🎯 Usage

### Search for Products
1. Go to the home page
2. Enter a product name in the search bar (e.g., "laptop", "phone")
3. Click **Live Search**
4. View results from all 4 websites sorted by price

### Save Products
1. Click the **💾 Save** button on any search result
2. Product is added to your saved list

### Set Price Alerts
1. Login to your account
2. Go to saved products
3. Click **🔔 Alert** on any product
4. Enter your target price
5. Get notified when price drops

### Delete Products
1. Click **🗑️ Delete** on any saved product
2. Confirm deletion

---

## 🔧 Management Commands

### Scrape Prices for All Saved Products

---

## 🐛 Known Issues

- **Web Scraping Limitations**: E-commerce sites may block scrapers or change HTML structure
- **Anti-Bot Protection**: Some sites use Cloudflare or similar protection
- **Rate Limiting**: Too many requests may result in temporary blocks

### Solutions:
- Use proxy services (ScraperAPI, Bright Data)
- Implement Selenium for JavaScript-heavy sites
- Use official APIs where available

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---



## 👨‍💻 Author

**Madhan Koka**
- GitHub: [@Madhan-Koka](https://github.com/Madhan-Koka)
- Project Link: [Consumer Catalog Price Weighing Up](https://github.com/Madhan-Koka/consumer-catalog-price-weighing-up)

---

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap
- BeautifulSoup4
- All contributors and testers


---

## 📞 Support

If you have any questions or issues, please open an issue on GitHub or contact me directly.
madhan78934@gmail.com
---

**⭐ If you like this project, please give it a star!**
