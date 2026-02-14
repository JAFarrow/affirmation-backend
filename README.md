# Affirmation — Backend

LIVE: https://affirmation-backend-aqrp.onrender.com

**NB** First request can take some time as backend cold starts.

Backend API for the **Mood Architect** affirmation project.  
Built with **Flask** and deployed on **Render**.  
This service exposes a single API endpoint that generates personalized, supportive affirmations using the OpenAI API.

---

# Tech Stack

- Python
- Flask
- Gunicorn (production server)
- Hosted on Render

---

# Local Development

## 1. Clone the repository

```bash
git clone https://github.com/JAFarrow/affirmation-backend
cd affirmation-backend
```

## 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Environment Variables

Create a `.env` file (or set via shell):

```bash
OPENAI_API_KEY=your_api_key_here
FRONTEND_URL=http://localhost:5173
```

### Required Variables

- `OPENAI_API_KEY` — OpenAI API key (required)
- `FRONTEND_URL` — allowed CORS origin for frontend

**Security Requirements**

- Never commit secrets
- Secrets can be added via the render UI

---

## 5. Run Development Server

```bash
gunicorn app:run
```

---

# Production — Render Deployment

## Steps

1. Push backend repository to GitHub
2. Create new Web Service on Render
3. Connect repository
4. Set start command:

```
gunicorn run:app
```

5. Add environment variables in Render dashboard:

```
OPENAI_API_KEY=<YOUR_SECRET>
FRONTEND_URL=<YOUR_FRONTEND_URL>
```

6. Deploy
