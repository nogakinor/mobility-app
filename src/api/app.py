from flask import Flask

app = Flask(__name__)

@app.get('/non_treated_hazards')
def all_non_treated_hazards():
    filter = "ALL_NON_TREATED"
    query = "SQL_QUERY"
    return 0

@app.get('/hazards_in_radius/<location>/<radius>')
def hazards_in_radius(location, radius):
    circle_x, circle_y = location
    x, y = (0,0)
    if ((x - circle_x) * (x - circle_x) + (y - circle_y) * (y - circle_y) <= radius * radius):
        x,y = (0,0)
        # TODO: x,y in radius
    else:
        x,y = (0,0)
        # TODO: x,y not in radius
    filter = "LOCATION AND RADIUS"
    query = "SQL_QUERY"
    return 0