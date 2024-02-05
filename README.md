#   GYM MANAGEMENT SYSTEM WITH SMS SUPPORT

pyinstaller gym.py --add-data "./test_images;test_images" --add-data "./employee_qrcodes;employee_qrcodes" --add-data "./frame_2_icons;frame_2_icons" --add-data "./frame_3_icons;frame_3_icons" --add-data "./frame_4_icons;frame_4_icons" --add-data "./frame_5_icons;frame_5_icons" --add-data "./frame_6_icons;frame_6_icons" --add-data "./frame_7_icons;frame_7_icons" --add-data "./member_qrcodes;member_qrcodes" --add-data "./trainer_qrcodes;trainer_qrcodes" --add-data "./enquiry_qrcodes;enquiry_qrcodes"  --add-data "./member_photo;member_photo"

The Awrim Gym Management System with SMS support is a desktop application aim to enhance the fitness center's communication efficiency, 
streamline operations, and improve gym member management. The system includes a QR code for  member and employee attendance. With the use of SMS, 
this creative system may provide timely attendance notifications, automate duties, and communicate with gym members via SMS, reminders for gym membership 
plans,and analytics. Reduced operating costs, better communication, more satisfaction among members, improved security of information. 

1. Attendance Management with SMS Support
2. Account Management
3. Membership Management with renewal(1-month only)
4. Employee Management
5. Trainer Management
6. Equipment Inventory
7. Payment Monitoring(Dashboard)
8. Integrate QR code attendance with SMS support

# Requirements For Installation
- Pip install -r Requirements.txt
# IDE
- Pycharm professional(Updated version) or VS Code (setup venv)
# Language used
- Python 3.11
# Library
- Tkinter/Customtkinter https://customtkinter.tomschimansky.com/
# Database
- SQLite 3
# SMS API
- Semaphore (Subscribe to semaphore to get the API key)
# Login
- Username: Admin#11
- Password: Admin#11

  Note:
  - Every Account Registered has only 1 role.
  - When reseting username and password, a philippine number is required(e.g: 091234567890 11-digit)
  - Semaphore API key is required for sending sms.
  - Only the registered account's contact number will only recieve the OTP for resetting the username and password.
  - username and password must be mixed with uppercase and lowercase, numbers and symbols.
  - The renewal of membership is set to 1-month.
  - When the end_date is reached, the status of the member will automatically expire and the qr code will be denied in the qr attendance.
  - If the status of the trainer and emloyee is inactive, the qr attendance will deny the qr code.
  - press Q to close the scanner
 

# Contact:
- FB: Anubhav Tripathi (Software Engineer)







