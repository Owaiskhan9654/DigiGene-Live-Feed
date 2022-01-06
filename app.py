import datetime
from flask import Flask, redirect, render_template
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from plotly import subplots
from dash.dependencies import Input, Output
import http.client
import json
from werkzeug.serving import run_simple
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from concurrent.futures import ThreadPoolExecutor

external_stylesheets = [
    'https://github.com/Owaiskhan9654/DigiGene/blob/bdf66f620f8b75b59f7a4e4687508ec908b9a6c8/DigiGene.css']


server = Flask(__name__)

@server.route('/')
def index():
    return 'Hello User.. Please add proper URL to move to DigiGene Web app'

dashApp = dash.Dash(__name__, external_stylesheets=external_stylesheets,title="DigiGene Live Feed Web Based Data Analysis Application",
    server=server,
    routes_pathname_prefix='/DigiGene/')
dashApp._favicon = "favico.ico"
dashApp.layout = html.Div(
    html.Div([
        html.Div(id='live-update-text', style={'padding': '5px', 'fontSize': '32px', 'textAlign': 'center',
                                               'backgroundColor': 'rgb(17, 17, 17)', 'color': 'white'}),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1 * 5000,  # in milliseconds
            n_intervals=0
        )
    ], ),
)


def rgb_to_hex(r, g, b):
    return ('{:x}{:x}{:x}').format(r, g, b)


@dashApp.callback(Output('live-update-text', 'children'),
              Input('interval-component', 'n_intervals'))
def update_metrics(n):
    # Current_color = open("Current_color.txt","r")
    # Current_color= Current_color.readlines()

    conn = http.client.HTTPSConnection("getpantry.cloud")
    payload = ''
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("GET", "/apiv1/pantry/2cb1189d-f1e5-4acb-8fba-c86b8282f25f/basket/DigiGeneV1", payload, headers)
    res = conn.getresponse()
    data_pantry = res.read()

    data_pantry = json.loads(data_pantry.decode('utf-8'))
    Current_color = data_pantry["current"]

    def int_custom(a):
        try:
            return (int(a))
        except:
            return 0

    Current_color = Current_color.split(' ,')
    Current_color = [int_custom(i) for i in Current_color]

    RedSensor1 = Current_color[0]
    GreenSensor1 = Current_color[1]
    BlueSensor1 = Current_color[2]
    RedSensor2 = Current_color[4]
    GreenSensor2 = Current_color[5]
    BlueSensor2 = Current_color[6]
    RedSensor3 = Current_color[8]
    GreenSensor3 = Current_color[9]
    BlueSensor3 = Current_color[10]

    # print('RedSensor1 ',Current_color[0],'GreenSensor1 ',Current_color[1],'BlueSensor1 ', Current_color[2])
    Sensor1_name = '#' + rgb_to_hex(RedSensor1, GreenSensor1, BlueSensor1)
    Sensor2_name = '#' + rgb_to_hex(RedSensor2, GreenSensor2, BlueSensor2)
    Sensor3_name = '#' + rgb_to_hex(RedSensor3, GreenSensor3, BlueSensor3)
    style = {'padding': '3px', 'fontSize': '24px', 'textAlign': 'center', 'backgroundColor': 'rgb(17, 17, 17)',
             'color': 'white'}
    return [

        html.Span('DigiGene Live Feed Web Based Data Analysis Application', style=style),
        html.Br(),
        html.Span('Sensor 1:  Red {0:.2f}, Sensor 1: Green {1:.2f}, Sensor 1: Blue {2:.2f}, Green1/Blue1: {3:.2f},\
        Blue1/Red1: {4:.2f}'.format(RedSensor1, GreenSensor1, BlueSensor1, GreenSensor1 / BlueSensor1,
                                    BlueSensor1 / RedSensor1, )
                  , style=style),
        html.Br(),
        html.Span('Sensor 2: Red {0:.2f} , Sensor 2: Green {1:.2f}, Sensor 2: Blue {2:.2f},Green2/Blue2: {3:.2f},Blue2/Red2: {4:.2f}\
        '.format(RedSensor2, GreenSensor2, BlueSensor2, GreenSensor2 / BlueSensor2, BlueSensor2 / RedSensor2, ),
                  style=style)
        , html.Br(),
        html.Span('Sensor 3: Red {0:0.2f} , Sensor 3: Green {1:.2f}, Sensor 3: Blue {2:.2f}, Green3/Blue3: {3:.2f},Blue3/Red3: {4:.2f}\
        '.format(RedSensor3, GreenSensor3, BlueSensor3, GreenSensor3 / BlueSensor3, BlueSensor3 / RedSensor3, ),
                  style=style),
        html.Br(),
        html.Div(className='row',
                 style={'display': 'flex', 'color': 'white', 'padding-left': '300px', 'padding-right': '300px'},
                 children=[
                     html.Div('Sensor 1 Color',
                              style={'color': 'white', 'backgroundColor': 'rgb(17, 17, 17)', 'padding': '35px',
                                     'fontSize': '32px',
                                     'textAlign': 'center', }, className='col s6 m6', ),
                     html.Div('                 ',
                              style={'backgroundColor': Sensor1_name, 'padding': '35px', 'fontSize': '32px',
                                     'textAlign': 'center', 'borderRadius': '15px', }, className='col s6 m6', ),

                     html.Div('Sensor 2 Color',
                              style={'color': 'white', 'backgroundColor': 'rgb(17, 17, 17)', 'padding': '35px',
                                     'fontSize': '32px',
                                     'textAlign': 'center', }, className='col s6 m6', ),
                     html.Div('               ',
                              style={'backgroundColor': Sensor2_name, 'padding': '35px', 'fontSize': '32px',
                                     'textAlign': 'center', 'borderRadius': '15px', }, className='col s6 m6', ),

                     html.Div('Sensor 3 Color',
                              style={'color': 'white', 'backgroundColor': 'rgb(17, 17, 17)', 'padding': '35px',
                                     'fontSize': '32px',
                                     'textAlign': 'center', }, className='col s6 m6', ),

                     html.Div('               ',
                              style={'backgroundColor': Sensor3_name, 'padding': '35px', 'fontSize': '32px',
                                     'textAlign': 'center', 'borderRadius': '15px', }, className='col s6 m6', )])
    ]


# '+str(int(RedSensor1))+','+str(int(GreenSensor1))+ ','+str(int(BlueSensor1))+'

# Multiple components can update everytime interval gets fired.
@dashApp.callback(Output('live-update-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_graph_live(n):
    data = {
        'time': [],
        'Red Sensor 1': [],
        'Green Sensor 1': [],
        'Blue Sensor 1': [],
        'Red Sensor 2': [],
        'Green Sensor 2': [],
        'Blue Sensor 2': [],
        'Red Sensor 3': [],
        'Green Sensor 3': [],
        'Blue Sensor 3': [],
    }
    conn = http.client.HTTPSConnection("getpantry.cloud")
    payload = ''
    headers = {
        'Content-Type': 'application/json'
    }
    # Collect some data
    for i in range(6):
        time = datetime.datetime.now() - datetime.timedelta(seconds=i * 3)
        # Current_color = open("Current_color.txt","r")
        # Current_color= Current_color.readlines()
        # print(Current_color)

        conn.request("GET", "/apiv1/pantry/2cb1189d-f1e5-4acb-8fba-c86b8282f25f/basket/DigiGeneV1", payload, headers)
        res = conn.getresponse()
        data_pantry = res.read()

        data_pantry = json.loads(data_pantry.decode('utf-8'))
        Current_color = data_pantry["current"]

        def int_custom(a):
            try:
                return (int(a))
            except:
                return 0

        Current_color = Current_color.split(' ,')
        Current_color = [int_custom(i) for i in Current_color]

        RedSensor1 = Current_color[0]
        GreenSensor1 = Current_color[1]
        BlueSensor1 = Current_color[2]
        RedSensor2 = Current_color[4]
        GreenSensor2 = Current_color[5]
        BlueSensor2 = Current_color[6]
        RedSensor3 = Current_color[8]
        GreenSensor3 = Current_color[9]
        BlueSensor3 = Current_color[10]

        # RedSensor1 = random.randint(1, 25)
        # GreenSensor1 = random.randint(1, 55)
        # BlueSensor1 = random.randint(20, 25)
        # RedSensor2 = random.randint(50, 75)
        # GreenSensor2 = random.randint(60, 95)
        # BlueSensor2 = random.randint(45, 55)
        # RedSensor3 = random.randint(1, 25)
        # GreenSensor3 = random.randint(1, 55)
        # BlueSensor3 = random.randint(1, 35)
        data['Red Sensor 1'].append(RedSensor1)
        data['Green Sensor 1'].append(GreenSensor1)
        data['Blue Sensor 1'].append(BlueSensor1)

        data['Red Sensor 2'].append(RedSensor2)
        data['Green Sensor 2'].append(GreenSensor2)
        data['Blue Sensor 2'].append(BlueSensor2)

        data['Red Sensor 3'].append(RedSensor3)
        data['Green Sensor 3'].append(GreenSensor3)
        data['Blue Sensor 3'].append(BlueSensor3)
        data['time'].append(time)

    # Create the graph with subplots
    fig = subplots.make_subplots(rows=3, cols=3, vertical_spacing=0.2, subplot_titles=[
        'Red Sensor 1',
        'Green Sensor 1',
        'Blue Sensor 1',
        'Red Sensor 2',
        'Green Sensor 2',
        'Blue Sensor 2',
        'Red Sensor 3',
        'Green Sensor 3',
        'Blue Sensor 3',
    ], )
    fig['layout']['margin'] = {
        'l': 50, 'r': 10, 'b': 10, 't': 60
    }
    # fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

    # fig.add_bar(
    #   x =data['time'],
    #   y= data['Red Sensor 1'],
    #   name= 'Red Sensor 1',
    # width=800,

    # 'line':dict(width=1, color='red')
    #   marker=dict(color="Red"),
    #   row=1, col=1)

    fig.append_trace({
        'x': data['time'],
        'y': data['Red Sensor 1'],
        'name': 'Red Sensor 1',
        'mode': 'lines',
        'line': dict(width=1, color='Red')
    }, 1, 1)

    fig.append_trace({
        'x': data['time'],
        'y': data['Green Sensor 1'],
        'name': 'Green Sensor 1',
        'mode': 'lines',
        'line': dict(width=1, color='green')
    }, 1, 2)

    fig.append_trace({
        'x': data['time'],
        'y': data['Blue Sensor 1'],
        'name': 'Blue Sensor 1',
        'mode': 'lines',  # 'lines+markers',
        'line': dict(width=1, color='blue')
    }, 1, 3)

    fig.append_trace({
        'x': data['time'],
        'y': data['Red Sensor 2'],
        'name': 'Red Sensor 2',
        'mode': 'lines',

        'line': dict(width=1, color='red')
    }, 2, 1)

    fig.append_trace({
        'x': data['time'],
        'y': data['Green Sensor 2'],
        'name': 'Green Sensor 2',
        'mode': 'lines',
        'line': dict(width=1, color='green')
    }, 2, 2)

    fig.append_trace({
        'x': data['time'],
        'y': data['Blue Sensor 2'],
        'name': 'Blue Sensor 2',
        'mode': 'lines',
        'line': dict(width=1, color='blue')
    }, 2, 3)

    fig.append_trace({
        'x': data['time'],
        'y': data['Red Sensor 3'],
        'name': 'Red Sensor 3',
        'mode': 'lines',

        'line': dict(width=1, color='red')
    }, 3, 1)

    fig.append_trace({
        'x': data['time'],
        'y': data['Green Sensor 3'],
        'name': 'Green Sensor 3',
        'mode': 'lines',
        'line': dict(width=1, color='green')
    }, 3, 2)

    fig.append_trace({
        'x': data['time'],
        'y': data['Blue Sensor 3'],
        'name': 'Blue Sensor 3',
        'mode': 'lines',
        'line': dict(width=1, color='blue')
    }, 3, 3)

    fig.update_yaxes(range=[0, 255], dtick=30)
    fig.update_layout(height=1200, width=1900, template='plotly_dark')
    return fig


#executor = ThreadPoolExecutor(max_workers=1)
#executor.submit(update_data)
app = DispatcherMiddleware(server, {
    '/dash1': dashApp.server,
})
if __name__ == '__main__':
    @server.route('/DigiGene')
    def render_dashboard():
        return redirect('/dash1')


    run_simple('127.0.0.32', 5000, app, use_reloader=True, use_debugger=True)
