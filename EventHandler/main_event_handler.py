from PyQt5.QtWidgets import QLineEdit
import Database.db_authentication as authentication
from ExceptionHanlder.exception_handler import CustomExceptionHandler


class MainEventHandler:
    def __init__(self, app, ui):
        self.app = app
        self.ui = ui
        self.login_disabled = False
        self.previous_page = 0
        self.current_page = 0
        self.remaining_time = 5
        self.countdown_timer = None
        self.failed_login_attempts = 0
        self.remaining_attempts = 3

    def toggle_password(self):
        sender = self.app.sender()  # Get the sender of the event
        try:
            # Check if the sender is the toggle password button
            if sender == self.ui.btn_toggle_password:
                # Check if the current page is the login page
                if self.current_page == 0:
                    # Check if the password line edit is in password mode
                    if self.ui.line_lgn_password.echoMode() == QLineEdit.Password:
                        # Change the password line edit to normal mode
                        self.ui.line_lgn_password.setEchoMode(QLineEdit.Normal)
                    else:
                        # Change the password line edit to password mode
                        self.ui.line_lgn_password.setEchoMode(QLineEdit.Password)
                # Check if the current page is the registration page
                elif self.current_page == 2:
                    # Check if the password line edit is in password mode
                    if self.ui.line_rg_password.echoMode() == QLineEdit.Password:
                        # Change the password line edit to normal mode
                        self.ui.line_rg_password.setEchoMode(QLineEdit.Normal)
                    else:
                        # Change the password line edit to password mode
                        self.ui.line_rg_password.setEchoMode(QLineEdit.Password)
        except Exception as e:
            custom_exception = CustomExceptionHandler(e)
            print(f"An error occurred during toggle password event,Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}")

    def login_event_handler(self):
        try:
            sender = self.app.sender()  # Get the sender of the event
            self.ui.previous_page = 0  # Set the previous page to 0
            if sender == self.ui.btn_lgn_login:  # Check if the sender is the login button
                # Check if login is not disabled due to multiple failed attempts
                if not self.login_disabled:
                    if authentication.user_db.authenticate_user(self.ui.line_lgn_userName.text(),
                                                                self.ui.line_lgn_password.text()):
                        self.ui.lbl_info_message.setText("You are connected!")  # Set the info message
                        self.ui.pages.setCurrentIndex(1)  # Set the current page index to 1
                        self.update_header()  # Update the header
                        self.reset_attempts()  # Reset the login attempts
                    else:
                        self.failed_login_attempts += 1  # Increment the failed login attempts
                        self.remaining_attempts -= 1  # Decrement the remaining attempts
                        if self.remaining_attempts > 0:
                            self.ui.lbl_info_message.setText(
                                'User information \nis wrong.' + f'\nRemaining Attempt: {3 - self.failed_login_attempts}')  # Set the info message
                            self.ui.pages.setCurrentIndex(1)  # Set the current page index to 1
                            self.update_header()  # Update the header
                        else:
                            self.login_disabled = True  # Disable the login
                            self.ui.lbl_info_message.setText('')  # Clear the info message
                            self.countdown_timer.start(1000)  # Start the countdown timer
                            self.ui.btn_info_return.hide()  # Hide the return button
                            self.ui.pages.setCurrentIndex(1)  # Set the current page index to 1
                            self.update_header()  # Update the header

            elif sender == self.ui.btn_lgn_info:  # Check if the sender is the info button
                self.ui.lbl_info_message.setText(
                    'User Name: Admin\nPassword: 12345')  # Set the info message with user credentials
                self.ui.pages.setCurrentIndex(1)  # Set the current page index to 1
                self.update_header()  # Update the header
            elif sender == self.ui.btn_lgn_register:  # Check if the sender is the register button
                self.ui.pages.setCurrentIndex(2)  # Set the current page index to 2
                self.update_header()  # Update the header
        except Exception as e:
            custom_exception = CustomExceptionHandler(e)
            print(f"An error occurred during login event,Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}")

    def message_event_handler(self):
        try:
            # Get the sender of the event
            sender = self.app.sender()
            # Return to the login window when the return button is clicked
            if sender == self.ui.btn_info_return:
                if self.previous_page == 0:
                    # Clear the text fields
                    self.clear_text()
                    # Show the login window
                    self.ui.pages.setCurrentIndex(0)
                    self.update_header()
                elif self.previous_page == 2:
                    # Clear the text fields
                    self.clear_text()
                    # Show the login window
                    self.ui.pages.setCurrentIndex(2)
                    self.update_header()
        except Exception as e:
            custom_exception = CustomExceptionHandler(e)
            print(f"An error occurred during message event handler,Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}")

    def register_event_handler(self):
        try:
            sender = self.app.sender()  # Get the sender of the event
            self.previous_page = 2  # Set the previous page to 2
            if sender == self.ui.btn_rg_register:  # Check if the sender is the register button

                user_name = self.ui.line_rg_userName.text()  # Get the username from the input field
                user_password = self.ui.line_rg_password.text()  # Get the user password from the input field
                phone = self.ui.line_rg_phone.text()  # Get the phone number from the input field
                email = self.ui.line_rg_email.text()  # Get the email from the input field
                self.ui.pages.setCurrentIndex(1)  # Set the current page index to 1
                self.update_header()  # Update the header
                result = authentication.user_db.add_user(user_name, user_password, phone,
                                                         email)  # Add the user to the database and get the result
                if result == 0:  # Check if the result is success
                    self.ui.lbl_info_message.setText("User Successfully Added")  # Set the info message
                    self.previous_page = 0  # Set the previous page to 0
                elif result == 1:  # Check if the result indicates empty fields
                    self.ui.lbl_info_message.setText("Please Fill All \nThe Blank Fields.")  # Set the info message
                elif result == 2:  # Check if the result indicates existing user information
                    self.ui.lbl_info_message.setText("User Information \nAlready Exists")  # Set the info message
                else:
                    self.ui.lbl_info_message.setText("An error occurred")  # Set the info message
                    print("An Result Error Occurred")  # Print an error message
                    print(result)  # Print the result
        except Exception as e:
            custom_exception = CustomExceptionHandler(e)
            print(f"An error occurred during register event,Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}")

    def update_countdown_label(self):
        try:
            # Update the countdown label with the remaining time or a message if the time is up
            if self.remaining_time > 0:  # Check if there is remaining time
                minutes = self.remaining_time // 60  # Calculate the remaining minutes
                seconds = self.remaining_time % 60  # Calculate the remaining seconds
                self.ui.lbl_info_message.setText(  # Set the label text with the remaining time
                    f"Please \ntry again in : \n{minutes:02d}:{seconds:02d}")
                self.remaining_time -= 1  # Decrement the remaining time
            else:
                self.countdown_timer.stop()  # Stop the countdown timer
                self.ui.lbl_info_message.setText(
                    "You can try again.")  # Set the label text to indicate the user can try again
                self.ui.btn_info_return.show()  # Show the return button
        except Exception as e:
            custom_exception = CustomExceptionHandler(e)
            print(f"An error occurred during countdown update event,Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}")

    def clear_text(self):
        try:
            # Clear input fields based on the previous page
            if self.previous_page == 0:  # Check the previous page
                # Clear input fields for login and registration
                self.ui.line_lgn_password.setText("")
                self.ui.line_rg_userName.setText("")
                self.ui.line_rg_password.setText("")
                self.ui.line_rg_email.setText("")
                self.ui.line_rg_phone.setText("")
            else:
                pass  # Do nothing if the previous page is not 0
        except Exception as e:
            custom_exception = CustomExceptionHandler(e)
            print(f"An error occurred during clear text event,Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}")

    def update_header(self):
        try:
            # Update the header label based on the current page
            self.current_page = self.ui.pages.currentIndex()  # Get the current page index
            if self.current_page == 0:  # Check if the current page is the login page
                self.ui.lbl_login.setText("Log In")  # Update the header label to indicate login
            elif self.current_page == 2:  # Check if the current page is the register page
                self.ui.lbl_login.setText("Register")  # Update the header label to indicate registration
            else:
                self.ui.lbl_login.setText("Info")  # Update the header label to indicate info page
        except Exception as e:
            custom_exception = CustomExceptionHandler(e)
            print(f"An error occurred during update header event,Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}")

    def reset_attempts(self):
        try:
            # Reset the login attempts and remaining attempts
            self.failed_login_attempts = 0  # Reset the failed login attempts
            self.remaining_attempts = 3  # Reset the remaining attempts
        except Exception as e:
            custom_exception = CustomExceptionHandler(e)
            print(f"An error occurred during reset attempts event,Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}")
