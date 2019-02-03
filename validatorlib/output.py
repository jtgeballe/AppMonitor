import smtplib, ssl, json, os


smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "jtgeballe@gmail.com"
password = ""


class Email:

    def __init__(self, msg, lock):
        self.__msg = msg
        self.__lock = lock

    def send(self):
        file_path = "watcherfile.txt"

        try:
            self.__lock.acquire()
            if not os.path.isfile(file_path) or os.stat(file_path).st_size == 0:
                data = {"entries": []}
                data["entries"].append(self.__msg)
                with open(file_path, "w") as outfile:
                    json.dump(data, outfile)
            else:
                with open(file_path, "r") as json_file:
                    all_lines = json_file.read()
                    data = json.loads(all_lines)
                    data["entries"].append(self.__msg)

            with open(file_path, 'w') as outfile:
                json.dump(data, outfile)

        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            self.__lock.release()

    def send_e(self):
        # Create a secure SSL context
        context = ssl.create_default_context()

        # Try to log in to server and send email
        try:
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()  # Can be omitted
            server.starttls(context=context)  # Secure the connection
            server.ehlo()  # Can be omitted
            # server.login(sender_email, password)
            # TODO: Send email here
            # server.sendmail(sender_email, "jtgeballe@hotmail.com", self.__msg)
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit()
