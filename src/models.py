from pydantic import BaseModel, HttpUrl, Field

class ProgramFile(BaseModel):
    name: str = Field( min_length=1, description="Название программы")
    icon: str = Field(description="Путь к файлу иконки или URL")
    url: HttpUrl = Field(description="Ссылка на программу или ресурс")
    
class ProgramFiles(BaseModel):
    programs: list[ProgramFile]
