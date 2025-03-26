# Medicine Tracker

Medicine Tracker is a Django-based web application designed to help users manage their daily, weekly, and monthly medicine schedules. Users can log their medicine intake, track progress, and deactivate medicines when no longer needed.

## Features

- **Daily Medicine Log**: Track medicines for the current day.
- **Weekly Medicine Log**: View and manage medicines for the week.
- **Monthly Medicine Log**: Overview of medicines for the entire month.
- **Add New Medicines**: Add medicines with dosage, frequency, and dose count.
- **Mark as Taken**: Update medicine logs to reflect doses taken.
- **Deactivate Medicines**: Remove medicines from active tracking.
- **Custom Themes**: Switch between themes for a personalized experience.

## Project Structure

```
django-tracker/
├── .gitignore
├── db.sqlite3
├── manage.py
├── requirements.txt
├── medicine_tracker/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── tracker/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   └── tracker/
│   │       ├── medicine_log.html
│   │       └── ...
│   └── ...
└── users/
    ├── forms.py
    ├── views.py
    └── ...
```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/medicine-tracker.git
   cd medicine-tracker
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:8000`.

## Usage

1. **Register an Account**:
   - Create a new user account to start tracking medicines.

2. **Add Medicines**:
   - Use the "Add New Medicine" form to add medicines with details like name, dosage, frequency, and dose count.

3. **Track Progress**:
   - View daily, weekly, or monthly logs to track medicine intake.
   - Mark medicines as taken or deactivate them when no longer needed.

4. **Switch Themes**:
   - Customize the appearance by switching between available themes.

## Requirements

- Python 3.8+
- Django 4.2.9
- Additional dependencies listed in `requirements.txt`.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your fork.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- Built with [Django](https://www.djangoproject.com/).
- UI powered by [Bootstrap v5](https://getbootstrap.com/).

---

Feel free to reach out with any questions or suggestions!
