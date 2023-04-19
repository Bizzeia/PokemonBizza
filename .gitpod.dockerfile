FROM gitpod/workspace-mysql
RUN pip install mysql-connector-python
RUN pip install -U flask
RUN pip install pandas
