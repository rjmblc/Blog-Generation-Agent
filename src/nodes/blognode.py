from src.states.blogstate import BlogState

class BlogNode:
    """
    A class to represent a blog node
    """

    def __init__(self,llm):
        self.llm=llm

    def title_creation(self,state:BlogState):
        """
        create the title for the blog
        """

        if "topic" in state and state["topic"]:
            prompt = """
            you are an expert blog content writer. Use  markdown  formatting. Generate a blog title for the {topic}. The title should be creative and SEO friendly
            
            """
            system_message=prompt.format(topic=state["topic"])
            response = self.llm.invoke(
                system_message
            )

            return {"blog":{"title":response.content}}

    def content_creation(self,state:BlogState):
        """
        create the content for the blog
        """
        
        if "blog" in state and state["blog"]:
            prompt = """
            you are an expert blog content writer: Use the markdown formatting. Generate content for the {topic}. The content should be creative and SEO friendly

            """
            system_message=prompt.format(topic=state["topic"])
            response=self.llm.invoke(
                system_message
            )

            return {"blog":{"title":state["blog"]["title"],"content":response.content}}
            