from engine.tools.calculator import calculator
from engine.tools.document_qa import get_response_from_documents
from engine.tools.finance import stock_report
from engine.tools.weather import get_weather
from engine.tools.fallback import llm_fallback
from engine.tools.calendar import get_today_date, calendar_add_event, calendar_list_events, calendar_get_event, calendar_update_event, calendar_delete_event, calendar_events_on_date
from engine.tools.music import audio_play, audio_stop, audio_pause, audio_resume, audio_next, audio_previous, audio_status

tools = [calculator, get_response_from_documents, stock_report, get_weather,llm_fallback]
tools = [*tools, audio_play, audio_stop, audio_pause, audio_resume, audio_next, audio_previous, audio_status]
tools = [*tools, get_today_date, calendar_add_event, calendar_list_events, calendar_get_event, calendar_update_event, calendar_delete_event, calendar_events_on_date]