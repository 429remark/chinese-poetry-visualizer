```python
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Optional, Set
from enum import Enum

class PoemType(Enum):
    """诗歌体裁"""
    SHI = "诗"
    CI = "词"
    QU = "曲"
    FU = "赋"
    WEN = "文"
    YUEFU = "乐府"

class EmotionTone(Enum):
    """情感基调"""
    HEROIC = "豪放"
    GRACEFUL = "婉约"
    MELANCHOLY = "忧思"
    JOYFUL = "喜悦"
    TRANQUIL = "恬淡"
    PATRIOTIC = "爱国"
    NOSTALGIC = "思乡"
    FAREWELL = "送别"

@dataclass
class Verse:
    """诗句：最基本的诗意单元"""
    content: str
    pinyin: Optional[str] = None
    annotation: Optional[str] = None
    imagery: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        if not self.imagery:
            self.imagery = self._extract_imageries()
    
    def _extract_imageries(self) -> List[str]:
        """从诗句中提取古典意象"""
        common_imageries = [
            "月", "风", "云", "雨", "雪", "山", "水", "江", "河", "湖", "海",
            "柳", "梅", "兰", "竹", "菊", "松", "荷", "桃", "梨", "杏",
            "雁", "鹤", "莺", "燕", "杜鹃", "鹏",
            "楼", "台", "亭", "阁", "桥", "船", "舟",
            "酒", "剑", "琴", "棋", "书", "画",
            "春", "秋", "夕阳", "黄昏", "明月", "东风", "西风"
        ]
        return [img for img in common_imageries if img in self.content]

@dataclass
class Poem:
    """一首完整的诗"""
    poem_id: str
    title: str
    author: str
    dynasty: str
    content: List[Verse]
    poem_type: PoemType
    creation_year: Optional[int] = None
    creation_location: Optional[str] = None
    
    translation: Optional[str] = None
    appreciation: Optional[Dict[str, str]] = None
    artistic_conception: Optional[str] = None
    emotion_tone: Optional[EmotionTone] = None
    
    themes: Set[str] = field(default_factory=set)
    techniques: List[str] = field(default_factory=list)
    related_poems: List[str] = field(default_factory=list)
    related_locations: List[str] = field(default_factory=list)
    
    created_at: datetime = field(default_factory=datetime.now)
    source: Optional[str] = None
    
    @property
    def full_text(self) -> str:
        """完整诗文"""
        return "\n".join([v.content for v in self.content])
    
    @property
    def word_count(self) -> int:
        """字数统计"""
        return sum(len(v.content) for v in self.content)
    
    def __hash__(self):
        return hash(self.poem_id)
    
    def __str__(self):
        return f"《{self.title}》· {self.author} ({self.dynasty})"
