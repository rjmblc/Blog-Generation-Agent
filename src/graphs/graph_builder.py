from langgraph.graph import StateGraph,START,END
from src.llms.groq_llm import GroqLLM
from src.states.blogstate import BlogState
from src.nodes.blognode import BlogNode


class GraphBuilder:
    def __init__(self,llm):
        self.llm=llm
        self.graph=StateGraph(BlogState)

    def build_topic(self):
        """
        Build a graph  to generate blogs based on topic
        """
        self.blog_node_obj = BlogNode(self.llm)
        ### Nodes
        self.graph.add_node("title_creation",self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation",self.blog_node_obj.content_creation)

        self.graph.add_edge(START,"title_creation")
        self.graph.add_edge("title_creation","content_generation")
        self.graph.add_edge("content_generation",END)

        return self.graph

    def  setup_graph(self,usecase):
        if usecase =="topic":
            self.build_topic()
        return self.graph.compile()


llm = GroqLLM().get_llm()

graph_builder=GraphBuilder(llm)
graph=graph_builder.build_topic().compile()