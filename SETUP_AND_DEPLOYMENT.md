# Setup & Deployment Guide

## Local Setup (Windows/Mac/Linux)

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AkashSR07/Classical-Ciphers-Lab.git
   cd Classical-Ciphers-Lab
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

   The app will open at `http://localhost:8501`

## Deployment Options

### Option 1: Streamlit Cloud (Free & Easy)

1. Push your code to GitHub
2. Go to https://share.streamlit.io
3. Sign in with GitHub
4. Click "New app" and select your repository
5. Select the branch and app.py file
6. Click Deploy!

Your app will be live at: `https://[your-username]-classical-ciphers-lab.streamlit.app`

### Option 2: Heroku (Free tier available)

1. Create `Procfile`:
   ```
   web: streamlit run --server.port=$PORT app.py
   ```

2. Deploy:
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

### Option 3: Replit

1. Import your GitHub repository
2. Replit auto-detects requirements.txt
3. Run the app directly in Replit

### Option 4: PythonAnywhere

1. Upload files to PythonAnywhere
2. Set up virtual environment
3. Create web app with Flask/Streamlit WSGI
4. Access your deployed app

## Features

- **Caesar Cipher**: Encryption/Decryption with configurable shift
- **Vigenère Cipher**: Keyword-based polyalphabetic encryption
- **Brute Force Attack**: Try all 26 possible shifts for Caesar cipher
- **Frequency Analysis**: Visualize character distribution
- **Interactive UI**: Built with Streamlit for easy interaction

## Project Structure

```
Classical-Ciphers-Lab/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── SETUP_AND_DEPLOYMENT.md        # This file
└── .gitignore                      # Git ignore rules
```

## Technology Stack

- **Framework**: Streamlit 1.28.1
- **Visualization**: Plotly 5.17.0
- **Language**: Python 3.8+
- **Dependencies**: See requirements.txt

## Project for Portfolio

This project demonstrates:
✅ Full-stack web application development
✅ Cryptography algorithm implementation
✅ Interactive UI/UX design
✅ Data visualization
✅ GitHub repository management
✅ Deployment & DevOps

## Usage Examples

### Caesar Cipher
- Enter plaintext: "Hello World"
- Set shift: 3
- Click Encrypt → "Khoor Zruog"

### Vigenère Cipher
- Enter plaintext: "Send backup supplies"
- Set key: "CRYPTOGRAPHY"
- Click Encrypt → "UVls uoibue zsrgjxxg"

### Brute Force Attack
- Paste encrypted text: "Khoor Zruog"
- Click "Attack" → See all 26 possible decryptions
- Shift 3 will show original message: "Hello World"

## Educational Value

This project teaches:
- Classical encryption methods
- Basic cryptanalysis techniques
- Frequency analysis visualization
- Web application development
- Deployment strategies

## Security Note

These classical ciphers are **NOT secure** for modern use. They're included for educational purposes only. For real security, use:
- AES-256 (symmetric encryption)
- RSA-2048 (asymmetric encryption)
- TLS/SSL (secure communication)

## Contributing

Feel free to:
- Add more cipher implementations
- Improve UI/UX
- Add more cryptanalysis tools
- Submit pull requests

## License

MIT License - Feel free to use for educational projects

## Questions?

Open an issue on GitHub or contact the developer.
