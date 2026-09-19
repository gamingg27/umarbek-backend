# InStudy CRM Backend

## Run
1. Create/activate a virtual environment.
2. `pip install -r requirements.txt`
3. `python manage.py makemigrations`
4. `python manage.py migrate`
5. `python manage.py createsuperuser`
6. `python manage.py runserver`

Frontend: `/`
Admin: `/admin/`

Main API routes:
- `/api/auth/`
- `/api/users/`
- `/api/education/students/`
- `/api/education/teachers/`
- `/api/education/courses/`
- `/api/education/groups/`
- `/api/finance/payment/`
- `/api/finance/salary/`
- `/api/attendance/attendance/`
- `/api/notifications/notification/`
- `/api/reports/report/`
