# Smart Clinic Appointment Scheduler

A beautiful and efficient web application for managing clinic appointments. This system helps clinics schedule and manage patient appointments while preventing conflicts and optimizing doctor availability.

## Features

- Beautiful and responsive modern UI
- Easy appointment scheduling
- Automatic conflict prevention
- Real-time available time slot updates
- Easy appointment cancellation
- Doctor specialization support
- Patient information management

## Installation

1. Make sure you have Python 3.x installed on your system.

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your web browser and navigate to: `http://localhost:5000`

## Sample Data

The application comes with sample doctor data pre-loaded:
- Dr. John Smith (General Medicine)
- Dr. Sarah Johnson (Pediatrics)
- Dr. Michael Brown (Cardiology)

## Technical Details

- Built with Flask web framework
- SQLite database with SQLAlchemy ORM
- Bootstrap 5 for responsive UI
- Font Awesome icons
- jQuery for dynamic updates

## Usage

1. Navigate to the home page to see available doctors
2. Click "New Appointment" to schedule an appointment
3. Select a doctor, enter patient details, and choose an available time slot
4. View and manage appointments in the appointments page
5. Cancel appointments when needed

## Time Slots

- Appointments are scheduled in 30-minute slots
- Available hours: 9:00 AM to 5:00 PM
- The system automatically prevents double-booking
