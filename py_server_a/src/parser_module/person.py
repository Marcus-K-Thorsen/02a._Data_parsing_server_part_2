from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import List, Union

class Person(BaseModel):
    
    name: str = Field(
        default=...,
        description="Name of the person.",
        examples=["James"]
    )
    
    weight: Union[float, int, str] = Field(
        default=...,
        description="Weight of the person.",
        examples=[85.5]
    )
    
    hobbies: List[str] = Field(
        default_factory=list(),
        description="Hobbies of the person.",
        examples=[["reading", "swimming"]]
    )
    
    file_type: str = Field(
        default=...,
        description="The file type the person is from.",
        examples=["json"]
    )
    
    language: str = Field(
        default="python",
        description="The programming language the person is from.",
        examples=["python"]
    )
    
    model_config = ConfigDict(from_attributes=True)
    
    @field_validator("weight")
    def validate_weight(cls, weight: Union[float, int, str]) -> float:
        if not isinstance(weight, (float, int, str)):
            raise ValueError("Weight must be a number.")
        if isinstance(weight, str):
            try:
                weight = float(weight)
            except ValueError:
                raise ValueError("Weight must be a string that can become a floating number.")
        if isinstance(weight, int):
            weight = float(weight)
        return weight


    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I weigh {self.weight} kg. and my hobbies are {', '.join(self.hobbies)}"

    def __repr__(self) -> str:
        hobbies_str = ', '.join(f"'{hobby}'" for hobby in self.hobbies)
        return f"Person {{\n  name: '{self.name}',\n  weight: {self.weight},\n  hobbies: [ {hobbies_str} ]\n}}"
    