"""
Export data from local database to SQL file for production import
"""
import pymysql
import json
from datetime import datetime

# Database connection
host = 'localhost'
user = 'root'
password = 'Ashok@11042005'
database = 'clinic_db'

try:
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    
    cursor = connection.cursor()
    
    # Export hospitals
    print("Exporting hospitals...")
    cursor.execute("SELECT * FROM hospital")
    hospitals = cursor.fetchall()
    
    cursor.execute("DESCRIBE hospital")
    hospital_columns = [col[0] for col in cursor.fetchall()]
    
    # Export doctors
    print("Exporting doctors...")
    cursor.execute("SELECT * FROM doctor")
    doctors = cursor.fetchall()
    
    cursor.execute("DESCRIBE doctor")
    doctor_columns = [col[0] for col in cursor.fetchall()]
    
    # Export users
    print("Exporting users...")
    cursor.execute("SELECT * FROM user")
    users = cursor.fetchall()
    
    cursor.execute("DESCRIBE user")
    user_columns = [col[0] for col in cursor.fetchall()]
    
    # Create SQL insert statements
    with open('production_data.sql', 'w', encoding='utf-8') as f:
        f.write("-- Production Data Export\n")
        f.write(f"-- Generated: {datetime.now()}\n\n")
        
        # Hospitals
        f.write("-- Hospitals\n")
        for hospital in hospitals:
            values = []
            for i, val in enumerate(hospital):
                if val is None:
                    values.append('NULL')
                elif isinstance(val, str):
                    values.append(f"'{val.replace(chr(39), chr(39)+chr(39))}'")
                else:
                    values.append(str(val))
            
            f.write(f"INSERT INTO hospital ({', '.join(hospital_columns)}) VALUES ({', '.join(values)});\n")
        
        f.write("\n-- Doctors\n")
        for doctor in doctors:
            values = []
            for i, val in enumerate(doctor):
                if val is None:
                    values.append('NULL')
                elif isinstance(val, str):
                    values.append(f"'{val.replace(chr(39), chr(39)+chr(39))}'")
                else:
                    values.append(str(val))
            
            f.write(f"INSERT INTO doctor ({', '.join(doctor_columns)}) VALUES ({', '.join(values)});\n")
        
        f.write("\n-- Users\n")
        for user in users:
            values = []
            for i, val in enumerate(user):
                if val is None:
                    values.append('NULL')
                elif isinstance(val, str):
                    values.append(f"'{val.replace(chr(39), chr(39)+chr(39))}'")
                else:
                    values.append(str(val))
            
            f.write(f"INSERT INTO user ({', '.join(user_columns)}) VALUES ({', '.join(values)});\n")
    
    print(f"\n✓ Exported {len(hospitals)} hospitals")
    print(f"✓ Exported {len(doctors)} doctors")
    print(f"✓ Exported {len(users)} users")
    print(f"\n✓ Data exported to: production_data.sql")
    
    cursor.close()
    connection.close()
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
