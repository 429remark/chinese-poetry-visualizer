"""
诗人画像模块
定义诗人的生平、作品、社交网络等数据结构
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class LifeEvent:
    """人生轨迹节点"""
    year: int
    location: str
    event: str
    related_poem: Optional[str] = None

@dataclass
class Author:
    """诗人全景画像"""
    author_id: str
    name: str
    dynasty: str
    
    # TODO: 实现完整的作者信息字段
    # style_name: str = None  # 字
    # hao: str = None         # 号
    # birth_year: int = None
    # death_year: int = None
    # biography: str = None
    # life_events: List[LifeEvent] = field(default_factory=list)
    # representative_works: List[str] = field(default_factory=list)
    # friends: List[str] = field(default_factory=list)
    
    def __str__(self):
        return f"{self.name} · {self.dynasty}"
