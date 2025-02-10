FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["pytest", "--html=reports/pytest-html-report.html"]
