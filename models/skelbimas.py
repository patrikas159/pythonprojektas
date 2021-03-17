from . import db


class Auction(db.Model):

    __tablename__ = "Auction"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.VARCHAR(50),nullable=False)
    category = db.Column(db.VARCHAR(50), nullable=False)
    description = db.Column(db.VARCHAR(200),nullable=False)
    city = db.Column(db.VARCHAR(50),nullable=False)
    price = db.Column(db.Integer,nullable=False)
    image = db.Column(db.VARCHAR(256), nullable=False)
    views = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
