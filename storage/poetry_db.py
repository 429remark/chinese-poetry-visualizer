"""
诗词数据库
存储和检索上万首古诗词
"""

from typing import List, Optional
from ..core.poem import Poem

class PoetryDatabase:
    """诗词数据库"""
    
    def __init__(self, db_path: str = "data/poetry.db"):
        self.db_path = db_path
        self.poems = {}  # 内存存储，后续换 SQLite
    
    def add_poem(self, poem: Poem):
        """添加一首诗到数据库"""
        self.poems[poem.poem_id] = poem
    
    def search_by_author(self, author: str) -> List[Poem]:
        """按作者搜索"""
        return [p for p in self.poems.values() if p.author == author]
    
    def search_by_title(self, title_keyword: str) -> List[Poem]:
        """按标题搜索"""
        return [p for p in self.poems.values() if title_keyword in p.title]
    
    def search_by_content(self, keyword: str) -> List[Poem]:
        """按内容搜索"""
        return [p for p in self.poems.values() if keyword in p.full_text]
    
    def get_all_poems(self) -> List[Poem]:
        """获取所有诗词"""
        return list(self.poems.values())
