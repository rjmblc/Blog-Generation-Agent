from typing_extensions import TypedDict


class Blog(TypedDict, total=False):
    title: str
    content: str


class BlogState(TypedDict, total=False):
    topic: str
    blog: Blog
    current_language: str