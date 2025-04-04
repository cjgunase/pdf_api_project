# PDF Data Extraction API

## Overview
This project is a simple API built with [FastAPI](https://fastapi.tiangolo.com/) that extracts raw text from uploaded PDF files. It uses [pypdf](https://pypdf.readthedocs.io/en/latest/) to read PDF content and returns the extracted text as a JSON response.

## Features
- **Upload PDFs:** Accepts PDF files through a POST request.
- **Text Extraction:** Reads and extracts text from each page of the PDF.
- **JSON Response:** Returns the extracted text in a structured JSON format.
- **Error Handling:** Provides error messages for unsupported file types or unreadable PDFs.

## Tech Stack
- **Backend:** Python, FastAPI
- **Server:** Uvicorn
- **PDF Processing:** pypdf

## Setup & Installation

### Prerequisites
- [Python 3.11+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

### Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/chathurajgunasekara/pdf_api_project.git
