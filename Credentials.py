# Logins Class for PWManager V1
from abc import abstractmethod

class Credentials():

    def __init__(self, app, username, email):
        """Initializer."""
        self._app = app
        self._username = username
        self._email = email

    @property
    def app(self):
        return self._app

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    @abstractmethod
    def asdict(self):
        """Abstract method for turning object into dictionary."""
        raise NotImplementedError

    @abstractmethod
    def password(self):
        """Abstract password method."""
        raise NotImplementedError

    @abstractmethod
    def file(self):
        """Abstract file method."""
        raise NotImplementedError

    def __repr__(self):
        """Return string representation for repr()."""
        return(f'Login for: {self._app}\n' +
            f'Username: {self._username}\n' +
            f'Email: {self._email}\n')


class Login(Credentials):
        """Login class."""

        def __init__(self, app, username, email, password, url, notes):
            """Initializer."""
            super().__init__(app, username, email)
            self._password = password
            self._url = url
            self._notes = notes 

        @property
        def app(self):
            return self._app

        @app.setter
        def app(self, app):
            self._app = app

        @property
        def username(self):
            return self._username

        @username.setter
        def username(self, username):
            self._username = username

        @property
        def email(self):
            return self._email

        @email.setter
        def email(self, email):
            self._email = email

        @property
        def password(self):
            return self._password

        @password.setter
        def password(self, password):
            """Override password method for Login."""
            self._password = password
        
        @property
        def url(self):
            return self._url

        @url.setter
        def url(self, url):
            self._url = url

        @property
        def notes(self):
            return self._notes

        @notes.setter
        def notes(self, notes):
            self._notes = notes

        def asdict(self):
            """Override asdict method from Credentials. 
                Returns object as a dictionary of it's attributes."""
            return {"app": self.app, "username": self.username, 
                    "email": self.email, "password": self.password, 
                    "url": self.url, "notes": self.notes}

        def __repr__(self):
            """Return string representation for repr()."""
            return(f'Login for: {self._app}\n' +
                f'Username: {self._username}\n' +
                f'Email: {self._email}\n' +
                f'Password: {self._password}\n' +
                f'URL: {self._url}\n' +
                f'Notes: {self._notes}\n')


class MasterLogin(Credentials):
    """Master Login sub-class."""

    def __init__(self, username, email, password):
        """Initializer.""" 
        super().__init__('PWmanager', username, email)
        self._password = password
        self._file = f'{username}_vault.txt'
    
    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, username):
        """Override file method for MasterLogin."""
        self._file = f'{username}_vault.txt'
    
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        """Override password method for MasterLogin."""
        self._password = password

    def asdict(self):
        """Override asdict method from Credentials.
            Returns object as a dictionary of it's attributes."""
        return {"app": self.app, "password": self.password,
                "username": self.username, "email": self.email, 
                "filename": self.file}

    def __repr__(self):
        """Return string representation for repr()."""
        return(f"Username: {self._username}\n" +
            f"Email: {self._email}\n" +
            f"Filename: {self._file}\n" +
            f"Password: {self._password}")