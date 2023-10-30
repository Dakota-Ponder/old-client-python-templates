# python script to add and query an employee in the database using ORM.
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Employee(Base):
    """Employee ORM model for the database."""
    __tablename__ = 'employees'
    id = Column(Integer, Sequence('emp_id_seq'), primary_key=True)
    name = Column(String(50))


# Setup and connection:
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Add and query an employee in the database:
session = Session()
new_employee = Employee(name='John Doe')
session.add(new_employee)
session.commit()

# print the employee
for emp in session.query(Employee).all():
    print(emp.id, emp.name)
