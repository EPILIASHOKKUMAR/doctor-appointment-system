# Frontend - Doctor Appointment System

HTML/CSS/JavaScript templates for the doctor appointment system.

## Structure

```
frontend/
└── templates/
    ├── base.html                    # Base template with navbar
    ├── index.html                   # Homepage
    ├── login.html                   # Login page
    ├── register.html                # Registration page
    ├── hospitals.html               # Hospital listing
    ├── hospital_details.html        # Hospital details
    ├── book_appointment.html        # Appointment booking
    ├── emergency.html               # Emergency services
    ├── location_test.html           # Location testing
    │
    ├── patient/
    │   ├── dashboard.html           # Patient dashboard
    │   ├── appointment_details.html # Appointment details
    │   ├── medical_history.html     # Medical history
    │   ├── emergency_contacts.html  # Emergency contacts
    │   └── ambulance_bookings.html  # Ambulance bookings
    │
    ├── doctor/
    │   ├── dashboard.html           # Doctor dashboard
    │   └── appointment_details.html # Appointment management
    │
    └── hospital/
        ├── dashboard.html           # Hospital admin dashboard
        ├── register.html            # Hospital registration
        └── add_doctor.html          # Add doctor form
```

## Features

### Patient Interface
- View and book appointments
- Access medical history
- Manage emergency contacts
- Request ambulance services
- Real-time location tracking

### Doctor Interface
- View pending/upcoming appointments
- Update patient records
- Add diagnosis and prescriptions
- Approve/complete appointments

### Hospital Admin Interface
- Manage hospital profile
- Add/manage doctors
- View all appointments
- Monitor hospital statistics

## Technologies

- **HTML5** - Semantic markup
- **CSS3** - Bootstrap 5 for styling
- **JavaScript** - Vanilla JS for interactivity
- **Jinja2** - Template engine (Flask)
- **Google Maps API** - Location services
- **Font Awesome** - Icons

## Integration

These templates are rendered by the Flask backend (`backend/app.py`). They use:
- Jinja2 templating syntax (`{{ }}`, `{% %}`)
- Flask session data for authentication
- Flask flash messages for notifications
- AJAX calls to backend API endpoints

## Running

Templates are served by the Flask backend. To view:

1. Start the backend server:
   ```bash
   cd backend
   python app.py
   ```

2. Open browser to: `http://localhost:5000`

## Customization

- Modify templates in `templates/` directory
- Update styles in `<style>` tags or add external CSS
- Add JavaScript in `<script>` tags or external files
- Configure API keys in backend `.env` file
