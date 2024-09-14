from database import Base

from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey

class Users(Base):

    id = Column(Integer, primary_key=True)
    f_name = Column(String)
    l_name = Column(String)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    phone = Column(Integer, unique=True)
    date_of_birth = Column(Date)
    location = Column(String)
    nationality = Column(String)
    notice_period = Column(String)
    current_fixed = Column(Integer)
    current_variable = Column(Integer)
    current_ctc = Column(Integer)    
    expected_ctc = Column(Integer)    
    is_open = Column(Boolean, default=True)
    current_company = Column(String)
    current_resps = Column(String)
    skills = Column(String)
    leet_url = Column(String)
    github_url = Column(String)
    li_url = Column(String)
    other_url = Column(String)


class Career(Base):

    #resume = Column()
    previous_company = Column(String)
    previous_resps = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    
class jobs(Base):

    jobs_applied = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))
