# Forestry Platform

A Django-based platform for aggregating, processing, and analyzing forestry research documents from multiple sources using web scraping, PDF processing, OCR, and AI classification.

## Features

- **Multi-source Web Scraping**: Automatically scrape forestry documents from:
  - CIFOR (Center for International Forestry Research)
  - FAO (Food and Agriculture Organization)
  - IUFRO (International Union of Forest Research Organizations)
  - ReliefWeb
  - OpenLibrary
  
- **PDF Management**: Download and store PDFs locally with duplicate detection

- **OCR Processing**: Extract text from PDF documents using Tesseract OCR

- **AI Classification**: Automatically classify documents using transformer-based ML models

- **REST API**: RESTful API for document management and retrieval

- **Scheduled Tasks**: Automated document scraping and processing using APScheduler

- **Document Search**: Full-text search capabilities for documents

## Project Structure

```
forestry_platform/
├── documents/          # Django app for document management
│   ├── models.py       # Document model definition
│   ├── serializers.py  # REST API serializers
│   ├── views.py        # API endpoints
│   ├── search.py       # Search functionality
│   ├── citations.py    # Citation handling
│   └── admin.py        # Django admin configuration
├── scraper/            # Web scraping module
│   ├── base.py         # Base scraper class
│   ├── cifor.py        # CIFOR scraper
│   ├── fao.py          # FAO scraper
│   ├── iufro.py        # IUFRO scraper
│   ├── reliefweb.py    # ReliefWeb scraper
│   ├── openlibrary.py  # OpenLibrary scraper
│   ├── downloader.py   # PDF download handler
│   ├── duplicate.py    # Duplicate detection
│   ├── metadata.py     # Document metadata extraction
│   ├── scheduler.py    # Task scheduling
│   └── main.py         # Scraper entry point
├── ai/                 # AI/ML module
│   └── classifier.py   # Document classification
├── ocr/                # OCR processing
│   └── scanner.py      # PDF text extraction
├── downloads/          # Downloaded PDF storage
├── forestry/           # Django project settings
│   ├── settings.py     # Django configuration
│   ├── urls.py         # URL routing
│   └── wsgi.py         # WSGI application
├── requirements.txt    # Python dependencies
├── manage.py           # Django management script
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Docker Compose configuration
└── db.sqlite3          # SQLite database
```

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL (optional, uses SQLite by default)
- Tesseract OCR
- Docker (optional)

### Local Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd forestry_platform
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create superuser** (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

7. **Start development server**:
   ```bash
   python manage.py runserver
   ```

### Docker Setup

```bash
docker-compose up -d
```

This will:
- Build and start the Django application
- Set up the PostgreSQL database
- Create necessary volumes for downloaded documents

## Dependencies

Key dependencies include:

- **Django 5.2**: Web framework
- **Django REST Framework**: REST API development
- **requests**: HTTP client for web scraping
- **BeautifulSoup4 & lxml**: HTML/XML parsing
- **Playwright**: Browser automation for scraping
- **PyPDF & pdfplumber**: PDF manipulation
- **pytesseract & Pillow**: OCR processing
- **transformers & torch**: AI/ML classification
- **APScheduler**: Task scheduling
- **psycopg2**: PostgreSQL adapter

## Usage

### Web Scraping

#### Run all scrapers:
```bash
python manage.py shell
from scraper.main import run_all_scrapers
run_all_scrapers()
```

#### Run specific scraper:
```bash
from scraper.cifor import CIFORScraper
scraper = CIFORScraper()
scraper.scrape()
```

### API Endpoints

#### Get all documents:
```bash
GET /api/documents/
```

#### Get document details:
```bash
GET /api/documents/{id}/
```

#### Search documents:
```bash
GET /api/documents/search/?q=keyword
```

#### Create document:
```bash
POST /api/documents/
Content-Type: application/json

{
  "title": "Document Title",
  "source": "source_name",
  "source_url": "https://example.com",
  "pdf_url": "https://example.com/doc.pdf"
}
```

### OCR Processing

Extract text from PDFs:
```bash
from ocr.scanner import extract_text_from_pdf
text = extract_text_from_pdf('path/to/document.pdf')
print(text)
```

### AI Classification

Classify documents:
```bash
from ai.classifier import classify_document
classification = classify_document(document_text)
print(classification)
```

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
# Or for PostgreSQL:
# DATABASE_URL=postgresql://user:password@localhost:5432/forestry_db
```

### Settings

Edit `forestry/settings.py` to customize:
- Database configuration
- Installed apps
- Middleware
- Logging
- Static files

## Database Schema

### Document Model

```python
- id (Primary Key)
- title (CharField)
- source (CharField)
- source_url (URLField, Unique)
- pdf_url (URLField)
- local_file (FileField)
- summary (TextField)
- content (TextField)
- category (CharField)
- publication_date (DateField)
- downloaded_at (DateTimeField, Auto)
- hash (CharField, Unique)
```

## Development

### Running Tests

```bash
python manage.py test
```

### Code Quality

```bash
# Format code
black .

# Lint
flake8 .

# Type checking
mypy .
```

### Database Migrations

```bash
# Create migration
python manage.py makemigrations

# Apply migration
python manage.py migrate

# View migration SQL
python manage.py sqlmigrate documents 0001
```

## API Documentation

Full API documentation is available at:
- Swagger UI: `http://localhost:8000/api/docs/`
- ReDoc: `http://localhost:8000/api/redoc/`

## Architecture

```
┌─────────────────────────────────────┐
│        Web Scrapers                 │
│ (CIFOR, FAO, IUFRO, etc.)           │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Downloader & Duplicate Detection  │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│    OCR & Metadata Extraction        │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│     AI Classification               │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│      Django Database                │
│   (SQLite/PostgreSQL)               │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│       REST API                      │
└─────────────────────────────────────┘
```

## Troubleshooting

### Tesseract OCR Not Found
Install Tesseract:
- **Windows**: Download installer from https://github.com/UB-Mannheim/tesseract/wiki
- **macOS**: `brew install tesseract`
- **Linux**: `apt-get install tesseract-ocr`

### Database Connection Issues
- Ensure PostgreSQL is running (if using PostgreSQL)
- Check DATABASE_URL in `.env`
- Run migrations: `python manage.py migrate`

### Download Failures
- Check internet connection
- Verify source URLs are accessible
- Check disk space for downloads folder

## Performance Optimization

- Use connection pooling for database
- Enable caching for frequently accessed documents
- Use async tasks for long-running scraping jobs
- Index database fields used in searches

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For issues, questions, or suggestions, please open an issue on GitHub or contact the development team.

## Acknowledgments

- Data sources: CIFOR, FAO, IUFRO, ReliefWeb, OpenLibrary
- Built with Django, Django REST Framework, and modern ML/OCR tools
