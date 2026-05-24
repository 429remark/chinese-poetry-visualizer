"""
诗境系统使用示例
"""

import asyncio
from core.poem import Poem, Verse, PoemType
from engine.analyzer import PoetryAnalyzer
from visual.graph import PoetryKnowledgeGraph

async def demo_analyze_poem():
    """演示：分析一首诗"""
    
    print("🏯 诗境系统 - 中华传统诗词可视化")
    print("=" * 50)
    
    # 初始化引擎
    analyzer = PoetryAnalyzer("your-api-key-here")
    
    # 分析《登高》
    poem = await analyzer.analyze_full(
        title="登高",
        author="杜甫",
        dynasty="唐",
        content="""风急天高猿啸哀，渚清沙白鸟飞回。
无边落木萧萧下，不尽长江滚滚来。
万里悲秋常作客，百年多病独登台。
艰难苦恨繁霜鬓，潦倒新停浊酒杯。"""
    )
    
    print(f"\n✅ 分析完成：{poem}")
    print(f"📝 字数统计：{poem.word_count} 字")
    print(f"🎨 检测到的意象：{', '.join(sum([v.imagery for v in poem.content], []))}")
    
    # 构建知识图谱
    print("\n🕸️ 正在构建知识图谱...")
    graph = PoetryKnowledgeGraph()
    graph.add_author_node("杜甫", "唐", "唐代伟大的现实主义诗人")
    graph.add_poem_node("登高", "杜甫", "唐")
    
    output_file = graph.visualize()
    print(f"✅ 图谱已生成：{output_file}")
    
    print("\n🎉 恭喜！你的第一个诗词分析完成！")

if __name__ == "__main__":
    asyncio.run(demo_analyze_poem())
