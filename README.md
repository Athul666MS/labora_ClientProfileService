# Client Profile Service

Client Profile Service stores and manages client-side profile records for Labora users. It trusts Auth Service JWTs for identity and uses the JWT `user_id` as the profile owner.

## Responsibilities

- Create, update, view, and delete the authenticated client's profile.
- Store client business/profile metadata independently from Auth Service.
- Provide a paginated internal client list for Admin Service.

## Features

- Client-only profile CRUD.
- `user_id` is taken from the authenticated JWT during profile creation and lookup.
- Optional profile image storage under `media/client_profiles/`.
- Paginated internal listing ordered by newest profile.

## API Endpoints

Base path: `/api/`

| Method | Path | Auth | Description |
| --- | --- | --- | --- |
| `POST` | `client/add/` | Client JWT | Create a client profile for the authenticated user. |
| `PUT`, `PATCH` | `client/update/` | Client JWT | Partially update the authenticated user's profile. |
| `GET` | `client/view/` | Client JWT | Return the authenticated user's profile. |
| `DELETE` | `client/delete/` | Client JWT | Delete the authenticated user's profile. |

## Internal Service Endpoints

Internal endpoints use `X-Service-Key: <SERVICE_API_KEY>`.

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `internal/clients/` | Return paginated client summaries. |

## Authentication

Public profile APIs require `Authorization: Bearer <access_token>` and the token role must be `client`. JWT verification uses the shared RS256 public key.

## Environment Variables

| Variable | Purpose |
| --- | --- |
| `DJANGO_SECRET_KEY` | Django secret key. |
| `DEBUG` | Enables debug mode when set to `True`. |
| `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD` | MySQL database configuration. |
| `JWT_PUBLIC_KEY_PATH` | Public key used to verify Auth Service JWTs. |
| `SERVICE_API_KEY` | Shared key for internal service endpoints. |
| `*_SERVICE_URL` | Optional service URLs loaded by settings for cross-service configuration. |

## Setup

```bash
cd ClientProfileService
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8001
```

## Service Architecture

- Django project: `client_profile_service`
- App: `profiles`
- Authentication: `profiles.authentication.CustomJWTAuthentication`
- Role checks: `profiles.role_permissions.IsClient`
- Internal service-key permission: `profiles.permissions.internal_service.IsInternalService`

## Database Models

- `ClientProfile`: stores `user_id`, `company_name`, `full_name`, `bio`, `location`, `profile_image`, `industry`, `website`, `total_jobs_posted`, `total_spent`, `is_verified`, and timestamps.

## Notification/Event Flow

This service does not emit notifications or WebSocket events.
