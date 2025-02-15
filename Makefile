# 配置变量（核心改进点）
VENV_PATH := .venv
PYTHON := $(VENV_PATH)/bin/python
UV_PIP := $(VENV_PATH)/bin/uv pip
APP_MODULE := app.main:app
PORT := 8000
DOCKER_IMAGE := jobanalyzer

.PHONY: help install install-dev run test lint format clean docker-build docker-run

help:  ## 显示所有可用命令
	@echo "Makefile commands:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: venv  ## 安装生产依赖
	@echo "Installing dependencies..."
	$(UV_PIP) install -r requirements.txt

install-dev: venv  ## 安装开发依赖
	@echo "Installing development dependencies..."
	$(UV_PIP) install -r requirements-dev.txt
	$(UV_PIP) install ruff pytest pre-commit mypy
	pre-commit install

run:  ## 启动开发服务器
	@echo "Starting the FastAPI server..."
	$(PYTHON) -m uvicorn $(APP_MODULE) --reload --host 0.0.0.0 --port $(PORT)

test:  ## 运行测试
	@echo "Running tests..."
	$(PYTHON) -m pytest -v tests/

lint:  ## 代码质量检查
	@echo "Running ruff for code style check..."
	$(VENV_PATH)/bin/ruff check app/ --fix
	$(VENV_PATH)/bin/mypy app/

format:  ## 格式化代码
	@echo "Formatting code with ruff..."
	$(VENV_PATH)/bin/ruff format app/

clean:  ## 清理缓存文件
	@echo "Cleaning up cache files..."
	find . -type d -name '__pycache__' -exec rm -rf {} +
	rm -rf .pytest_cache .ruff_cache

docker-build:  ## 构建Docker镜像
	@echo "Building Docker image..."
	docker build -t $(DOCKER_IMAGE) .

docker-run:  ## 运行Docker容器
	@echo "Running Docker container..."
	docker run -p $(PORT):$(PORT) $(DOCKER_IMAGE)

venv:  ## 创建虚拟环境（隐藏命令）
	if [ ! -d "$(VENV_PATH)" ]; then \
		python -m venv $(VENV_PATH); \
		$(UV_PIP) install --upgrade pip setuptools wheel; \
	fi
