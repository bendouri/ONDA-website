# 🛫 ONDA Website - Office National des Aéroports

<div align="center">
  <img src="static/images/logo.png" alt="ONDA Logo" width="200"/>
  <h3>Morocco's National Airports Office - Complete Web Platform</h3>
  <p>
    <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
    <img src="https://img.shields.io/badge/Flask-2.3.3-green.svg" alt="Flask">
    <img src="https://img.shields.io/badge/MySQL-8.0+-orange.svg" alt="MySQL">
    <img src="https://img.shields.io/badge/Bootstrap-5.3-purple.svg" alt="Bootstrap">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  </p>
</div>

## 🌟 Overview

ONDA Website is a comprehensive Flask web application for Morocco's Office National des Aéroports (National Airports Office). This modern, full-featured platform provides complete airport services management, flight information, user authentication, and administrative capabilities.

### ✨ Key Highlights
- 🏢 **Complete Airport Management System**
- ✈️ **Real-time Flight Information**
- 👥 **User Authentication & Admin Panel**
- 🍽️ **Restaurant & Shopping Directory**
- 🚌 **Transportation Services**
- 💼 **Job Applications & Tender Management**
- 📱 **Fully Responsive Design**
- 🌍 **Multi-language Ready**

## 🚀 Features

### 🎯 Core Functionalities

#### 👑 **Admin Features**
- **Dashboard**: Comprehensive statistics and activity logs
- **User Management**: Create, edit, delete users with role-based access
- **Flight Management**: Manage flights with 202 worldwide destinations
- **Content Management**: Restaurants, transport, shopping centers
- **Job Applications**: Complete recruitment system with document upload
- **Tender Management**: Manage public tenders with PDF documents
- **Contact Management**: Handle user inquiries and messages
- **Activity Logs**: Full audit trail of all admin actions

#### 🌐 **Public Features**
- **Flight Search**: Real-time flight information and search
- **Services Directory**: Restaurants, transport, shopping with advanced filters
- **Travel Documents**: Passport, visa, and travel requirements guide
- **Job Portal**: Browse and apply for positions without registration
- **Tender Portal**: Access public tenders and download documents
- **Contact System**: Multi-channel contact with form submission
- **Responsive Design**: Perfect experience on all devices

#### 🔐 **Authentication & Security**
- **Secure Login**: Password hashing with Werkzeug
- **Session Management**: Flask-Login integration
- **Role-based Access**: Admin vs regular user permissions
- **File Upload Security**: Validated file types and sizes
- **SQL Injection Protection**: SQLAlchemy ORM

## 🛠️ Technology Stack

### Backend
- **Framework**: Flask 2.3.3
- **Database**: MySQL 8.0+
- **ORM**: SQLAlchemy
- **Authentication**: Flask-Login
- **File Handling**: Werkzeug
- **Password Security**: Werkzeug Security

### Frontend
- **CSS Framework**: Bootstrap 5.3
- **Icons**: Font Awesome 6.4
- **Maps**: Leaflet.js
- **Animations**: AOS (Animate On Scroll)
- **JavaScript**: Vanilla JS + jQuery

### Database Schema
- **Users**: Authentication and role management
- **Flights**: Flight information and schedules
- **Airports**: 20 Moroccan airports with coordinates
- **Restaurants**: Dining options with ratings and filters
- **Transport**: Transportation services by city and type
- **Shopping**: Shopping centers and traditional markets
- **JobOffers**: Employment opportunities
- **JobApplications**: Candidate applications with file uploads
- **Tenders**: Public tender announcements
- **Contacts**: User inquiries and messages
- **ActivityLogs**: Complete audit trail

## 📋 Prerequisites

- **Python 3.8+**
- **MySQL 8.0+** (via XAMPP recommended)
- **Git** (for version control)
- **Modern Web Browser**

## ⚡ Installation & Setup

### 1. Install XAMPP
1. Download XAMPP from [https://www.apachefriends.org/](https://www.apachefriends.org/)
2. Install and start Apache and MySQL services

### 2. Clone/Download Project
```bash
# If using git
git clone <repository-url>
cd ONDA---website-main

# Or download and extract the ZIP file
```

### 3. Run Setup Script
```bash
python setup.py
```

The setup script will:
- Check Python version compatibility
- Verify MySQL connection
- Install Python dependencies
- Create necessary directories
- Initialize the database with sample data
- Create configuration files

### 4. Start the Application
```bash
python app.py
```

### 5. Access the Website
- **Website**: http://localhost:5000
- **phpMyAdmin**: http://localhost/phpmyadmin
- **Database**: onda_db

## 🔐 Default Credentials

### Admin Account
- **Username**: admin
- **Password**: admin123
- **Access**: Full administrative privileges

### User Account
- **Username**: user
- **Password**: user123
- **Access**: Standard user privileges

## 📁 Project Structure

```
ONDA---website-main/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── init_db.py            # Database initialization script
├── setup.py              # Automated setup script
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── templates/           # HTML templates
│   ├── base.html        # Base template
│   ├── index.html       # Homepage
│   ├── login.html       # Login page
│   ├── register.html    # Registration page
│   ├── contact.html     # Contact form
│   ├── transport.html   # Transport listings
│   ├── food.html        # Restaurant listings
│   ├── shopping.html    # Shopping centers
│   ├── services.html    # Services page
│   ├── info.html        # About page
│   ├── documents.html   # Travel documents
│   └── admin/           # Admin templates
│       └── dashboard.html
├── static/              # Static files
│   ├── css/            # Stylesheets
│   ├── js/             # JavaScript files
│   ├── images/         # Images
│   └── uploads/        # User uploads
└── instance/           # Instance-specific files
```

## 🗄️ Database Schema

### Users Table
- id, username, email, password_hash, is_admin, created_at

### Airports Table
- id, name, city, code, latitude, longitude, description, is_active

### Restaurants Table
- id, name, city, cuisine_type, description, address, phone, rating, image_url, is_active

### Transport Table
- id, name, type, city, description, price_range, contact_info, image_url, is_active

### Shopping Table
- id, name, city, type, description, address, opening_hours, image_url, is_active

### Contact Table
- id, name, email, subject, message, created_at, is_read

### News Table
- id, title, content, author, created_at, is_published, image_url

## 🔧 Configuration

### Database Configuration
Edit `app.py` or use environment variables:
```python
SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/onda_db'
```

### Environment Variables
Create a `.env` file based on `.env.example`:
```bash
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=mysql://root:@localhost/onda_db
```

## 🚦 API Endpoints

### Public Endpoints
- `GET /` - Homepage
- `GET /services` - Services page
- `GET /transport` - Transport listings
- `GET /food` - Restaurant listings
- `GET /shopping` - Shopping centers
- `GET /contact` - Contact form
- `POST /contact` - Submit contact form
- `GET /api/airports` - Get all airports (JSON)
- `GET /api/search` - Search functionality (JSON)

### Authentication Endpoints
- `GET /login` - Login form
- `POST /login` - Process login
- `GET /register` - Registration form
- `POST /register` - Process registration
- `GET /logout` - Logout user

### Protected Endpoints
- `GET /dashboard` - User dashboard
- `GET /admin` - Admin dashboard (admin only)

## 🎨 Customization

### Adding New Pages
1. Create HTML template in `templates/`
2. Add route in `app.py`
3. Update navigation in `base.html`

### Adding New Database Models
1. Define model class in `app.py`
2. Create migration: `flask db migrate`
3. Apply migration: `flask db upgrade`

### Styling
- Edit `static/css/style.css` for custom styles
- Bootstrap 5 classes available throughout

## 🔍 Troubleshooting

### Common Issues

**MySQL Connection Error**
- Ensure XAMPP MySQL is running
- Check database credentials in `app.py`
- Verify database `onda_db` exists

**Import Errors**
- Run `pip install -r requirements.txt`
- Check Python version (3.7+ required)

**Template Not Found**
- Ensure templates are in `templates/` directory
- Check template names in route functions

**Static Files Not Loading**
- Verify files are in `static/` directory
- Check Flask static file configuration

### Database Reset
To reset the database with fresh sample data:
```bash
python init_db.py
```

## 📞 Support

For support and questions:
- **Email**: contact@onda.ma
- **Documentation**: Check this README
- **Issues**: Create an issue in the repository

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License. See LICENSE file for details.

## 🙏 Acknowledgments

- ONDA (Office National des Aéroports) for the inspiration
- Flask community for the excellent framework
- Bootstrap team for the responsive framework
- Leaflet.js for the mapping functionality

---

**Made with ❤️ for ONDA - Office National des Aéroports**
