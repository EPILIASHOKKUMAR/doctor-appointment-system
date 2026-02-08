# Backend - Doctor Appointment System

Flask-based REST API backend for the doctor appointment system.

## Structure

```
backend/
├── app.py              # Main Flask application with all routes
├── models.py           # Database models (User, Hospital, Doctor, Appointment, etc.)
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (API keys, DB credentials)
├── clinic_db.sql      # Database schema and initial data
└── setup_db.py        # Database setup script
```

## Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment**
   - Copy `.env.example` to `.env`
   - Add your API keys:
     ```
     GEMINI_API_KEY=your_gemini_api_key
     GOOGLE_MAPS_API_KEY=your_google_maps_key
     ```

3. **Setup Database**
   ```bash
   python setup_db.py
   ```

4. **Run Server**
   ```bash
   python app.py
   ```

Server runs on: `http://localhost:5000`

## Database

- **Type**: MySQL
- **Name**: clinic_db
- **Connection**: `mysql+pymysql://root:password@localhost/clinic_db`

## API Endpoints

### Authentication
- `POST /login` - User login
- `POST /register` - User registration
- `GET /logout` - User logout

### Patient Routes
- `GET /patient/dashboard` - Patient dashboard
- `GET /patient/medical-history` - View medical history
- `POST /book_appointment/<doctor_id>` - Book appointment
- `POST /cancel_appointment/<appointment_id>` - Cancel appointment

### Doctor Routes
- `GET /doctor/dashboard` - Doctor dashboard
- `GET /doctor/appointment/<appointment_id>` - View/update appointment
- `POST /update_appointment_status` - Update appointment status

### Hospital Routes
- `GET /hospital/dashboard` - Hospital admin dashboard
- `POST /add_doctor` - Add new doctor
- `GET /hospitals` - List all hospitals
- `GET /hospital/<hospital_id>` - Hospital details

### Emergency
- `GET /emergency` - Emergency services page
- `POST /emergency/contacts/add` - Add emergency contact

## Technologies

- **Framework**: Flask
- **Database**: MySQL with SQLAlchemy ORM
- **Authentication**: Session-based with password hashing
- **AI**: Google Gemini API
- **Maps**: Google Maps API
