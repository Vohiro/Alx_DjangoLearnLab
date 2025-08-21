## Overview
This project sets up the foundation of a Social Media API with Django + DRF.  
It includes custom user authentication, registration, login, and profile management.

## Features
- Custom User Model (with bio, profile picture, followers)
- Token-based Authentication
- Endpoints:
  - `/api/accounts/register/` → User registration
  - `/api/accounts/login/` → User login
  - `/api/accounts/profile/` → Profile view/update (auth required)

## Posts & Comments

### Endpoints
- POST          /api/posts/              (auth)  → create post
- GET           /api/posts/              (open)  → list posts  (?search=, ?author=, ?ordering=, ?page=)
- GET           /api/posts/{id}/         (open)  → retrieve post
- PUT           /api/posts/{id}/         (auth, owner only)
- PATCH/DELETE  /api/posts/{id}/ (auth, owner only)
- GET           /api/posts/{id}/comments/ (open) → list comments for a post

- POST          /api/comments/           (auth)  → create comment
- GET           /api/comments/           (open)  → list comments (?post=, ?author=, ?search=, ?ordering=, ?page=)
- GET/PUT/PATCH/DELETE /api/comments/{id}/ (auth; edit/delete owner only)

## User_Follow & Feeds

### Endpoints
- POST /accounts/follow/<id>/      (auth)  → Follow User Endpoint
- POST /accounts/unfollow/<id>/    (auth)  → Unfollow User Endpoint
- GET /posts/feed/                 (auth)  → User Feed Endpoint
