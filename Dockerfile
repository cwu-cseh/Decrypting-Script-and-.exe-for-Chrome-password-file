FROM python:latest

RUN pip install pyinstaller
RUN pip install pycryptodomex

CMD ["pyinstaller", "src/get_password.py"]
