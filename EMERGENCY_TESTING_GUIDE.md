# 🚑 Emergency Features Testing Guide

## Quick Start Testing

### Prerequisites
✅ Server running on http://127.0.0.1:5000
✅ Database updated with new tables
✅ Browser with location services enabled

---

## Test Scenarios

### 1. Emergency Page Access (No Login Required)

**Test Steps:**
1. Open http://127.0.0.1:5000
2. Click "Emergency" in navbar
3. Allow location access when prompted

**Expected Results:**
- ✅ Emergency page loads with 4 action cards
- ✅ Map displays your location (red marker)
- ✅ Emergency numbers visible (108, 100, 101)
- ✅ Nearby hospitals appear on map
- ✅ SmartClinic hospitals listed on right side

**Action Cards Visible:**
- 🚑 Book Ambulance
- 🩸 Blood Banks
- 💊 Pharmacies
- 👨‍👩‍👧‍👦 Emergency Contacts

---

### 2. Blood Bank Locator (No Login Required)

**Test Steps:**
1. On Emergency page, click "Blood Banks" card
2. Wait for search to complete

**Expected Results:**
- ✅ Modal opens with "Nearby Blood Banks" title
- ✅ List of blood banks with distances
- ✅ "Get Directions" button for each bank
- ✅ "Call 108" button available
- ✅ If no banks found, shows helpful message

**Test Actions:**
- Click "Get Directions" → Opens Google Maps
- Click "Call 108" → Opens phone dialer

---

### 3. Pharmacy Locator (No Login Required)

**Test Steps:**
1. On Emergency page, click "Pharmacies" card
2. Wait for search to complete

**Expected Results:**
- ✅ Modal opens with "Nearby Pharmacies" title
- ✅ List of pharmacies sorted by distance
- ✅ 24/7 pharmacies have green badge
- ✅ Opening hours displayed
- ✅ "Get Directions" button for each
- ✅ "Call" button if phone available

**Test Actions:**
- Look for "24/7" badges
- Check opening hours display
- Click "Get Directions" → Opens Google Maps
- Click "Call" → Opens phone dialer

---

### 4. Emergency Contacts Management (Login Required)

**Test Steps:**
1. Login as patient:
   - Email: patient@test.com
   - Password: patient123
2. Go to Patient Dashboard
3. Click "Emergency Contacts" card (blue)

**Expected Results:**
- ✅ Emergency Contacts page loads
- ✅ "Add Contact" button visible
- ✅ Empty state message if no contacts

**Add Contact Test:**
1. Click "Add Contact" button
2. Fill in form:
   - Name: "John Doe"
   - Relationship: "Spouse"
   - Phone: "9876543210"
   - Email: "john@example.com"
   - Check "Set as primary contact"
3. Click "Save Contact"

**Expected Results:**
- ✅ Success message appears
- ✅ Contact appears in list
- ✅ "Primary" badge visible
- ✅ Phone and email are clickable links
- ✅ Delete button available

**Delete Contact Test:**
1. Click delete button (trash icon)
2. Confirm deletion

**Expected Results:**
- ✅ Confirmation dialog appears
- ✅ Contact removed from list
- ✅ Success message shown

---

### 5. Ambulance Booking (Login Required)

**Test Steps:**
1. Login as patient (if not already)
2. Go to Emergency page
3. Click "Book Ambulance" card

**Expected Results:**
- ✅ Modal opens with booking form
- ✅ All fields visible and functional

**Fill Booking Form:**
1. Patient Name: "Test Patient"
2. Contact Phone: "9876543210"
3. Click "Use Current Location" button
   - ✅ Address auto-fills
   - ✅ Coordinates captured
4. Destination Hospital: "City Hospital"
5. Emergency Type: Select "Accident"
6. Patient Condition: "Minor injury, conscious"
7. Click "Request Ambulance"

**Expected Results:**
- ✅ Success message appears
- ✅ Modal closes
- ✅ Booking saved to database

**View Bookings:**
1. Go to Patient Dashboard
2. Look for ambulance bookings link (if added)
   OR
3. Navigate to: http://127.0.0.1:5000/emergency/my-bookings

**Expected Results:**
- ✅ Booking appears in list
- ✅ Status shows "Requested"
- ✅ "View" button available
- ✅ Click "View" shows full details

---

### 6. Patient Dashboard Integration

**Test Steps:**
1. Login as patient
2. Go to Patient Dashboard

**Expected Results:**
- ✅ 4 stat cards visible:
  - Upcoming Appointments
  - Completed Appointments
  - Emergency Contacts (blue, clickable)
  - Emergency Services (red, clickable)
- ✅ Click Emergency Contacts → Goes to contacts page
- ✅ Click Emergency Services → Goes to emergency page

---

### 7. Map Interactions

**Test Steps:**
1. Go to Emergency page
2. Wait for map to load with hospitals

**Test Actions:**
1. Click on hospital marker (numbered blue circle)
   - ✅ Popup shows hospital name
   - ✅ Distance displayed
   - ✅ "Get Directions" button works

2. Click on your location marker (red dot)
   - ✅ Popup shows "Your Location"

3. Zoom in/out on map
   - ✅ Map responds smoothly

4. Pan around map
   - ✅ Map moves smoothly

---

### 8. Mobile Responsiveness

**Test Steps:**
1. Open browser DevTools (F12)
2. Toggle device toolbar (Ctrl+Shift+M)
3. Select mobile device (iPhone, Android)
4. Navigate through emergency features

**Expected Results:**
- ✅ Emergency page responsive
- ✅ Action cards stack vertically
- ✅ Map adjusts to screen size
- ✅ Modals fit mobile screen
- ✅ Buttons easily tappable
- ✅ Forms usable on mobile

---

### 9. Error Handling

**Test Location Denied:**
1. Go to Emergency page
2. Deny location permission

**Expected Results:**
- ✅ Warning message appears
- ✅ Map still loads (default view)
- ✅ Features still accessible
- ✅ Helpful message to enable location

**Test No Internet:**
1. Disconnect internet
2. Try to search blood banks/pharmacies

**Expected Results:**
- ✅ Error message appears
- ✅ Suggests calling 108
- ✅ No app crash

**Test Invalid Form:**
1. Try to book ambulance
2. Leave required fields empty
3. Click submit

**Expected Results:**
- ✅ Form validation triggers
- ✅ Required fields highlighted
- ✅ Helpful error messages

---

### 10. Cross-Browser Testing

**Test Browsers:**
- ✅ Chrome
- ✅ Firefox
- ✅ Edge
- ✅ Safari (if available)

**Test Each:**
1. Emergency page loads
2. Map displays correctly
3. Modals open/close
4. Forms submit successfully
5. Location services work

---

## Performance Testing

### Load Time
- Emergency page should load < 3 seconds
- Map should render < 2 seconds
- Hospital search should complete < 5 seconds

### API Calls
- Overpass API responses < 10 seconds
- Nominatim geocoding < 3 seconds
- Multiple simultaneous searches work

---

## Security Testing

### Authentication
1. Try to access emergency contacts without login
   - ✅ Redirects to login
2. Try to book ambulance without login
   - ✅ Shows login prompt
3. Try to access another user's contacts
   - ✅ Unauthorized error

### Data Validation
1. Try SQL injection in forms
   - ✅ Properly escaped
2. Try XSS in text fields
   - ✅ Properly sanitized
3. Try invalid coordinates
   - ✅ Handled gracefully

---

## Integration Testing

### Database
1. Add emergency contact
   - ✅ Saved to database
2. Book ambulance
   - ✅ Saved to database
3. Delete contact
   - ✅ Removed from database
4. Check data persistence
   - ✅ Data survives server restart

### External APIs
1. OpenStreetMap
   - ✅ Hospital search works
   - ✅ Blood bank search works
   - ✅ Pharmacy search works
2. Google Maps
   - ✅ Directions links work
3. Phone Links
   - ✅ tel: links work on mobile

---

## User Acceptance Testing

### Patient User Stories

**Story 1: Emergency Situation**
"As a patient in an emergency, I want to quickly find nearby hospitals so I can get immediate help."
- ✅ Emergency page accessible from navbar
- ✅ Map shows nearby hospitals
- ✅ Distances calculated
- ✅ Directions available

**Story 2: Ambulance Needed**
"As a patient, I want to book an ambulance for a medical emergency."
- ✅ Ambulance booking form easy to use
- ✅ Current location auto-detected
- ✅ Booking confirmation received
- ✅ Can view booking status

**Story 3: Emergency Contacts**
"As a patient, I want to save emergency contacts so medical staff can reach my family."
- ✅ Can add multiple contacts
- ✅ Can set primary contact
- ✅ Can edit/delete contacts
- ✅ Contacts easily accessible

**Story 4: Find Pharmacy**
"As a patient, I need to find a 24/7 pharmacy for urgent medication."
- ✅ Pharmacy search shows nearby options
- ✅ 24/7 pharmacies clearly marked
- ✅ Opening hours displayed
- ✅ Can get directions

**Story 5: Blood Emergency**
"As a patient, I need to find a blood bank urgently."
- ✅ Blood bank search works
- ✅ Shows nearest options
- ✅ Can call emergency services
- ✅ Can get directions

---

## Regression Testing

After any code changes, verify:
- ✅ Existing appointment system still works
- ✅ Patient dashboard loads correctly
- ✅ Doctor dashboard unaffected
- ✅ Hospital dashboard unaffected
- ✅ Medical history still accessible
- ✅ AI chatbot still works
- ✅ Login/logout functional
- ✅ Registration works

---

## Known Limitations

1. **Ambulance Booking**
   - Currently stores requests only
   - No real ambulance service integration
   - Status updates manual
   - For real emergencies, call 108

2. **Location Services**
   - Requires browser permission
   - May be inaccurate indoors
   - Depends on device GPS

3. **External Data**
   - OpenStreetMap data may be incomplete
   - Some areas have limited coverage
   - Data updated by community

4. **Offline Mode**
   - Requires internet connection
   - Map won't load offline
   - Emergency numbers still work

---

## Troubleshooting Common Issues

### Map Not Loading
```
Solution:
1. Check internet connection
2. Disable ad blockers
3. Clear browser cache
4. Try incognito mode
```

### Location Not Working
```
Solution:
1. Enable location in browser settings
2. Allow location permission
3. Check device GPS enabled
4. Try refreshing page
```

### No Results Found
```
Solution:
1. Check if in covered area
2. Increase search radius (code change)
3. Try different location
4. Check OpenStreetMap coverage
```

### Form Not Submitting
```
Solution:
1. Check all required fields filled
2. Verify logged in (if required)
3. Check browser console for errors
4. Try different browser
```

---

## Test Checklist

### Before Release
- [ ] All features tested manually
- [ ] Database migrations successful
- [ ] No console errors
- [ ] Mobile responsive
- [ ] Cross-browser compatible
- [ ] Security tested
- [ ] Performance acceptable
- [ ] Documentation complete
- [ ] User guide created
- [ ] Admin notified

### After Release
- [ ] Monitor error logs
- [ ] Check user feedback
- [ ] Verify API usage
- [ ] Monitor performance
- [ ] Track feature usage
- [ ] Plan improvements

---

## Success Metrics

### Feature Adoption
- Number of emergency contacts added
- Ambulance bookings per week
- Blood bank searches
- Pharmacy searches
- Emergency page visits

### User Satisfaction
- Feature usage rate
- User feedback
- Error rate
- Response time
- Completion rate

---

## Support & Feedback

**Report Issues:**
- Check console for errors
- Note browser and OS version
- Describe steps to reproduce
- Include screenshots if possible

**Feature Requests:**
- Describe use case
- Explain expected behavior
- Suggest implementation

---

**Testing Completed:** ___________
**Tested By:** ___________
**Issues Found:** ___________
**Status:** ___________

---

**Last Updated:** November 25, 2025
**Version:** 2.0
**Status:** Ready for Testing ✅
