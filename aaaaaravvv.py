import mysql.connector as sqltor

mycon = sqltor.connect(host="localhost", user="root", passwd="aarav", database="aarav")
if mycon.is_connected():
    print("Successfully connected to MySQL database")

cursor = mycon.cursor()

# Create main hospital table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS hospital(
    serial_no INT(5) NOT NULL PRIMARY KEY,
    patient_name VARCHAR(20),
    Patient_room INT(5) NOT NULL,
    cause VARCHAR(20) NOT NULL,
    bill INT(10) NOT NULL,
    docter_incharge VARCHAR(20) NOT NULL,
    date_of_entry VARCHAR(20) NOT NULL,
    date_of_discharge VARCHAR(20) NOT NULL)
""")

# Create specialist doctors table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS specialist_doctors(
    doc_id INT AUTO_INCREMENT PRIMARY KEY,
    doctor_name VARCHAR(50) NOT NULL,
    specialization VARCHAR(50) NOT NULL,
    experience_years INT(2),
    phone VARCHAR(15))
""")

mycon.commit()

while True:  # loop and option
    print("\n" + "="*50)
    print("       HOSPITAL MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Insert Patient Records")
    print("2. Delete Patient Records")
    print("3. Update Patient Records")
    print("4. Display Patient Records")
    print("5. Manage Specialist Doctors")
    print("6. Exit")
    print("="*50)
    ch = int(input("ENTER THE OPTION: "))

    # ---------------- INSERT PATIENT ----------------
    if ch == 1:
        serial_no = int(input("Enter the serial no: "))
        patient_name = input("Enter the patient name: ")
        Patient_Room = int(input("Enter Patient_room: "))
        cause = input("Enter the cause: ")
        bill = int(input("Enter the amount: "))
        docter_incharge = input("Enter the doctor incharge: ")
        date_of_entry = input("Enter the entry date: ")
        date_of_discharge = input("Enter the discharge date: ")

        sql = """INSERT INTO hospital(serial_no,patient_name,Patient_room,cause,bill,
                 docter_incharge,date_of_entry,date_of_discharge)
                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = (serial_no, patient_name, Patient_Room, cause, bill,
                  docter_incharge, date_of_entry, date_of_discharge)
        cursor.execute(sql, values)
        mycon.commit()
        print("✓ Patient record inserted successfully!")

    # ---------------- DELETE PATIENT ----------------
    elif ch == 2:
        dele = int(input("ENTER THE SERIAL NO WHICH YOU WANT TO DELETE: "))
        cursor.execute("DELETE FROM hospital WHERE serial_no = %s", (dele,))
        mycon.commit()
        print("✓ Record deleted successfully!")

    # ---------------- UPDATE PATIENT ----------------
    elif ch == 3:
        while True:
            print("\n--- UPDATE MENU ---")
            print("1. UPDATE SERIAL NO")
            print("2. UPDATE PATIENT NAME")
            print("3. UPDATE PATIENT ROOM")
            print("4. UPDATE CAUSE")
            print("5. UPDATE DOCTOR INCHARGE")
            print("6. UPDATE DATE OF ENTRY")
            print("7. UPDATE DATE OF DISCHARGE")
            print("8. EXIT UPDATE MENU")

            r = int(input("ENTER THE OPTION: "))

            # -------- SERIAL NO --------
            if r == 1:
                old_serial = int(input("Enter OLD serial number: "))
                cursor.execute("SELECT * FROM hospital WHERE serial_no = %s", (old_serial,))
                record = cursor.fetchone()
                if not record:
                    print("No record found!")
                    continue

                new_serial = int(input("Enter NEW serial number: "))
                cursor.execute("SELECT * FROM hospital WHERE serial_no = %s", (new_serial,))
                if cursor.fetchone():
                    print("Serial number already exists!")
                    continue

                confirm = input(f"Confirm update {old_serial} → {new_serial}? (y/n): ")
                if confirm.lower() == "y":
                    cursor.execute("UPDATE hospital SET serial_no = %s WHERE serial_no = %s",
                                   (new_serial, old_serial))
                    mycon.commit()
                    print("✓ Serial number updated!")

            # -------- PATIENT NAME --------
            elif r == 2:
                serial_no = int(input("Enter patient SERIAL NO: "))
                cursor.execute("SELECT * FROM hospital WHERE serial_no = %s", (serial_no,))
                record = cursor.fetchone()
                if not record:
                    print("No record found!")
                    continue

                new_name = input("Enter NEW patient name: ")
                confirm = input(f"Confirm update {record[1]} → {new_name}? (y/n): ")
                if confirm.lower() == "y":
                    cursor.execute("UPDATE hospital SET patient_name = %s WHERE serial_no = %s",
                                   (new_name, serial_no))
                    mycon.commit()
                    print("✓ Patient name updated!")

            # -------- PATIENT ROOM --------
            elif r == 3:
                serial_no = int(input("Enter patient SERIAL NO: "))
                cursor.execute("SELECT * FROM hospital WHERE serial_no = %s", (serial_no,))
                record = cursor.fetchone()
                if not record:
                    print("No record found!")
                    continue

                new_room = int(input("Enter NEW patient room: "))
                confirm = input(f"Confirm update {record[2]} → {new_room}? (y/n): ")
                if confirm.lower() == "y":
                    cursor.execute("UPDATE hospital SET Patient_room = %s WHERE serial_no = %s",
                                   (new_room, serial_no))
                    mycon.commit()
                    print("✓ Patient room updated!")

            # -------- CAUSE --------
            elif r == 4:
                serial_no = int(input("Enter patient SERIAL NO: "))
                cursor.execute("SELECT * FROM hospital WHERE serial_no = %s", (serial_no,))
                record = cursor.fetchone()
                if not record:
                    print("No record found!")
                    continue

                new_cause = input("Enter NEW cause: ")
                confirm = input(f"Confirm update {record[3]} → {new_cause}? (y/n): ")
                if confirm.lower() == "y":
                    cursor.execute("UPDATE hospital SET cause = %s WHERE serial_no = %s",
                                   (new_cause, serial_no))
                    mycon.commit()
                    print("✓ Cause updated!")

            # -------- DOCTOR INCHARGE --------
            elif r == 5:
                serial_no = int(input("Enter patient SERIAL NO: "))
                cursor.execute("SELECT * FROM hospital WHERE serial_no = %s", (serial_no,))
                record = cursor.fetchone()
                if not record:
                    print("No record found!")
                    continue

                new_doc = input("Enter NEW doctor incharge: ")
                confirm = input(f"Confirm update {record[5]} → {new_doc}? (y/n): ")
                if confirm.lower() == "y":
                    cursor.execute("UPDATE hospital SET docter_incharge = %s WHERE serial_no = %s",
                                   (new_doc, serial_no))
                    mycon.commit()
                    print("✓ Doctor incharge updated!")

            # -------- DATE OF ENTRY --------
            elif r == 6:
                serial_no = int(input("Enter patient SERIAL NO: "))
                cursor.execute("SELECT * FROM hospital WHERE serial_no = %s", (serial_no,))
                record = cursor.fetchone()
                if not record:
                    print("No record found!")
                    continue

                new_entry = input("Enter NEW date of entry: ")
                confirm = input(f"Confirm update {record[6]} → {new_entry}? (y/n): ")
                if confirm.lower() == "y":
                    cursor.execute("UPDATE hospital SET date_of_entry = %s WHERE serial_no = %s",
                                   (new_entry, serial_no))
                    mycon.commit()
                    print("✓ Date of entry updated!")

            # -------- DATE OF DISCHARGE --------
            elif r == 7:
                serial_no = int(input("Enter patient SERIAL NO: "))
                cursor.execute("SELECT * FROM hospital WHERE serial_no = %s", (serial_no,))
                record = cursor.fetchone()
                if not record:
                    print("No record found!")
                    continue

                new_discharge = input("Enter NEW date of discharge: ")
                confirm = input(f"Confirm update {record[7]} → {new_discharge}? (y/n): ")
                if confirm.lower() == "y":
                    cursor.execute("UPDATE hospital SET date_of_discharge = %s WHERE serial_no = %s",
                                   (new_discharge, serial_no))
                    mycon.commit()
                    print("✓ Date of discharge updated!")

            elif r == 8:
                print("Exiting update menu...")
                break

    # ---------------- DISPLAY PATIENT RECORDS ----------------
    elif ch == 4:
        cursor.execute("SELECT * FROM hospital")
        data = cursor.fetchall()
        print("\n" + "="*80)
        print("                        HOSPITAL RECORDS")
        print("="*80)
        if not data:
            print("No patient records found.")
        else:
            print(f"{'Serial':<8} {'Name':<15} {'Room':<6} {'Cause':<15} {'Bill':<10} {'Doctor':<15} {'Entry':<12} {'Discharge':<12}")
            print("-"*80)
            for row in data:
                print(f"{row[0]:<8} {row[1]:<15} {row[2]:<6} {row[3]:<15} {row[4]:<10} {row[5]:<15} {row[6]:<12} {row[7]:<12}")
        print("="*80)

    # ---------------- SPECIALIST DOCTORS SUBMENU ----------------
    elif ch == 5:
        while True:
            print("\n" + "="*50)
            print("     SPECIALIST DOCTORS MANAGEMENT")
            print("="*50)
            print("1. View All Specialist Doctors")
            print("2. Add New Specialist Doctor")
            print("3. Update Specialist Doctor")
            print("4. Delete Specialist Doctor")
            print("5. Back to Main Menu")
            print("="*50)

            sub_ch = int(input("Enter your choice: "))

            # -------- VIEW SPECIALIST DOCTORS --------
            if sub_ch == 1:
                cursor.execute("SELECT * FROM specialist_doctors ORDER BY doc_id")
                doctors = cursor.fetchall()
                print("\n" + "="*70)
                print("               SPECIALIST DOCTORS LIST")
                print("="*70)
                if not doctors:
                    print("No specialist doctors found in the database.")
                else:
                    print(f"{'ID':<5} {'Name':<20} {'Specialization':<20} {'Exp(yrs)':<10} {'Phone':<15}")
                    print("-"*70)
                    for doc in doctors:
                        print(f"{doc[0]:<5} {doc[1]:<20} {doc[2]:<20} {doc[3]:<10} {doc[4]:<15}")
                print("="*70)

            # -------- ADD SPECIALIST DOCTOR --------
            elif sub_ch == 2:
                print("\n--- Add New Specialist Doctor ---")
                doc_name = input("Enter doctor name: ")
                specialization = input("Enter specialization (e.g., Cardiologist, Neurologist): ")
                experience = int(input("Enter years of experience: "))
                phone = input("Enter phone number: ")

                sql = """INSERT INTO specialist_doctors(doctor_name, specialization, experience_years, phone)
                         VALUES (%s, %s, %s, %s)"""
                values = (doc_name, specialization, experience, phone)
                
                try:
                    cursor.execute(sql, values)
                    mycon.commit()
                    print(f"✓ Doctor {doc_name} added successfully!")
                except Exception as e:
                    print(f"Error adding doctor: {e}")

            # -------- UPDATE SPECIALIST DOCTOR --------
            elif sub_ch == 3:
                # First show all doctors
                cursor.execute("SELECT * FROM specialist_doctors ORDER BY doc_id")
                doctors = cursor.fetchall()
                if not doctors:
                    print("No specialist doctors found to update.")
                    continue

                print("\n--- Current Specialist Doctors ---")
                for doc in doctors:
                    print(f"ID: {doc[0]} | Name: {doc[1]} | Specialization: {doc[2]} | Exp: {doc[3]} yrs | Phone: {doc[4]}")

                doc_id = int(input("\nEnter Doctor ID to update: "))
                
                # Check if doctor exists
                cursor.execute("SELECT * FROM specialist_doctors WHERE doc_id = %s", (doc_id,))
                doctor = cursor.fetchone()
                
                if not doctor:
                    print("Doctor not found!")
                    continue

                print(f"\nCurrent Details: {doctor[1]} | {doctor[2]} | {doctor[3]} yrs | {doctor[4]}")
                print("\n--- What would you like to update? ---")
                print("1. Doctor Name")
                print("2. Specialization")
                print("3. Experience Years")
                print("4. Phone Number")
                print("5. Update All Fields")
                print("6. Cancel Update")

                update_choice = int(input("Enter your choice: "))

                if update_choice == 1:
                    new_name = input("Enter new doctor name: ")
                    cursor.execute("UPDATE specialist_doctors SET doctor_name = %s WHERE doc_id = %s",
                                   (new_name, doc_id))
                    mycon.commit()
                    print("✓ Doctor name updated!")

                elif update_choice == 2:
                    new_spec = input("Enter new specialization: ")
                    cursor.execute("UPDATE specialist_doctors SET specialization = %s WHERE doc_id = %s",
                                   (new_spec, doc_id))
                    mycon.commit()
                    print("✓ Specialization updated!")

                elif update_choice == 3:
                    new_exp = int(input("Enter new experience years: "))
                    cursor.execute("UPDATE specialist_doctors SET experience_years = %s WHERE doc_id = %s",
                                   (new_exp, doc_id))
                    mycon.commit()
                    print("✓ Experience updated!")

                elif update_choice == 4:
                    new_phone = input("Enter new phone number: ")
                    cursor.execute("UPDATE specialist_doctors SET phone = %s WHERE doc_id = %s",
                                   (new_phone, doc_id))
                    mycon.commit()
                    print("✓ Phone number updated!")

                elif update_choice == 5:
                    new_name = input("Enter new doctor name: ")
                    new_spec = input("Enter new specialization: ")
                    new_exp = int(input("Enter new experience years: "))
                    new_phone = input("Enter new phone number: ")
                    
                    sql = """UPDATE specialist_doctors 
                             SET doctor_name = %s, specialization = %s, experience_years = %s, phone = %s 
                             WHERE doc_id = %s"""
                    cursor.execute(sql, (new_name, new_spec, new_exp, new_phone, doc_id))
                    mycon.commit()
                    print("✓ All fields updated successfully!")

                elif update_choice == 6:
                    print("Update cancelled.")

            # -------- DELETE SPECIALIST DOCTOR --------
            elif sub_ch == 4:
                # Show all doctors first
                cursor.execute("SELECT * FROM specialist_doctors ORDER BY doc_id")
                doctors = cursor.fetchall()
                if not doctors:
                    print("No specialist doctors found to delete.")
                    continue

                print("\n--- Current Specialist Doctors ---")
                for doc in doctors:
                    print(f"ID: {doc[0]} | Name: {doc[1]} | Specialization: {doc[2]}")

                doc_id = int(input("\nEnter Doctor ID to delete: "))
                
                # Check if doctor exists
                cursor.execute("SELECT * FROM specialist_doctors WHERE doc_id = %s", (doc_id,))
                doctor = cursor.fetchone()
                
                if not doctor:
                    print("Doctor not found!")
                    continue

                confirm = input(f"Are you sure you want to delete Dr. {doctor[1]}? (y/n): ")
                if confirm.lower() == 'y':
                    cursor.execute("DELETE FROM specialist_doctors WHERE doc_id = %s", (doc_id,))
                    mycon.commit()
                    print("✓ Doctor deleted successfully!")
                else:
                    print("Deletion cancelled.")

            # -------- BACK TO MAIN MENU --------
            elif sub_ch == 5:
                print("Returning to main menu...")
                break
            
            else:
                print("Invalid choice! Please try again.")

    # ---------------- EXIT ----------------
    elif ch == 6:
        print("\n" + "="*50)
        print("  Thank you for using Hospital Management System!")
        print("="*50)
        cursor.close()
        mycon.close()
        break

    else:
        print("Invalid option! Please choose between 1-6.")
