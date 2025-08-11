# core/settings.py
from pathlib import Path
import os
import environ

# Caminhos
BASE_DIR = Path(__file__).resolve().parent.parent

# django-environ
env = environ.Env(
    DJANGO_DEBUG=(bool, True),
)
# Lê o .env da raiz do projeto
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# ---- Segurança / Debug ----
SECRET_KEY = env("DJANGO_SECRET_KEY", default="unsafe-dev-secret-change-me")
DEBUG = env("DJANGO_DEBUG", default=True)

# Em dev, deixar "*" é ok; em prod use env com domínios
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["*"])

# ---- Apps ----
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Terceiros
    "rest_framework",
    "corsheaders",
    "professionals"
]

# ---- Middleware ----
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # CORS deve ficar bem no topo (logo após SecurityMiddleware)
    "corsheaders.middleware.CorsMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# ---- Banco de Dados (PostgreSQL pelo docker-compose) ----
# O .env deve conter DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME", default="projeto_lacrei"),
        "USER": env("DB_USER", default="postgres"),
        "PASSWORD": env("DB_PASSWORD", default="postgres"),
        "HOST": env("DB_HOST", default="db"),
        "PORT": env("DB_PORT", default="5432"),
    }
}

# ---- Validação de senha ----
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ---- i18n / tz ----
LANGUAGE_CODE = "pt-br"

# O desafio sugeria 'UTC'. Se preferir horário local durante o dev:
# TIME_ZONE = "America/Sao_Paulo"
TIME_ZONE = "UTC"

USE_I18N = True
USE_TZ = True

# ---- Static ----
STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ---- CORS / CSRF ----
# Leia origens do .env (ex: http://localhost:3000,http://127.0.0.1:3000)
_raw_cors = env("CORS_ALLOWED_ORIGINS", default="")
CORS_ALLOWED_ORIGINS = [o.strip() for o in _raw_cors.split(",") if o.strip()]

# Se precisar confiar em origens pro CSRF:
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])
