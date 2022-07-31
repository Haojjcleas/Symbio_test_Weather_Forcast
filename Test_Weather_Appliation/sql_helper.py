# -*- coding: utf-8 -*-
# Create:       2022-07-29
# Last modify:  2022-07-29
# Author:       Junjie Hao
# Contact:      mail@haojjcleas.net

from sqlalchemy import Column, CHAR, VARCHAR, TEXT, Integer, FLOAT, SmallInteger, create_engine, ForeignKey, DateTime, func, DATE
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Weather(Base):

    __tablename__ = "cs_weather"

    c_city_code = Column(Integer, primary_key=True)
    c_date = Column(DateTime)
    c_city = Column(CHAR(16))  # Longest Chinese City Name : NaRanSeBuSiTaiYinBuLaGe
    c_weather = Column(FLOAT)


dialect = 'mysql'
driver = 'pymysql'
username = 'symbio_test'
password = 'GN3bfPB6yNwfZK5c'
host = 'www.haojjcleas.net'
port = '3306'
database = 'symbio_test'

SQL_PATH = dialect + '+' + driver + '://' + username+':'+password+'@'+host+':'+port+'/'+database

engine = create_engine(SQL_PATH, pool_recycle=7200, pool_size=20, max_overflow=10, pool_timeout=30, echo=False)
DBSession = sessionmaker(bind=engine)
db_session = DBSession()


if __name__ == "__main__":
    Base.metadata.create_all(engine)
