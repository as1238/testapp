from dash import *
from testapp import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.layout = html.Div([
    github_info_header(),
    html.Div(dcc.Input(id='input-box', type='text')),
    html.Button('Submit', id='button'),
    html.Div(id='output-container-button',
             children='Please submit a value'),
    html.Img(src="assets/FX.jpg")
])

if __name__ == '__main__':
    #app.run_server(debug=True)
    app.run_server(host='localhost', port=3000, debug=True)






