from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(120), nullable=False)
    last_name: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    subscription_date: Mapped[str] = mapped_column(DateTime)
    # Favorites #

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    population: Mapped[int] = mapped_column(Integer, nullable=False)
    diameter: Mapped[int] = mapped_column(Integer, nullable=False)
    climate: Mapped[str] = mapped_column(String(120), nullable=False)
    # Favorite #

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "diameter": self.name,
            "climate": self.climate
        }


class People(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(120), nullable=False)
    last_name: Mapped[str] = mapped_column(String(120), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    origin: Mapped[str] = mapped_column(String(120), nullable=False)
    # People #

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.name,
            "last_name": self.population,
            "age": self.name,
            "origin": self.climate
        }

class Favorites(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    planet_id: Mapped[int] = mapped_column(db.ForeignKey("planet.id"))
    planet: Mapped["Planet"] = db.relationship(backref="favorite")

    people_id: Mapped[int] = mapped_column(db.ForeignKey("people.id"))
    people: Mapped["People"] = db.relationship(backref="favorite")

    user_id: Mapped[int] = mapped_column(db.ForeignKey("user.id"))
    user: Mapped["User"] = db.relationship(backref="favorites")



    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
