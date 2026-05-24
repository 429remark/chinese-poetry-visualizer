from typing import Optional, Dict, List
import asyncio
from ..core.poem import Poem, Verse, PoemType, EmotionTone

class PoetryAnalyzer:
    """
    中华诗词深度赏析引擎
    基于 MiMo-V2.5 的文化理解能力
    """
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.system_prompt = """
        你是一位精通中华古典文学的国学大师，熟读《全唐诗》《全宋词》《昭明文选》等经典。
        你的分析既有学术的严谨，又有文学的温度。
        请用诗意的语言，但又要精准、深刻。
        """
    
    async def analyze_full(self, title: str, author: str, 
                          content: str, dynasty: str = "未知") -> Poem:
        """完整分析一首诗"""
        
        verses = await self._parse_verses(content)
        
        poem = Poem(
            poem_id=self._generate_id(author, title),
            title=title,
            author=author,
            dynasty=dynasty,
            content=verses,
            poem_type=self._detect_type(content)
        )
        
        print(f"✅ 正在分析：{poem}")
        return poem
    
    async def _parse_verses(self, content: str) -> List[Verse]:
        """解析为诗句单元"""
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        return [Verse(content=line) for line in lines]
    
    def _generate_id(self, author: str, title: str) -> str:
        """生成唯一ID"""
        return f"{author}_{title}"
    
    def _detect_type(self, content: str) -> PoemType:
        """检测诗歌体裁"""
        if any(c in content for c in ["调", "令", "慢", "引"]):
            return PoemType.CI
        if "赋" in content[:20]:
            return PoemType.FU
        return PoemType.SHI
