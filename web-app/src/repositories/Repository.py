from flask import current_app as app
from .abstracts.AbcRepository import AbcRepository

from .. import db


# TODO: Switch to usage of Generics and implement get_all, get_by_id
class Repository(AbcRepository):

    @staticmethod
    def add_and_commit(item) -> None:
        """
        Adds a new Item and Commit the Changes to Database
        """
        try:
            db.session.add(item)
            db.session.commit()
        except Exception as e:
            app.logger.critical(e)
            db.session.rollback()

    @staticmethod
    def delete_and_commit(item) -> None:
        """
        Deletes a existing Item and Commit the Changes to Database
        """
        try:
            db.session.delete(item)
            db.session.commit()
        except Exception as e:
            app.logger.critical(e)
            db.session.rollback()

    @staticmethod
    def add(item) -> None:
        """
        Adds a new Item
        """
        try:
            db.session.add(item)
        except Exception as e:
            app.logger.critical(e)
            db.session.rollback()

    @staticmethod
    def delete(item) -> None:
        """
        Deletes a existing Item
        """
        try:
            db.session.delete(item)
        except Exception as e:
            app.logger.critical(e)
            db.session.rollback()

    @staticmethod
    def commit() -> None:
        """
        Commits Db-Session to Database
        """
        try:
            db.session.commit()
        except Exception as e:
            app.logger.critical(e)
            db.session.rollback()
