from flask import Flask,render_template, request, jsonify
import vertexai
from vertexai.language_models import CodeChatModel
from vertexai.preview.generative_models import GenerativeModel, Part

import os
from dotenv import load_dotenv


