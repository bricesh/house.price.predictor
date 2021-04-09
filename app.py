import streamlit as st
import pandas as pd
import app_constants as aconst
#import app_helper as ahelp
from shapash.utils.load_smartpredictor import load_smartpredictor
import plotly.express as px

def roundup(x):
	return x if x % 1000 == 0 else x + 1000 - x % 1000

st.title('House Price Predictor')
#import model
predictor_load = load_smartpredictor('./model/predictor.pkl')

#import necessary files
osm_count = pd.read_csv('./data/prod_osm_count.csv')
population = pd.read_csv('./data/prod_population.csv')
master = pd.read_csv('./data/prod_master.csv')
geo = pd.read_csv('./data/prod_geo.csv')

#create UI objects
st.sidebar.markdown('## Set characteristics:')
geo_plz = int(st.sidebar.text_input('Postcode', value=63110))
obj_data = {}
#obj_data['geo_plz'] = geo_plz
for list_name, list_values in aconst.input_lists.items():
	list_values.sort()
	obj_data[list_name] = st.sidebar.selectbox(aconst.feature_dict[list_name], list_values, key=list_name)
for slider_name, slider_values in aconst.input_sliders.items():
	obj_data[slider_name] = st.sidebar.slider(aconst.feature_dict[slider_name], key=slider_name, min_value=slider_values[0], max_value=slider_values[1], value=slider_values[2])
for check_name, check_values in aconst.input_checks.items():
	obj_data[check_name] = st.sidebar.checkbox(aconst.feature_dict[check_name], key=check_name)

obj_data['obj_energyEfficiencyClass'] = aconst.energy_rating_mapping[obj_data['obj_energyEfficiencyClass']]
obj_data['obj_condition'] = aconst.condition_mapping[obj_data['obj_condition']]
obj_data['obj_interiorQual'] = aconst.interior_condition_mapping[obj_data['obj_interiorQual']]
#obj_data['obj_heatingType'] = aconst.heating_mapping[obj_data['obj_heatingType']]
	
macro_data = pd.merge(pd.merge(pd.merge(osm_count, master, on="geo_plz"), geo, on="geo_plz"), population, on="geo_plz")
macro_data['density'] = macro_data['einwohner'] / (macro_data['area'] * 1000)
macro_data = macro_data[macro_data['geo_plz'] == geo_plz][aconst.macro_cols].to_dict(orient='records')[0]
data_to_predict = {**obj_data, **macro_data}
predictor_load.add_input(x=data_to_predict)

detailed_contributions = predictor_load.detail_contributions()
price_pred = roundup(int(detailed_contributions.iloc[0,0] * aconst.HOUSE_PRICE_INDEX))
min_price_pred = price_pred - 85000
max_price_pred = price_pred + 85000


cols = st.beta_columns([1,1,1])
with cols[0]:
	st.write('_€'+str(min_price_pred)+'_')
with cols[1]:
	st.write('__€'+str(price_pred)+'__')
with cols[2]:
	st.write('_€'+str(max_price_pred)+'_')

detailed_contributions = detailed_contributions[list(data_to_predict.keys())].T.sort_values(by=0)
detailed_contributions.columns = ['Feature']
detailed_contributions.rename(aconst.feature_dict, axis='rows', inplace = True)
detailed_contributions['colour'] = detailed_contributions['Feature'].apply(lambda x: ('pos' if x > 0 else 'neg'))
fig = px.bar(detailed_contributions,
	x='Feature',
	orientation='h',
	color='colour',
	labels=dict(Feature = 'Contribution', index=''),
	width=500,
	height=700,
	#hover_name='Feature',
	#hover_data={'colour': True, 'Feature': False},
	color_discrete_sequence=px.colors.qualitative.Set2[1:])
fig.layout.update(showlegend=False, plot_bgcolor='rgb(252,252,252)')
fig.update_xaxes(showgrid=True, gridwidth=2, gridcolor='rgb(200,200,200)')
fig.update_traces(
    #hovertext='{x.index.values}',
    hovertemplate='€%{x:.0f}')
st.plotly_chart(fig, use_container_width=True)
