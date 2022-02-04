from dash import *
from testapp import *

app = Dash(__name__)
server = app.server
app.layout = html.Div([
    github_info_header(),
    html.Img(src="assets/image.jpg")
])

if __name__ == '__main__':
    #app.run_server(debug=True)
    app.run_server(host='localhost', port=3000, debug=True)






