from sqlalchemy import Column, Integer, Text, ForeignKey

from app.models.base import CharityDonationBaseClass


class Donation(CharityDonationBaseClass):
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    comment = Column(Text)

    def __repr__(self) -> str:
        return (f'Donation from user_id: {self.user_id}; '
                f'comment: {self.comment}; '
                f'full_amount: {self.full_amount}; '
                f'create date: {self.create_date}.')
