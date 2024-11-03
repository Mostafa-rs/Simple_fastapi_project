from accounts.models import User


def password_validation(password, confirm_password):
    errors = []
    if password != confirm_password:
        errors.append('Passwords must match')
    if len(password) < 8:
        errors.append('Password must be at least 8 characters')
    if not any(c.isupper() for c in password):
        errors.append('Password must contain at least one uppercase character')
    if not any(c.isdigit() for c in password):
        errors.append('Password must contain at least one digit')

    return errors


def phone_number_validation(phone_number):
    errors = []

    if phone_number[:2] != '09':
        errors.append('Phone number must start with 09')

    if len(phone_number) != 11:
        errors.append('Phone number must have 11 digits')

    if not phone_number.isdigit():
        errors.append('phone number must be digits only')

    return errors


def user_register_validation(data, session):
    errors = []

    if phone_number_errors := phone_number_validation(data.phone_number):
        errors.extend(phone_number_errors)

    if session.query(User).filter_by(phone_number=data.phone_number).first():
        errors.append(f'phone {data.phone_number} already exists')

    if session.query(User).filter_by(email=data.email).first():
        errors.append(f'email {data.email} already exists')

    if password_errors := password_validation(data.password, data.confirm_password):
        errors.extend(password_errors)

    return errors
