"""
Setup Database for Restaurants
"""

#!/usr/bin/env python3

import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()


class Restaurant(Base):
    """Create Reataurant Table"""
    __tablename__ = 'restaurant'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)

    @property
    def serialize(self):
        ''' Serialize function to send JSON objects in a serializable format'''
        return {
            'name': self.name,
            'id': self.id,
        }


class MenuItem(Base):
    """Create MenuItem Table"""
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    ## Add a serialize function to send JSON objects in a serializable format
    @property
    def serialize(self):
        ''' Serialize function to send JSON objects in a serializable format'''
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }

# ######insert at end of file #######

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
