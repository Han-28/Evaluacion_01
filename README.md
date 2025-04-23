# 📚 MangaReader - Lector de Mangas con Django


Aplicación web para buscar y guardar mangas usando la API de MangaDex, con funciones CRUD completas.

## 🚀 Características
- Búsqueda en tiempo real de mangas
- Biblioteca personal para guardar favoritos

## 🛠 Tecnologías
- **Backend**: Django 4.2
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **API**: [MangaDex API](https://api.mangadex.org/docs/)
- **Base de datos**:  SQLite (local)

## 📦 Instalación Local
### Requisitos
- Python 3.10+
- Pip

### Pasos
1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/mangareader.git
   cd mangareader
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instala dependencias:
   ```bash
   pip install -r src/requirements.txt
   ```

4. Configura variables de entorno (crea `.env` en `src/`):
   ```env
   DEBUG=True
   SECRET_KEY=tu_super_secreto_aqui
   ```

5. Ejecuta las migraciones:
   ```bash
   cd src
   python manage.py migrate
   ```

6. Inicia el servidor:
   ```bash
   python manage.py runserver
   ```
