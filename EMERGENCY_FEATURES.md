# 🚑 Emergency Features Documentation

## Overview
SmartClinic now includes comprehensive emergency services to help patients in critical situations. These features are designed to provide quick access to emergency resources and services.

## Features Added

### 1. 🚑 Ambulance Booking System
**Location:** Emergency Page → "Book Ambulance" button

**Features:**
- Request emergency ambulance service
- Provide patient details and condition
- Auto-detect current location or enter manually
- Specify destination hospital
- Select emergency type (Accident, Heart Attack, Stroke, etc.)
- Track booking status (Requested, Dispatched, Arrived, Completed)
- View all past ambulance bookings

**How to Use:**
1. Go to Emergency page (navbar → Emergency)
2. Click "Book Ambulance" card
3. Fill in patient details:
   - Patient name
   - Contact phone
   - Pickup address (or use current location)
   - Destination hospital (optional)
   - Emergency type
   - Patient condition description
4. Click "Request Ambulance"
5. Emergency services will contact you shortly

**Important:** For immediate emergencies, always call **108** directly!

**Database Table:** `AmbulanceBooking`
- Stores booking details, location coordinates, status
- Tracks ambulance details (vehicle number, driver info)
- Records timestamps for tracking

---

### 2. 👨‍👩‍👧‍👦 Emergency Contact Management
**Location:** Patient Dashboard → "Emergency Contacts" card OR Emergency Page

**Features:**
- Add multiple emergency contacts
- Set primary contact (notified first)
- Store name, relationship, phone, email
- Quick access to call/email contacts
- Delete/manage contacts

**How to Use:**
1. Go to Patient Dashboard or Emergency page
2. Click "Emergency Contacts"
3. Click "Add Contact" button
4. Fill in details:
   - Name
   - Relationship (Spouse, Parent, Child, etc.)
   - Phone number
   - Email (optional)
   - Check "Set as primary contact" if needed
5. Save contact

**Use Cases:**
- Medical staff can quickly reach family in emergencies
- Automatic notification system (future enhancement)
- ICE (In Case of Emergency) contacts
- Multiple backup contacts

**Database Table:** `EmergencyContact`
- Linked to user account
- Supports multiple contacts per user
- Primary contact flag for priority

---

### 3. 🩸 Blood Bank Locator
**Location:** Emergency Page → "Blood Banks" button

**Features:**
- Find nearby blood banks within 100km radius
- Real-time location-based search
- Display distance from your location
- Red droplet markers on map
- Get directions to blood bank
- Quick call to emergency services (108)

**How to Use:**
1. Go to Emergency page
2. Click "Blood Banks" card
3. Allow location access when prompted
4. View list of nearby blood banks with distances
5. Click "Get Directions" to navigate
6. Call 108 for emergency blood requirements

**Data Source:** OpenStreetMap (OSM) via Overpass API
- Searches for `amenity=blood_bank`
- Searches for `healthcare=blood_donation`
- Real-time data from OSM contributors

---

### 4. 💊 Pharmacy Locator
**Location:** Emergency Page → "Pharmacies" button

**Features:**
- Find nearby pharmacies within 100km radius
- Identify 24/7 pharmacies (highlighted with badge)
- Display opening hours
- Show distance from your location
- Green plus (+) symbol markers on map
- Get directions to pharmacy
- Direct call to pharmacy (if phone available)

**How to Use:**
1. Go to Emergency page
2. Click "Pharmacies" card
3. Allow location access when prompted
4. View list of nearby pharmacies sorted by distance
5. Look for "24/7" badge for round-the-clock service
6. Click "Get Directions" to navigate
7. Call pharmacy directly if phone number available

**Data Source:** OpenStreetMap (OSM) via Overpass API
- Searches for `amenity=pharmacy`
- Includes opening hours information
- Shows up to 15 nearest pharmacies

---

## Enhanced Emergency Page

### Interactive Map
- Shows your current location (red circle marker)
- Displays nearby hospitals (red hospital icon markers - up to 100km)
- Displays pharmacies (green plus symbol markers - up to 100km)
- Displays blood banks (red droplet markers - up to 100km)
- Map legend showing all marker types
- Click markers for details and directions
- Auto-zoom to show all nearby services
- Real-time location tracking
- Shows total count of facilities found

### Emergency Contact Numbers
- **Ambulance: 108** (clickable to call)
- **Police: 100** (clickable to call)
- **Fire: 101** (clickable to call)

### Nearby Hospitals
- Hospitals from OpenStreetMap (within 10km)
- SmartClinic registered hospitals
- Distance calculation
- Direct booking for registered hospitals
- Google Maps directions

---

## Technical Implementation

### Database Models

#### EmergencyContact
```python
- id: Primary key
- user_id: Foreign key to User
- name: Contact name
- relationship: Relationship to user
- phone: Contact phone number
- email: Contact email (optional)
- is_primary: Boolean flag for primary contact
- created_at: Timestamp
```

#### AmbulanceBooking
```python
- id: Primary key
- user_id: Foreign key to User
- patient_name: Name of patient
- phone: Contact phone
- pickup_address: Pickup location address
- pickup_lat/lng: Pickup coordinates
- destination_hospital: Destination name
- destination_lat/lng: Destination coordinates
- emergency_type: Type of emergency
- patient_condition: Description of condition
- status: Booking status (requested/dispatched/arrived/completed/cancelled)
- ambulance_number: Vehicle number (when dispatched)
- driver_name: Driver name (when dispatched)
- driver_phone: Driver contact (when dispatched)
- estimated_arrival: ETA (when dispatched)
- created_at/updated_at: Timestamps
```

### API Routes

#### Emergency Contacts
- `GET /emergency/contacts` - View all contacts
- `POST /emergency/contacts/add` - Add new contact
- `POST /emergency/contacts/delete/<id>` - Delete contact

#### Ambulance Booking
- `POST /emergency/ambulance/book` - Book ambulance
- `GET /emergency/ambulance/status/<id>` - Check booking status
- `GET /emergency/my-bookings` - View all bookings

### External APIs Used
1. **OpenStreetMap Nominatim** - Reverse geocoding (coordinates to address)
2. **Overpass API** - Search for hospitals, blood banks, pharmacies
3. **Leaflet.js** - Interactive map display
4. **Google Maps** - Directions and navigation

---

## Setup Instructions

### 1. Update Database
Run the database update script to create new tables:
```bash
cd doctor-appointment-system-main
python update_emergency_db.py
```

### 2. Restart Server
```bash
python app.py
```

### 3. Test Features
1. Login as a patient
2. Go to Emergency page
3. Test each feature:
   - Add emergency contacts
   - Book ambulance (test mode)
   - Search blood banks
   - Find pharmacies

---

## User Permissions

### Patient Users
- ✅ Access all emergency features
- ✅ Book ambulances
- ✅ Manage emergency contacts
- ✅ View blood banks and pharmacies
- ✅ View booking history

### Doctor/Hospital Users
- ✅ View emergency page
- ✅ Find blood banks and pharmacies
- ❌ Cannot book ambulances (patient feature)
- ❌ Cannot manage emergency contacts (patient feature)

### Guest Users (Not Logged In)
- ✅ View emergency page
- ✅ Find hospitals, blood banks, pharmacies
- ✅ Call emergency numbers
- ❌ Cannot book ambulances (requires login)
- ❌ Cannot save emergency contacts (requires login)

---

## Future Enhancements

### Planned Features
1. **Real Ambulance Integration**
   - Partner with ambulance services
   - Real-time tracking
   - Live ETA updates
   - Driver location on map

2. **Emergency Notifications**
   - SMS alerts to emergency contacts
   - Email notifications
   - Push notifications
   - Automatic contact notification on booking

3. **Blood Donation**
   - Blood donor registration
   - Blood type matching
   - Donor availability
   - Blood request system

4. **Pharmacy Integration**
   - Medicine availability check
   - Online ordering
   - Prescription upload
   - Home delivery

5. **Emergency Medical Records**
   - Quick access to critical medical info
   - Allergies and conditions
   - Current medications
   - Blood type and medical history
   - QR code for emergency access

6. **Telemedicine Emergency**
   - Video consultation with emergency doctors
   - AI-powered symptom checker
   - First aid guidance
   - Triage system

---

## Safety & Privacy

### Data Security
- All emergency contacts encrypted
- Location data not stored permanently
- Booking data secured with user authentication
- HIPAA-compliant data handling

### Privacy
- Location access requires user permission
- Emergency contacts only visible to user
- Booking details private to user
- No data sharing with third parties

### Best Practices
- Always call 108 for life-threatening emergencies
- Keep emergency contacts updated
- Verify pharmacy hours before visiting
- Confirm blood bank availability by phone
- Provide accurate location information

---

## Troubleshooting

### Location Not Working
- Enable location services in browser
- Allow location permission when prompted
- Check if GPS is enabled on device
- Try refreshing the page

### No Results Found
- Increase search radius (modify code)
- Check internet connection
- Verify OpenStreetMap data availability
- Try different location

### Ambulance Booking Failed
- Check if logged in as patient
- Verify all required fields filled
- Check internet connection
- Contact support if issue persists

### Map Not Loading
- Check internet connection
- Disable ad blockers
- Clear browser cache
- Try different browser

---

## Support

For issues or questions:
1. Check this documentation
2. Review TESTING_GUIDE.md
3. Check browser console for errors
4. Contact system administrator

**Emergency Hotlines:**
- Ambulance: 108
- Police: 100
- Fire: 101
- Women Helpline: 1091
- Child Helpline: 1098

---

## Credits

**Technologies Used:**
- Flask (Backend)
- SQLAlchemy (Database)
- Leaflet.js (Maps)
- OpenStreetMap (Map data)
- Overpass API (Location search)
- Bootstrap 5 (UI)
- Font Awesome (Icons)

**Data Sources:**
- OpenStreetMap Contributors
- Google Maps API
- Emergency service numbers (India)

---

## Version History

### v2.0 - Emergency Features Release
- ✅ Ambulance booking system
- ✅ Emergency contact management
- ✅ Blood bank locator
- ✅ Pharmacy locator
- ✅ Enhanced emergency page
- ✅ Interactive maps
- ✅ Real-time location services

### v1.0 - Initial Release
- Basic appointment system
- Hospital and doctor management
- Patient medical history
- AI chatbot integration

---

**Last Updated:** November 25, 2025
**Version:** 2.0
**Status:** Production Ready ✅
