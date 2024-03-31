import sqlalchemy
from source.database.db_session import SqlAlchemyBase


# Модель настроек игры
class SettingModel(SqlAlchemyBase):
    __tablename__ = 'settings'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    value = sqlalchemy.Column(sqlalchemy.String)
