import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ================================
# MODEL CONFIG
# ================================
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4")
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 1000))

# ================================
# SECURITY FLAGS
# ================================
ENABLE_GUARDRAILS = os.getenv("ENABLE_GUARDRAILS", "true") == "true"
ENABLE_PERMISSION_CHECK = os.getenv("ENABLE_PERMISSION_CHECK", "true") == "true"
ENABLE_SECRET_DETECTION = os.getenv("ENABLE_SECRET_DETECTION", "true") == "true"

# ================================
# ATTACK SYSTEM
# ================================
ENABLE_ATTACK_GENERATION = os.getenv("ENABLE_ATTACK_GENERATION", "true") == "true"
ENABLE_MULTI_AGENT_ATTACKS = os.getenv("ENABLE_MULTI_AGENT_ATTACKS", "true") == "true"

# ================================
# DEBUG
# ================================
DEBUG = os.getenv("DEBUG", "false") == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")