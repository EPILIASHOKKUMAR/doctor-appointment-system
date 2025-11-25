# 🗺️ Emergency Map Markers Guide

## Map Legend

### Your Location
- **Symbol:** Red Circle (●)
- **Color:** Red (#e74a3b)
- **Description:** Shows your current GPS location
- **Appears:** Automatically when location permission granted

---

### Hospitals
- **Symbol:** Hospital Icon (🏥)
- **Color:** Red (#dc3545)
- **Shape:** Rounded square with white border
- **Search Radius:** 100km
- **Description:** All hospitals within 100km of your location
- **Features:**
  - Click marker to see hospital name and distance
  - Get directions via Google Maps
  - Shows total count found
  - Top 20 displayed in list

---

### Pharmacies
- **Symbol:** Plus Sign (+)
- **Color:** Green (#28a745)
- **Shape:** Circle with white border
- **Search Radius:** 100km
- **Description:** All pharmacies within 100km
- **Features:**
  - Click marker to see pharmacy name and distance
  - Shows opening hours
  - 24/7 pharmacies highlighted with badge
  - Get directions via Google Maps
  - Call pharmacy directly (if available)
  - Top 20 displayed in list

---

### Blood Banks
- **Symbol:** Droplet Icon (💧)
- **Color:** Red (#dc3545)
- **Shape:** Circle with white border
- **Search Radius:** 100km
- **Description:** Blood banks and donation centers
- **Features:**
  - Click marker to see blood bank name and distance
  - Get directions via Google Maps
  - Quick call to 108 for emergency
  - All found blood banks displayed in list

---

## How to Use the Map

### 1. Initial Load
1. Open Emergency page
2. Allow location permission when prompted
3. Map centers on your location
4. Your location marked with red circle

### 2. View Hospitals
- Red hospital icons appear automatically
- Shows all hospitals within 100km
- Alert shows total count (e.g., "Found 45 hospitals within 100km")
- Click any marker for details
- Click hospital card in list to zoom to that location

### 3. View Pharmacies
1. Click "Pharmacies" action card
2. Green plus markers added to map
3. Modal shows list of pharmacies
4. Look for "24/7" badge for round-the-clock service
5. Click marker or list item for details

### 4. View Blood Banks
1. Click "Blood Banks" action card
2. Red droplet markers added to map
3. Modal shows list of blood banks
4. Click marker or list item for details

---

## Map Controls

### Zoom
- **Zoom In:** Click + button or scroll up
- **Zoom Out:** Click - button or scroll down
- **Double Click:** Zoom in on specific area

### Pan
- Click and drag to move around the map
- Use arrow keys for precise movement

### Markers
- **Click:** Show popup with details
- **Hover:** Highlight marker
- **Popup:** Click "Get Directions" for navigation

---

## Search Radius Explained

### 100km Coverage
- **Why 100km?** Covers large metropolitan areas and surrounding regions
- **Hospital Count:** Typically 20-100 hospitals depending on area
- **Pharmacy Count:** Typically 50-200 pharmacies depending on area
- **Blood Bank Count:** Typically 5-20 blood banks depending on area

### Performance
- Map shows up to 50 markers of each type for performance
- List shows top 20 sorted by distance
- All facilities within 100km are counted

---

## Marker Details

### Hospital Marker
```
┌─────────────┐
│   🏥        │  Red background
│  Hospital   │  White border
│   Icon      │  35x35 pixels
└─────────────┘
```

**Popup Shows:**
- Hospital name
- Distance in km
- "Get Directions" button

### Pharmacy Marker
```
┌─────────────┐
│     +       │  Green background
│   Plus      │  White border
│   Symbol    │  32x32 pixels
└─────────────┘
```

**Popup Shows:**
- Pharmacy name
- Distance in km
- Opening hours
- "Get Directions" button

### Blood Bank Marker
```
┌─────────────┐
│     💧      │  Red background
│  Droplet    │  White border
│   Icon      │  32x32 pixels
└─────────────┘
```

**Popup Shows:**
- Blood bank name
- Distance in km
- "Get Directions" button

---

## Distance Calculation

### How It Works
- Uses Haversine formula
- Calculates straight-line distance
- Displayed in kilometers (km)
- Accurate to within 1%

### Distance Badges
- **< 5km:** Very close (walk/bike)
- **5-20km:** Close (short drive)
- **20-50km:** Moderate distance
- **50-100km:** Far (longer drive)

---

## Map Legend (Bottom Right)

The map includes a permanent legend showing:
- 🔴 Your Location
- 🏥 Hospitals (Red)
- ➕ Pharmacies (Green)
- 💧 Blood Banks (Red)

**Location:** Bottom right corner of map
**Always Visible:** Yes
**Background:** White with shadow

---

## Tips for Best Results

### Location Accuracy
1. Enable GPS on your device
2. Allow browser location permission
3. Use outdoors for better signal
4. Refresh if location seems wrong

### Finding Facilities
1. **Nearest First:** List sorted by distance
2. **24/7 Pharmacies:** Look for green badge
3. **Multiple Options:** Compare distances
4. **Directions:** Use Google Maps for real-time traffic

### Emergency Situations
1. **Call First:** Always call 108 for emergencies
2. **Nearest Hospital:** Check top of list
3. **Traffic:** Consider current traffic conditions
4. **Backup Options:** Note 2-3 nearest facilities

---

## Troubleshooting

### Map Not Loading
- Check internet connection
- Disable ad blockers
- Clear browser cache
- Try different browser

### No Markers Showing
- Verify location permission granted
- Check if in covered area
- Wait for search to complete
- Refresh page

### Wrong Location
- Enable device GPS
- Move outdoors
- Refresh page
- Manually enter address

### Too Many/Few Results
- **Too Many:** Use list to find nearest
- **Too Few:** Increase search radius (code change)
- **None Found:** Check OpenStreetMap coverage

---

## Data Sources

### OpenStreetMap (OSM)
- Community-maintained map data
- Updated regularly by volunteers
- Global coverage
- Free and open source

### Search Queries
- **Hospitals:** `amenity=hospital`
- **Pharmacies:** `amenity=pharmacy`
- **Blood Banks:** `amenity=blood_bank` OR `healthcare=blood_donation`

### Data Accuracy
- Depends on OSM contributors
- Urban areas: Very accurate
- Rural areas: May be incomplete
- Report missing facilities to OSM

---

## Technical Details

### Map Library
- **Leaflet.js** - Open-source JavaScript library
- **Tile Provider:** OpenStreetMap
- **Geocoding:** Nominatim API
- **Search:** Overpass API

### Marker Icons
- **Font Awesome** icons
- **Custom CSS** styling
- **Responsive** sizing
- **Accessible** colors

### Performance
- **Lazy Loading:** Markers load as needed
- **Clustering:** Prevents overlap (future)
- **Caching:** Reduces API calls
- **Optimization:** Limits displayed markers

---

## Accessibility

### Color Blind Friendly
- Red and green clearly distinguishable
- Icons supplement colors
- Text labels provided
- High contrast design

### Screen Readers
- Alt text for markers
- Descriptive labels
- Keyboard navigation
- ARIA labels

---

## Future Enhancements

### Planned Features
1. **Marker Clustering** - Group nearby markers
2. **Filter Options** - Show/hide marker types
3. **Custom Radius** - User-adjustable search distance
4. **Route Planning** - Multi-stop directions
5. **Real-time Updates** - Live facility status
6. **Offline Maps** - Work without internet
7. **Save Favorites** - Bookmark facilities
8. **Share Location** - Send to emergency contacts

---

## Quick Reference

| Marker Type | Color | Symbol | Radius | Count |
|------------|-------|--------|--------|-------|
| Your Location | Red | ● | - | 1 |
| Hospitals | Red | 🏥 | 100km | Up to 50 |
| Pharmacies | Green | + | 100km | Up to 50 |
| Blood Banks | Red | 💧 | 100km | All |

---

## Support

**Need Help?**
- Check EMERGENCY_FEATURES.md for detailed docs
- Review EMERGENCY_TESTING_GUIDE.md for testing
- Contact system administrator
- Report issues on GitHub

**Emergency Hotlines:**
- Ambulance: 108
- Police: 100
- Fire: 101

---

**Last Updated:** November 25, 2025
**Version:** 2.0
**Status:** Production Ready ✅
