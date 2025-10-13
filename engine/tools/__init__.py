from engine.tools.calculator import calculator
from engine.tools.document_qa import get_response_from_documents
from engine.tools.finance import stock_report
from engine.tools.weather import get_weather
from engine.tools.fallback import llm_fallback

tools = [calculator, get_response_from_documents, stock_report, get_weather,llm_fallback]