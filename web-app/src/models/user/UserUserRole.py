from ... import db

class UserUserRole(db.Model):

    __tablename__ = 'user_userroles'


    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer(),
        db.ForeignKey(
            'users.id',
            ondelete='CASCADE'
        )
    )    
    
    userrole_id = db.Column(
        db.Integer(),
        db.ForeignKey(
            'userroles.id',
            ondelete='CASCADE'
        )
    )
