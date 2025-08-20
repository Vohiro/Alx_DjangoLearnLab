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