from sqlalchemy import Column, String, Text

from app.models.base import CharityDonationBaseClass


class CharityProject(CharityDonationBaseClass):
    name = Column(String(100))
    description = Column(Text)

    def __repr__(self) -> str:
        return (f'Charity Project: {self.name}; '
                f'description: {self.description}; '
                f'create date: {self.create_date}.')
