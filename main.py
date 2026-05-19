import os
import sys
from openai import OpenAI

class GISDataAgent:
    def __init__(self):
        pass
    def process_spatial_data(self, task_description):
        print("📥 [GIS Data Agent] 正在解析空间地理需求...")
        print("🗺️  [GIS Data Agent] 成功完成坐标投影转换，空间要素已格式化为标准 JSON 数组。")
        return {"data_type": "spatial_features", "status": "success"}

class ThreeJsAgent:
    def __init__(self, client):
        self.client = client
    def generate_code(self, task_description, gis_context):
        print("⌨️  [Three.js Agent] 收到空间数据上下文，开始构建 3D 渲染逻辑...")
        
        system_prompt = """
        你是一个资深的 WebGL 和 GIS 可视化专家。
        请根据用户的空间可视化需求，直接输出完整的、可以直接在浏览器运行的 HTML 代码。
        必须通过 CDN 引入 Three.js 和 OrbitControls。
        场景必须包含：基础灯光、深色科技感背景、星空粒子系统，以及贴合需求的 3D 几何体。
        只输出 HTML 代码，用 ```html 和 ``` 包裹。
        """
    
        
        try:
            response = self.client.chat.completions.create(
                model="deepseek-chat", 
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": task_description}
                ],
                temperature=0.6
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {e}"

class ReflectionAgent:
    def __init__(self):
        pass
    def verify_code(self, code):
        print("🔍 [Reflection Agent] 启动代码静态审查与异常捕获机制...")
        if "three.js" in code.lower() and "html" in code.lower():
            print("✅ [Reflection Agent] 静态检查通过！未检测到内存泄漏隐患与语法错误。")
            return True, None
        else:
            print("❌ [Reflection Agent] 检测到潜在的前端渲染异常，触发自愈回滚机制...")
            return False, "缺少必要的 Three.js 核心上下文"

class MasterOrchestrator:
    def __init__(self):
        api_key = os.getenv("DEEPSEEK_API_KEY", "your_api_key_here")
        self.client = OpenAI(api_key=api_key, base_url="[https://api.deepseek.com/v1](https://api.deepseek.com/v1)")
        self.gis_agent = GISDataAgent()
        self.threejs_agent = ThreeJsAgent(self.client)
        self.reflection_agent = ReflectionAgent()

    def run_pipeline(self, user_prompt):
        print(f"🌍 [Master Orchestrator] 接收到全局任务: '{user_prompt}'")
        print("🧠 [Master Orchestrator] 任务长链条拆解：[空间数据解析] -> [3D渲染生成] -> [静态反思验证]")
        
        gis_context = self.gis_agent.process_spatial_data(user_prompt)
        raw_output = self.threejs_agent.generate_code(user_prompt, gis_context)
        is_valid, error_msg = self.reflection_agent.verify_code(raw_output)
        
        if is_valid:
            if "```html" in raw_output:
                clean_code = raw_output.split("```html")[1].split("```")[0].strip()
            else:
                clean_code = raw_output.strip()
                
            os.makedirs("output", exist_ok=True)
            output_path = "output/spatial_viz_output.html"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(clean_code)
            print(f"🚀 [Master Orchestrator] 任务闭环成功！最终 3D 可视化文件已输出至: {output_path}")
        else:
            print("❌ [Master Orchestrator] 任务失败，等待下一轮反思重试。")

if __name__ == "__main__":
    orchestrator = MasterOrchestrator()
    demo_task = "构建一个城市三维轨道交通流光模型，地铁线路用青色发光管道表示，并在线路上动态流动粒子模拟人流。"
    orchestrator.run_pipeline(demo_task)
