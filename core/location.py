"""
诗意的坐标模块
定义有文化历史的地点信息
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from enum import Enum

class LocationType(Enum):
    """地点类型"""
    MOUNTAIN = "山"
    RIVER = "河"
    LAKE = "湖"
    CITY = "城"
    PAVILION = "亭台楼阁"
    TEMPLE = "寺庙"
    PASS = "关隘"

@dataclass
class HistoricalLayer:
    """历史文化层"""
    dynasty: str
    name: str
    description: str

@dataclass
class PoeticLocation:
    """有诗意的地点"""
    loc_id: str
    name: str
    location_type: LocationType
    coordinates: Tuple[float, float]  # (经度, 纬度)
    
    # TODO: 实现完整的地点信息
    # modern_name: str = None
    # historical_layers: List[HistoricalLayer] = field(default_factory=list)
    # scene_descriptions: Dict[str, str] = field(default_factory=dict)
    
    def __str__(self):
        return f"{self.name} [{self.location_type.value}]"
