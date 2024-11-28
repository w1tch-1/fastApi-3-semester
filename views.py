import shutil
from pathlib import Path
from functools import wraps

import db
from config import app, templates
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from db import get_db, User, Post, Comment

from fastapi.responses import HTMLResponse, RedirectResponse, Response
from fastapi import Request, Form, Depends, File, UploadFile


