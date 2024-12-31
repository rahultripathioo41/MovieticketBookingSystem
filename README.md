# Movie Ticket Booking System

## Overview
This is a Python-based console application that allows users to book movie tickets, select theaters, choose show timings, and pay for their seats. The application is integrated with a MySQL database to manage data and provides separate login options for users and administrators.

---

## Features
1. **User Login**:
   - Allows users to book tickets by providing their name.
   - Options to select a movie, theater, show timing, and seating type.

2. **Admin Login**:
   - Admins can view the booking details, including user names, movies, theaters, timings, and seat categories.

3. **Movie Selection**:
   - Users can choose from multiple movies (e.g., Circus, Avatar: The Way of Water, Freddy).

4. **Theater Selection**:
   - Users can pick a theater (e.g., INOX(Z Square), PVR(South X), Carnival Cinemas(Rave Moti)).

5. **Show Timings**:
   - Available timings include:
     - 9:30 AM - 12:30 PM
     - 1:00 PM - 4:00 PM
     - 4:30 PM - 7:30 PM
     - 8:00 PM - 11:00 PM

6. **Seat Categories**:
   - Gold: INR 190
   - Platinum: INR 250
   - Recliner: INR 450

7. **Payment Options**:
   - Credit/Debit Card
   - PhonePe/GPay/Paytm
   - UPI ID

---

## Database Requirements
- **Database Name**: `admin`
- **Table Name**: `movie`
- **Table Schema**:
  ```sql
  CREATE TABLE movie (
      n INT PRIMARY KEY,
      Name VARCHAR(50),
      moviename VARCHAR(100),
      theatre VARCHAR(100),
      timing VARCHAR(50),
      seat VARCHAR(50)
  );
  ```

---

## Prerequisites
1. Python 3.x installed on your system.
2. MySQL Server installed and configured.
3. Required Python libraries:
   - `mysql.connector`

   Install it using:
   ```bash
   pip install mysql-connector-python
   ```

---

## How to Run
1. Clone this repository or download the project files.
2. Set up the MySQL database as per the schema mentioned above.
3. Update the database credentials in the Python script:
   ```python
   mycon = sqltor.connect(host="localhost", user="root", passwd="<your_password>", database="admin")
   ```
4. Execute the script:
   ```bash
   python finalproject.py
   ```
5. Follow the on-screen instructions to book tickets or log in as an admin.

---

## Program Flow
1. **Welcome Screen**: Users are greeted with the "Movie Ticket Booking System" welcome message.
2. **Login Options**:
   - **User Login**: Proceed to movie booking.
   - **Admin Login**: View booking details.
3. **Booking Steps**:
   - Enter name.
   - Select movie, theater, timing, and seat category.
   - Review booking details.
   - Complete payment.
4. **Admin Access**:
   - Log in with admin credentials to view all bookings.

---

## Admin Credentials
- **Username**: `Monu@123`
- **Password**: `sachin`

---

## Contributions
Feel free to fork the repository, raise issues, and submit pull requests. Suggestions and contributions are always welcome!

---

## Contact
For queries or feedback, reach out to [rahultripathioo41@gmail.com].

