import datetime
import flask
from flask import render_template
import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly import subplots
from dash.dependencies import Input, Output
import dash_bootstrap_components as  dbc
import http.client
import json


external_stylesheets = [
    'https://github.com/Owaiskhan9654/DigiGene/blob/bdf66f620f8b75b59f7a4e4687508ec908b9a6c8/DigiGene.css']


server = flask.Flask(__name__)

@server.route('/')
def index():
    #var = 'data'
    #g = globals()
    #if var in g: del g[var]
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


    return render_template('index1.html')

app  = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],title="DigiGene Live Feed Web Based Data Analysis Application",
    server=server,
    routes_pathname_prefix='/DigiGene/')
app._favicon = "favico.ico"
red_button_style = {'background-color': 'red',
                    'color': 'white',
                    'height': '50px',
                    'width': '100px',
                    'margin-top': '50px',
                    'margin-left': '50px',
                    'borderRadius': '15px'}

company_logo = html.A(dbc.CardImg(src="assets/images/faster_Canary_logo_White-animation.gif", top=True, className='image_link'), href='https://www.canarydetect.com/', target="_blank", className='image_1')
company_logo_footer = html.A(dbc.CardImg(src="assets/images/faster_Canary_logo_White-animation.gif", top=True, className='image_link_footer'), href='https://www.canarydetect.com/', target="_blank", className='image_link_footer')

profile_links_top = dbc.Row([dbc.Col(company_logo, width=20, className='link_col'),], className='link_icons')

heading = html.Div(dbc.Row([dbc.Col(html.H3("Canary DigiGene Sensor Dashboard for Deep Analysis ( Compatible with "
                                            "desktop)", className='page_title'), width=8, className='header_col1'),
                            dbc.Col(profile_links_top, width=4, className='header_col2')],
                            className='header_container'))


footer = html.Div(dbc.Row([company_logo_footer], className='footer_container'))
footer_1 = html.Div(dbc.Row([dcc.Markdown(" Saving Lives Through Early Disease Detection" ,className='footer_container_line')], className='footer_container'))


text_1 = dcc.Markdown('''Data is fetched Live Through DigiGene Device''')
text_2 = dcc.Markdown('''This DigiGene Device is build by our Electronics Team and Research Scientists''')
text_3 = dcc.Markdown('''Canary Global Inc. ([Canary](https://www.canarydetect.com/)) is a medical technology company 
that builds revolutionary diagnostic platforms and services. Combined with AI-powered intelligence, 
Canary’s nano-sensor technology can detect diseases, characterize the nature and location of cancers, and predict and 
monitor responses to therapy.Canary technology is based on robust science derived from decades of published research, 
cutting-edge digital technology and a flexible platform design to enable multiple uses including disease diagnosis 
and precision medicine''')
text_4 = dcc.Markdown("Our mission is to save lives and help conquer Covid, Cancer and other life-threatening conditions. With our breath and liquid testing platforms,"
                      " we can predict disease risk, identify and characterize presence of disease, and track and monitor responses to therapies and medications.")
text_5 = dcc.Markdown("Our team works with key opinion leaders, clinicians, regulatory experts, data scientists and commercial partners to design the most rigorous"
                      " and fastest pathway to develop the products so patients and their doctors can use them to improve and save lives.Canary Global Inc. wants"
                      " to change healthcare and make safe and accurate rapid testing accessible. ")

text_6 = dcc.Markdown("All viruses, including SARS-CoV-2, the virus that causes COVID-19, change over time. Most changes have little to no impact on the virus’ "
                      "properties. However, some changes may affect the virus’s properties, such as how easily it spreads, the associated disease severity, or "
                      "the performance of vaccines, therapeutic medicines, diagnostic tools, or other public health and social measures")

text_8 = dcc.Markdown(" A [team](https://www.canarydetect.com/about) built around globally-diverse industry experience, sharing a common passion for out the box "
                      "thinking and a drive towards making diagnostic health services widely accessible.  ")
text_9 = dcc.Markdown("For more information about Canary Global Inc.’s products and services or to speak with someone from our team, please "
                      "[contact](https://www.canarydetect.com/contact) us. ")
summary = dbc.Row(dbc.Col(dbc.Card(dbc.CardBody([
                                    html.Div('About this Medical Company', className='ques'),
                                    html.Div(text_3, className='ans'),
                                    html.Hr(style={'borderColor': 'white', 'border': '1.5'}),
                                    html.Div('Mission', className='ques'),
                                    html.Div(text_4, className='ans'),
                                    html.Hr(style={'borderColor': 'white', 'border': '1.5'}),
                                    html.Div('Our Vision', className='ques'),
                                    html.Div(text_5, className='ans'),
                                    html.Hr(style={'borderColor': 'white', 'border': '1.5'}),
                                    html.Div('Our Team', className='ques'),
                                    html.Div(text_8, className='ans'),
                                    html.Hr(style={'borderColor': 'white', 'border': '1.5'}),
                                    html.Div('About DigiGene Sensor Dashboard  BY CANARY GLOBAL INC.', className='ques'),
                                    html.Div(text_2, className='ans'),
                                    html.Hr(style={'borderColor': 'white', 'border': '1.5'}),
                                    html.Div('Source of the Sensor data:', className='ques'),
                                    html.Div(text_1, className='ans'),
                                    html.Hr(style={'borderColor': 'white', 'border': '1.5'}),
                                    html.Div('Contact Us', className='ques'),
                                    html.Div(text_9, className='ans'),
                                    html.Hr(style={'borderColor': 'white', 'border': '1.5'}),
                                    ]), className='figure_summary'), className='figure_rows'),style={'padding': '25px'} )








app.layout = html.Div(children=[
    heading,
    html.Div([

        html.Div(id='live-update-text', style={'padding': '5px', 'fontSize': '16px', 'textAlign': 'center',
                                               'backgroundColor': 'rgb(17, 17, 17)', 'color': 'white'}),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1 * 5000,  # in milliseconds
            n_intervals=0
        )
    ], style={'padding': '25px',}),summary,footer,
footer_1]
)


def rgb_to_hex(r, g, b):
    return ('{:x}{:x}{:x}').format(r, g, b)


@app.callback(Output('live-update-text', 'children'),
              Input('interval-component', 'n_intervals'))
def update_metrics(n):
    print(n)
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
    Current_color = data_pantry["Current"]

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

    max_sensor1 = max(RedSensor1,GreenSensor1,BlueSensor1)
    max_sensor2 = max(RedSensor2, GreenSensor2, BlueSensor2)
    max_sensor3 = max(RedSensor3, GreenSensor3, BlueSensor3)
    if (max_sensor1 == RedSensor1):
        hue1=(1/6) * (GreenSensor1-BlueSensor1)/RedSensor1

    elif (max_sensor1 == GreenSensor1):
        hue1=(1/3) +1/6*(BlueSensor1-RedSensor1)/GreenSensor1

    elif (max_sensor1 == BlueSensor1):
        hue1 = (2/3) +1/6*(RedSensor1-GreenSensor1)/BlueSensor1

    if (max_sensor2 == RedSensor2):
        hue2=(1/6) * (GreenSensor2-BlueSensor2)/RedSensor2

    elif (max_sensor2 == GreenSensor2):
        hue2=(1/3) +1/6*(BlueSensor2-RedSensor2)/GreenSensor2

    elif (max_sensor2 == BlueSensor2):
        hue2 = (2/3) +1/6*(RedSensor2-GreenSensor2)/BlueSensor2


    if (max_sensor3 == RedSensor3):
        hue3=(1/6) * (GreenSensor3-BlueSensor3)/RedSensor3

    elif (max_sensor3 == GreenSensor3):
        hue3=(1/3) +1/6*(BlueSensor3-RedSensor3)/GreenSensor3

    elif (max_sensor3 == BlueSensor3):
        hue3 = (2/3) +1/6*(RedSensor3-GreenSensor3)/BlueSensor3


    # print('RedSensor1 ',Current_color[0],'GreenSensor1 ',Current_color[1],'BlueSensor1 ', Current_color[2])
    Sensor1_name = '#' + rgb_to_hex(RedSensor1, GreenSensor1, BlueSensor1)
    Sensor2_name = '#' + rgb_to_hex(RedSensor2, GreenSensor2, BlueSensor2)
    Sensor3_name = '#' + rgb_to_hex(RedSensor3, GreenSensor3, BlueSensor3)
    style = { 'fontSize': '24px', 'textAlign': 'center', 'backgroundColor': 'rgb(17, 17, 17)',
             'color': 'white'}
    return [

        html.Span('DIGIGene Live Feed Web Based Data Analysis Application', style=style),
        html.Br(),
        html.Span('Sensor 1:  Red {0:.2f}, Sensor 1: Green {1:.2f}, Sensor 1: Blue {2:.2f}, Green1/Blue1: {3:.2f},\
        Blue1/Red1: {4:.2f}, Hue Sensor 1 {5:.2f} '.format(RedSensor1, GreenSensor1, BlueSensor1, GreenSensor1 / BlueSensor1,
                                    BlueSensor1 / RedSensor1, hue1)
                  , style=style),
        html.Br(),
        html.Span('Sensor 2: Red {0:.2f} , Sensor 2: Green {1:.2f}, Sensor 2: Blue {2:.2f},Green2/Blue2: {3:.2f},\
        Blue2/Red2: {4:.2f} Hue Sensor 2 {5:.2f}'.format(RedSensor2, GreenSensor2, BlueSensor2, GreenSensor2 / BlueSensor2,
                                                         BlueSensor2 / RedSensor2, hue2),
                  style=style)
        , html.Br(),
        html.Span('Sensor 3: Red {0:0.2f} , Sensor 3: Green {1:.2f}, Sensor 3: Blue {2:.2f}, Green3/Blue3: {3:.2f},\
        Blue3/Red3: {4:.2f}, Hue Sensor 3 {5:.2f}'.format(RedSensor3, GreenSensor3, BlueSensor3, GreenSensor3 / BlueSensor3,
                                                          BlueSensor3 / RedSensor3,hue3 ),
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
                                     'textAlign': 'center', 'borderRadius': '15px', }, className='col s6 m6', )],

                 ),
        html.A(html.Button('Reset Plots',style=red_button_style), href='/'),
    ]


# '+str(int(RedSensor1))+','+str(int(GreenSensor1))+ ','+str(int(BlueSensor1))+'

# Multiple components can update everytime interval gets fired.
global data
data= {
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


@app.callback(Output('live-update-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_graph_live(n):


    conn = http.client.HTTPSConnection("getpantry.cloud")
    payload = ''
    headers = {
            'Content-Type': 'application/json'
        }
    # Collect some data
    #for i in range(1):
    #time = datetime.datetime.now() - datetime.timedelta(seconds=i * 3)
    # Current_color = open("Current_color.txt","r")
    # Current_color= Current_color.readlines()
    # print(Current_color)

    conn.request("GET", "/apiv1/pantry/2cb1189d-f1e5-4acb-8fba-c86b8282f25f/basket/DigiGeneV1", payload, headers)
    res = conn.getresponse()
    data_pantry = res.read()

    data_pantry = json.loads(data_pantry.decode('utf-8'))
    Current_color = data_pantry["Current"]
    time = data_pantry["Counter"]
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
    #try:
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
        
    #except:
    #    data= {
     #       'time': [],
      #      'Red Sensor 1': [],
       #     'Green Sensor 1': [],
       #     'Blue Sensor 1': [],
       #     'Red Sensor 2': [],
       #     'Green Sensor 2': [],
      #      'Blue Sensor 2': [],
       #     'Red Sensor 3': [],
       #     'Green Sensor 3': [],
       #     'Blue Sensor 3': [],
       # }

    # Create the graph with subplots
    fig = subplots.make_subplots(rows=1, cols=3, vertical_spacing=0.2, subplot_titles=[
        'Red,Green,Blue Values for Sensor 1',
        #'Green Sensor 1',
        #'Blue Sensor 1',
        'Red,Green,Blue Values for Sensor 2',
        #'Green Sensor 2',
        #'Blue Sensor 2',
        'Red,Green,Blue Values for Sensor 3',
        #'Green Sensor 3',
        #'Blue Sensor 3',
    ], )
    fig['layout']['margin'] = {'l': 80, 'r': 10, 'b': 90, 't': 60}
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
        'line': dict(width=1, color='Red')}, 1, 1)

    fig.append_trace({
        'x': data['time'],
        'y': data['Green Sensor 1'],
        'name': 'Green Sensor 1',
        'mode': 'lines',
        'line': dict(width=1, color='green')}, 1, 1)

    fig.append_trace({
        'x': data['time'],
        'y': data['Blue Sensor 1'],
        'name': 'Blue Sensor 1',
        'mode': 'lines',  # 'lines+markers',
        'line': dict(width=1, color='blue')}, 1, 1)

    fig.append_trace({
        'x': data['time'],
        'y': data['Red Sensor 2'],
        'name': 'Red Sensor 2',
        'mode': 'lines',

        'line': dict(width=1, color='red')
        }, 1, 2)

    fig.append_trace({
            'x': data['time'],
            'y': data['Green Sensor 2'],
            'name': 'Green Sensor 2',
            'mode': 'lines',
            'line': dict(width=1, color='green')
        }, 1, 2)

    fig.append_trace({
            'x': data['time'],
            'y': data['Blue Sensor 2'],
            'name': 'Blue Sensor 2',
            'mode': 'lines',
            'line': dict(width=1, color='blue')
        }, 1, 2)

    fig.append_trace({
            'x': data['time'],
            'y': data['Red Sensor 3'],
            'name': 'Red Sensor 3',
            'mode': 'lines',

            'line': dict(width=1, color='red')
        }, 1, 3)

    fig.append_trace({
            'x': data['time'],
            'y': data['Green Sensor 3'],
            'name': 'Green Sensor 3',
            'mode': 'lines',
            'line': dict(width=1, color='green')
        }, 1, 3)

    fig.append_trace({
            'x': data['time'],
            'y': data['Blue Sensor 3'],
            'name': 'Blue Sensor 3',
            'mode': 'lines',
            'line': dict(width=1, color='blue')
        }, 1, 3)

    fig.update_yaxes(range=[0, 255], dtick=60)
    fig.update_layout(template='plotly_dark',height=400)#height=300, width=1800, x_title='Time Counter(sec)',y_title='RGB Value',
    for i in range(1, 4):
        fig['layout']['xaxis{}'.format(i)]['title'] = 'Time Counter(sec)'
        fig['layout']['yaxis{}'.format(i)]['title'] = 'RGB Value'
    return fig

if __name__ == '__main__':
    app.server.run(debug=True, threaded=True)


