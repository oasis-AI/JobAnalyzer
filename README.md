


一个用于分析招聘软件的程序

工作的分析器

找工作的探路者


uv init -n JobAnalyzer --description "A tool for analyzing recruitment software" -p 3.12

uv add ruff

uv add fastapi --extra standard

创建pre-commit-config.yaml
使用

官网配置ruff





启动
uvicorn app.main:app --reload --port 8000
