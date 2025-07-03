"""Defines constants."""

import os, logging
import dotenv

dotenv.load_dotenv()

GEMINI_2_0_FLASH = "gemini-2.0-flash"
GEMINI_2_5_PRO_PREVIEW_05_06 = "gemini-2.5-pro-preview-05-06"
MATH_AGENT_BASE_URL = 'http://localhost:8003'
PUBLIC_AGENT_CARD_PATH = '/.well-known/agent.json'
EXTENDED_AGENT_CARD_PATH = '/agent/authenticatedExtendedCard'
LOGGING_LEVEL = logging.INFO

PROMPTS = [
    "What is 1+2?",
    "Calculate 2 + 2",
    "What is the square root of 16?",
    "What is sin(pi/4)?",
    "Calculate log(100)",
    "Solve x^2 - 4 = 0",
    "Solve 2x + 5 = 11",
    "Find the roots of x^3 - 6x^2 + 11x - 6 = 0",
    "Find the derivative of x^2 + 3x + 2",
    "Calculate the integral of x^2",
    "What is the derivative of sin(x)?",
    "Integrate e^x dx",
    "What is the determinant of [[1,2],[3,4]]?",
    "Multiply matrices [[1,2],[3,4]] and [[5,6],[7,8]]",
    "Find the inverse of [[2,1],[1,1]]",
    "Transpose [[1,2,3],[4,5,6]]",
    "Find the mean of [1,2,3,4,5]",
    "Calculate the standard deviation of [10,12,14,16,18]",
    "What is the median of [1,3,5,7,9,11]?",
    "Find the variance of [2,4,6,8,10]"
]