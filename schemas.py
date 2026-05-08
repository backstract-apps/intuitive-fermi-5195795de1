from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple,Union

import re

class Categories(BaseModel):
    user_id: int
    name: str
    color_hex: str
    created_at_dt: Optional[Any]=None


class ReadCategories(BaseModel):
    user_id: int
    name: str
    color_hex: str
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class Tasks(BaseModel):
    user_id: int
    category_id: Optional[Union[int, float]]=None
    title: str
    description: Optional[str]=None
    priority: str
    status: str
    due_date: Optional[str]=None
    completed_at_dt: Optional[Any]=None
    created_at_dt: Optional[Any]=None
    updated_at_dt: Optional[Any]=None


class ReadTasks(BaseModel):
    user_id: int
    category_id: Optional[Union[int, float]]=None
    title: str
    description: Optional[str]=None
    priority: str
    status: str
    due_date: Optional[str]=None
    completed_at_dt: Optional[Any]=None
    created_at_dt: Optional[Any]=None
    updated_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class Users(BaseModel):
    email: str
    password: str
    created_at_dt: Optional[Any]=None


class ReadUsers(BaseModel):
    email: str
    password: str
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True




class PostPlatformAuthPackageMaysonAuthUserLogin(BaseModel):
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostCategories(BaseModel):
    user_id: int = Field(...)
    name: str = Field(..., max_length=100)
    color_hex: str = Field(..., max_length=7)
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutCategoriesId(BaseModel):
    id: str = Field(..., max_length=100)
    user_id: int = Field(...)
    name: str = Field(..., max_length=100)
    color_hex: str = Field(..., max_length=7)
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostTasks(BaseModel):
    user_id: Union[int, float] = Field(...)
    category_id: Optional[Union[int, float]]=None
    title: str = Field(..., max_length=255)
    description: Optional[str]=None
    priority: str = Field(..., max_length=10)
    status: str = Field(..., max_length=10)
    due_date: Optional[str]=None
    completed_at_dt: Optional[str]=None
    created_at_dt: Optional[str]=None
    updated_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutTasksId(BaseModel):
    id: str = Field(..., max_length=100)
    user_id: Union[int, float] = Field(...)
    category_id: Optional[Union[int, float]]=None
    title: str = Field(..., max_length=255)
    description: Optional[str]=None
    priority: str = Field(..., max_length=10)
    status: str = Field(..., max_length=10)
    due_date: Optional[str]=None
    completed_at_dt: Optional[str]=None
    created_at_dt: Optional[str]=None
    updated_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostUsers(BaseModel):
    email: str = Field(..., max_length=255)
    password: str = Field(..., max_length=255)
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: str = Field(..., max_length=100)
    email: str = Field(..., max_length=255)
    password: str = Field(..., max_length=255)
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostPlatformAuthPackageMaysonAuthUserRegister(BaseModel):
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



# Query Parameter Validation Schemas

class GetCategoriesIdQueryParams(BaseModel):
    """Query parameter validation for get_categories_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetTasksIdQueryParams(BaseModel):
    """Query parameter validation for get_tasks_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteTasksIdQueryParams(BaseModel):
    """Query parameter validation for delete_tasks_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetUsersIdQueryParams(BaseModel):
    """Query parameter validation for get_users_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteUsersIdQueryParams(BaseModel):
    """Query parameter validation for delete_users_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteCategoriesIdQueryParams(BaseModel):
    """Query parameter validation for delete_categories_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True
