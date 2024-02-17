# Define o comando padrão do Python
PYTHON = python3

# Define o nome do seu script Python
SCRIPT_NAME = convert_map_foundry_70ppx.py

# Comando de setup para instalar dependências
setup:
	@echo "Instalando dependências..."
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install Pillow PyInstaller

# Comando para construir o executável
build:
	@echo "Construindo o executável..."
	pyinstaller --onefile --windowed $(SCRIPT_NAME)

# Comando para limpar arquivos de build e dist
clean:
	@echo "Limpando arquivos de build e dist..."
	rm -rf build dist __pycache__
	rm -f *.spec
