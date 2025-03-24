import os
import sys

def main():
    """Run administrative tasks."""
    print("Starting manage.py...")  # Debugging log
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicine_tracker.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        print("Error importing Django:", exc)  # Debugging log
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    print("Executing command:", sys.argv)  # Debugging log
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
