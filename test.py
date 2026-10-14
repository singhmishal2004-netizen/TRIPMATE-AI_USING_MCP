from Tools.tavily_tool import tavily_search
from Tools.flight_tool import search_flights
from backend import run_travel_agent
#res = tavily_search("Best hotel in india")
#res = search_flights("plan a 6 day trip to india from usa ")
res=run_travel_agent("plan a 6 day trip to india from usa ")
print(res)
