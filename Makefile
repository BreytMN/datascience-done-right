PYTHON_VERSION = 3.12

.PHONY: all help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

python: ## Install and config python
	@sudo apt-get update
	@sudo apt update && sudo apt upgrade -y
	@sudo apt install software-properties-common -y
	@sudo add-apt-repository ppa:deadsnakes/ppa
	@sudo apt-get install python-is-python3
	@sudo apt install python$(PYTHON_VERSION)
	@sudo apt install python$(PYTHON_VERSION)-venv
	@python$(PYTHON_VERSION) -m ensurepip
	@sudo update-alternatives --install /usr/bin/python python /usr/bin/python$(PYTHON_VERSION) $(subst .,,$(PYTHON_VERSION))

venv: ## Create virtual env
	@rm -rf .venv/ && python -m venv .venv && . .venv/bin/activate; \
	pip install --upgrade pip; \
	pip install uv; \
	uv pip install \
		-r requirements.txt \
		-r requirements_dev.txt; \
	pre-commit install;
