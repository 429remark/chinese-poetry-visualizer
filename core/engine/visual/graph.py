import networkx as nx
from pyvis.network import Network
from typing import Optional, Set, List

class PoetryKnowledgeGraph:
    """
    诗词知识图谱
    构建诗、人、地、主题的多维关联
    """
    
    COLORS = {
        "author": "#C0392B",      # 朱砂
        "poem": "#2C3E50",        # 墨色
        "location": "#16A085",    # 碧绿
        "theme": "#F39C12",       # 鎏金
        "dynasty": "#8E44AD",     # 紫檀
    }
    
    def __init__(self):
        self.G = nx.DiGraph()
    
    def add_poem_node(self, title: str, author: str, dynasty: str):
        """添加诗作节点"""
        self.G.add_node(
            title,
            type="poem",
            title=f"《{title}》· {author}",
            color=self.COLORS["poem"]
        )
        self.G.add_edge(author, title, relation="创作")
    
    def add_author_node(self, name: str, dynasty: str, biography: str = ""):
        """添加诗人节点"""
        self.G.add_node(
            name,
            type="author",
            title=f"{name} · {dynasty}\n{biography[:100]}...",
            color=self.COLORS["author"]
        )
    
    def visualize(self, output_file: str = "poetry_graph.html") -> str:
        """生成交互式可视化"""
        nt = Network(
            height="800px",
            width="100%",
            directed=True,
            notebook=False,
            bgcolor="#f5f0e6",
            font_color="#2C3E50"
        )
        
        for node, attrs in self.G.nodes(data=True):
            nt.add_node(node, title=attrs.get("title", node), 
                       color=attrs.get("color", "#999"))
        
        for source, target, attrs in self.G.edges(data=True):
            nt.add_edge(source, target, title=attrs.get("relation", ""))
        
        nt.write_html(output_file)
        return output_file
