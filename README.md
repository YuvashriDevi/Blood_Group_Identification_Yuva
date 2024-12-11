                               Blood Group Identification System

Overview: The Blood Group Identification System is a web-based application designed to identify blood groups by analyzing images of blood cells. It leverages Django for the backend and OpenCV for image processing to automate and simplify the traditionally manual process of blood typing. This system ensures quick, reliable, and accurate identification of both the ABO blood group and Rh factor.
Features: Automated Blood Typing: Identifies the ABO group and Rh factor from uploaded blood cell images. User Management: Registration and secure login. Personalized profile page to display results. Image Processing: Preprocessing images using techniques like grayscale conversion, thresholding, and morphological operations for accurate analysis. Dashboard Navigation: User-friendly interface for seamless access to the application features. Secure Data Storage: Stores user credentials and results securely in a structured database.
Tech Stack: Frontend: HTML CSS Backend: Django Image Processing: OpenCV Base64 Database: SQLite
https://drive.google.com/file/d/1B3SDodyRP22CbBDJVXF--sfx54krhcOG/view?usp=sharing

Installation:

Prerequisites: Ensure you have the following installed: Python (version 3.8 or higher) pip (Python package installer) Virtual environment (optional but recommended) Steps: 1. Clone this repository: git clone https://github.com/sumathi1205/Infosys-project.git cd blood-group-identification

 2.  Set up a virtual environment (optional but recommended):
        python -m venv venv
        source venv/bin/activate  # On Windows, use venv\Scripts\activate

 3.  Install the required packages:
        pip install -r requirements.txt
        
 4. Run migrations to set up the database:
        python manage.py migrate

 5. Start the Django development server:
        python manage.py runserver

 6. Access the application in your browser at http://127.0.0.1:8000.

How It Works:
 
 1. Registration & Login:
       New users register by entering basic details.
       Existing users log in securely to access their accounts.

2. Image Upload:
      Users upload images of blood cells for analysis.
      
3. Image Processing:
      The system preprocesses the uploaded image using OpenCV techniques:
      Converts the image to grayscale.
      Applies Gaussian blur to reduce noise.
      Thresholding highlights relevant features.
      Morphological operations refine contours for accurate analysis.
      
4. Result Display:
      The system identifies the ABO group and Rh factor.
      Results, along with the processed image, are displayed on the user’s profile page.

Routes:

                Route	                                Description
                
                /home	                                Main page introducing the system.
                /about	                              Information about the project.
                /contact	                            Contact details for support.
                /service	                            Access to the blood group analyzer.
                /login	                              User login page.
                /register	                            User registration page.

Outputs:

![Screenshot 2024-12-11 193258](https://github.com/user-attachments/assets/3102fb11-3909-4eee-8163-9fbcf185dfdf)


![Screenshot 2024-12-11 193354](https://github.com/user-attachments/assets/5535f30f-6cd6-45f4-8aa5-33e1b691317b)

![Screenshot 2024-12-11 193413](https://github.com/user-attachments/assets/a061bebe-b7c2-4f60-9ca5-4b5441563ae7)

![Screenshot 2024-12-11 193444](https://github.com/user-attachments/assets/67094b1c-74fe-412c-aec7-c63e20e34bb3)


Contributors: * Konatham Sumathi * Yuvashri Devi * Rajdeep Mondal

Future Scope: Integrate advanced AI/ML models for improved accuracy and speed. Expand support for additional blood tests or health parameters. Develop a mobile application for easier access.
