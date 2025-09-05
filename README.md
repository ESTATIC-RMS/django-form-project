# Django Profile Management System

A comprehensive Django web application for managing user profiles with form handling, file uploads, and candidate management features.

## 🚀 Features

- **User Profile Management**: Complete profile creation with personal details
- **Form Validation**: Comprehensive form validation with custom validators
- **File Upload Support**: Profile image and document upload functionality
- **Candidate Listing**: View and manage candidate profiles
- **Responsive Design**: Bootstrap-powered responsive UI
- **Custom Template Filters**: Custom Django template filters for data formatting
- **Admin Interface**: Django admin integration for profile management

## 📋 Project Structure

```
authentication/
├── core/                    # Django project settings
│   ├── settings.py         # Project configuration
│   ├── urls.py            # Main URL routing
│   └── wsgi.py            # WSGI configuration
├── userauths/             # Main application
│   ├── models.py          # Profile model definition
│   ├── views.py           # View functions
│   ├── forms.py           # Django forms
│   ├── admin.py           # Admin configuration
│   ├── urls.py            # App URL routing
│   ├── templates/         # HTML templates
│   │   └── userauths/
│   │       ├── base.html      # Base template
│   │       ├── home.html      # Home page with form
│   │       └── candidate.html # Candidate details page
│   └── templatetags/      # Custom template filters
│       └── customFilter.py
├── media/                 # File uploads
│   ├── profileimage/      # Profile images
│   └── doc/              # Documents
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### 1. Clone the Repository
```bash
git clone <repository-url>
cd authentication
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 📝 Usage

### Profile Creation
1. Navigate to the home page
2. Fill out the profile form with:
   - Personal information (name, date of birth, gender)
   - Address details (locality, city, state, PIN code)
   - Contact information (mobile, email)
   - Job preferences (preferred cities)
   - Optional profile image and document upload
3. Submit the form to create a new profile

### Viewing Candidates
- The right sidebar displays a list of all registered candidates
- Click on any candidate name to view their detailed profile
- Each candidate profile shows all submitted information

### Admin Interface
- Access the admin panel at `http://127.0.0.1:8000/admin/`
- Manage profiles, view submissions, and perform administrative tasks

## 🏗️ Technical Details

### Models
- **Profile Model**: Stores complete user profile information including:
  - Personal details (name, DOB, gender)
  - Address information (locality, city, state, PIN)
  - Contact details (mobile, email)
  - Job preferences (multiple city selection)
  - File uploads (profile image, documents)

### Forms
- **ProfileForm**: Comprehensive form with:
  - Custom validation for PIN codes (6 digits)
  - Mobile number validation (11 digits)
  - Radio buttons for gender selection
  - Checkbox multiple selection for job cities
  - File upload fields for images and documents

### Validation Features
- PIN code must be exactly 6 digits
- Mobile number must be exactly 11 digits
- Email format validation
- File upload validation
- Required field validation

### Custom Features
- **Custom Template Filter**: `remove_chars` filter to clean up display formatting
- **Image Preview**: JavaScript-powered image preview on file selection
- **Responsive Design**: Bootstrap 5 integration for mobile-friendly interface

## 🎨 UI/UX Features

- **Bootstrap 5**: Modern, responsive design
- **Form Validation**: Real-time error display
- **Image Preview**: Live preview of uploaded profile images
- **Clean Layout**: Two-column layout with form and candidate list
- **Error Handling**: Comprehensive error messages and validation feedback

## 📁 File Uploads

The application supports:
- **Profile Images**: Uploaded to `media/profileimage/`
- **Documents**: Uploaded to `media/doc/`
- **File Types**: Images (PNG, JPG) and documents (PDF, DOCX, etc.)

## 🔧 Configuration

### Settings
- **Database**: SQLite (default) - easily configurable for PostgreSQL/MySQL
- **Media Files**: Configured for file uploads
- **Static Files**: Bootstrap CDN integration
- **Security**: CSRF protection enabled

### Customization
- Modify `STATE_CHOICES` in `models.py` for different regions
- Update `JOB_CITY_CHOICES` in `forms.py` for different cities
- Customize validation rules in model validators
- Modify templates for different UI themes

## 🚀 Deployment

### Production Considerations
1. Change `DEBUG = False` in settings
2. Set a secure `SECRET_KEY`
3. Configure proper database (PostgreSQL recommended)
4. Set up static file serving
5. Configure media file serving
6. Set up proper logging
7. Use environment variables for sensitive data

### Environment Variables
```bash
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues or have questions:
1. Check the Django documentation
2. Review the code comments
3. Open an issue in the repository
4. Contact the development team

## 🔄 Future Enhancements

- User authentication and login system
- Profile editing functionality
- Search and filtering capabilities
- Export functionality (PDF, Excel)
- Email notifications
- API endpoints for mobile integration
- Advanced file validation
- Profile analytics and reporting

---

**Built with ❤️ using Django 5.2.5**
