from sqlalchemy import Column, Integer, String, Text
from app.configs.databaseConfig import Base


class Image(Base):
    __tablename__ = 'image'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, index=True, nullable=False)
    url = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    file_extension = Column(String, nullable=True)
    create_time = Column(String, nullable=True)

    def __repr__(self):
        return (f"<Image(id={self.id}, filename={self.filename}, url={self.url}, description={self.description}, "
                f"file_extension={self.file_extension}), create_time{self.create_time}>")
