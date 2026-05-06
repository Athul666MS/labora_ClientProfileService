# Client Profile Service

Client Profile Service is a dedicated microservice in the **Freelancing Platform** responsible for handling all **client-specific profile management**.  
It works independently from authentication and freelancer services and follows a **JWT-based microservice architecture**.

---

## 📌 Service Responsibilities

This service manages:

- Client personal and company details
- Client bio, industry, and website
- Profile image handling
- Client verification status
- Job posting statistics
- Client spending summary

❌ This service does NOT handle:
- User registration
- Login or password management
- Token generation
- Freelancer profiles

---

## 🧠 System Architecture

- **Backend Framework**: Django, Django REST Framework
- **Authentication**: JWT (issued by Auth Service)
- **Database**: MySQL
- **Architecture Style**: Microservices
- **Communication**: REST APIs (JSON)

The service identifies users using `user_id` extracted from the JWT token.

---

## 📂 Project Structure

Authorization: Bearer <JWT_TOKEN>

4. Client Profile Service:
- Validates token
- Extracts `user_id` and `role`
- Allows access only if role = `client`

---

## 🛂 Role-Based Access Control

| Role | Access |
|----|------|
| Client | Create / View / Update own profile |
| Admin | View & verify client profiles |
| Freelancer | ❌ No access |

---

## 📡 API Endpoints

### Client APIs

| Method | Endpoint | Description |
|------|---------|-------------|
| POST | `/api/client/profile/` | Create client profile |
| GET | `/api/client/profile/` | Get own profile |
| PUT | `/api/client/profile/` | Update profile |

### Admin APIs

| Method | Endpoint | Description |
|------|---------|-------------|
| GET | `/api/client/{id}/` | View any client |
| PATCH | `/api/client/verify/{id}/` | Verify client |

---

## ⚙️ Environment Variables

Create a `.env` file:



DEBUG=True
DJANGO_SECRET_KEY=your_secret_key

DB_NAME=freelance_client
DB_USER=root
DB_PASSWORD=*****
DB_HOST=localhost
DB_PORT=3306

JWT_PUBLIC_KEY_PATH=/path/to/public.pem


---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone <repository-url>
cd client-profile-service

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Run Server
python manage.py runserver
