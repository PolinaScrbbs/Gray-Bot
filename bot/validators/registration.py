import re

class RegistrationValidationError(Exception):
    pass

class RegistrationValidator:
    async def validate_username(username: str) -> str:
        if not username:
            raise RegistrationValidationError("Username не может быть пустым")
        if len(username) < 3:
            raise RegistrationValidationError("Username должен содержать не менее 3 символов")
        if len(username) > 20:
            raise RegistrationValidationError("Username не может содержать более 20 символов")
        if not re.match(r"^[a-zA-Z0-9_]+$", username):
            raise RegistrationValidationError("Username может содержать только латинские буквы, цифры и подчеркивания")

    async def validate_full_name(full_name):
        if not full_name:
            raise RegistrationValidationError("ФИО не может быть пустым")
        if not re.match(r"^[а-яА-ЯёЁ]+\s[а-яА-ЯёЁ]+\s[а-яА-ЯёЁ]+$", full_name):
            raise RegistrationValidationError(
                "Полное имя должно состоять из трех слов, записанных только русскими буквами"
            )

    async def validate_password(password, confirm_password):
        if not password:
            raise RegistrationValidationError("Пароль не может быть пустым")
        if password != confirm_password:
            raise RegistrationValidationError("Пароли не совпадают")
        if len(password) < 8:
            raise RegistrationValidationError(
                "Длина пароля должна составлять не менее 8 символов."
            )
        if len(password) > 20:
            raise RegistrationValidationError(
                "Длина пароля не может быть более 20 символов."
            )
        if not re.search(
            r"^[A-Za-z0-9!@#$%^&*()_+\-=\[\]{};:'\\|,.<>\/?]*$", password
        ):
            raise RegistrationValidationError(
                "Пароль должен состоять только из латинских букв, цифр и специальных символов."
            )
        if not re.search("[a-z]", password):
            raise RegistrationValidationError(
                "Пароль должен содержать хотя бы одну строчную букву."
            )
        if not re.search("[A-Z]", password):
            raise RegistrationValidationError(
                "Пароль должен содержать хотя бы одну заглавную букву."
            )
        if not re.search("[0-9]", password):
            raise RegistrationValidationError(
                "Пароль должен содержать хотя бы одну цифру."
            )
        if not re.search("[!@#$%^&*()_+-=]", password):
            raise RegistrationValidationError(
                "Пароль должен содержать хотя бы один специальный символ."
            )

    async def validate_phone_number(phone_number):
        if not phone_number:
            raise RegistrationValidationError("Номер телефона не может быть пустым")
        if not re.match(r"^\+?\d{10,15}$", phone_number):
            raise RegistrationValidationError("Номер телефона должен содержать от 10 до 15 цифр")

    async def validate_city(city):
        if not city:
            raise RegistrationValidationError("Город не может быть пустым")
        if len(city) > 50:
            raise RegistrationValidationError("Название города не может содержать более 50 символов")

    async def validate_address(address):
        if not address:
            raise RegistrationValidationError("Адрес не может быть пустым")
        if len(address) > 100:
            raise RegistrationValidationError("Адрес не может содержать более 100 символов")