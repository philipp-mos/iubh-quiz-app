from .abstracts.AbcRepository import AbcRepository

from .. import db

# TODO: Switch to usage of Generics and implement get_all, get_by_id
class Repository(AbcRepository):
    
    @staticmethod
    def add(item):
        """
        Adds a new Item and Commit the Changes to Database
        """
        try:
            db.session.add(item)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()


    @staticmethod
    def delete(item):
        """
        Deletes a existing Item and Commit the Changes to Database
        """
        try:
            db.session.delete(item)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()


    @staticmethod
    def update(item):
        """
        Updates a defined Record with new Values
        """
        raise NotImplementedError