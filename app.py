import streamlit as st
import pandas as pd
import app_constants as aconst
from shapash.utils.load_smartpredictor import load_smartpredictor
import plotly.express as px

st.set_page_config(
	page_title="House Price Predictor App",
	page_icon=":house:",
	initial_sidebar_state="expanded",
)

def roundup(x):
	return x if x % 1000 == 0 else x + 1000 - x % 1000

@st.cache
def import_files():
	osm_count = pd.read_csv('./data/prod_osm_count.csv')
	population = pd.read_csv('./data/prod_population.csv')
	master = pd.read_csv('./data/prod_master.csv')
	geo = pd.read_csv('./data/prod_geo.csv')
	return osm_count, population, master, geo

st.title('German House Price Predictor')
	
#import model
predictor_load = load_smartpredictor('./model/predictor202104111025.pkl')

#import necessary files
osm_count, population, master, geo = import_files()

#create UI objects
st.sidebar.markdown('## Choose characteristics:')
geo_plz = int(st.sidebar.text_input('Postcode', value=63110))
obj_data = {}

for list_name, list_values in aconst.input_lists.items():
	obj_data[list_name] = st.sidebar.selectbox(aconst.feature_dict[list_name], list(list_values[1].keys()), index=list_values[0], key=list_name)
for slider_name, slider_values in aconst.input_sliders.items():
	obj_data[slider_name] = st.sidebar.slider(aconst.feature_dict[slider_name], key=slider_name, min_value=slider_values[0], max_value=slider_values[1], value=slider_values[2])
for check_name, check_value in aconst.input_checks.items():
	obj_data[check_name] = st.sidebar.checkbox(aconst.feature_dict[check_name], value=check_value, key=check_name)

obj_data['obj_energyEfficiencyClass'] = aconst.energy_rating_mapping[aconst.obj_energyEfficiencyClass_mapping[obj_data['obj_energyEfficiencyClass']]]
obj_data['obj_condition'] = aconst.condition_mapping[aconst.obj_condition_mapping[obj_data['obj_condition']]]
obj_data['obj_interiorQual'] = aconst.interior_condition_mapping[aconst.obj_interiorQual_mapping[obj_data['obj_interiorQual']]]
obj_data['obj_heatingType'] = aconst.heating_mapping[aconst.obj_heatingType_mapping[obj_data['obj_heatingType']]]
obj_data['obj_buildingType'] = aconst.building_type_mapping[aconst.obj_buildingType_mapping[obj_data['obj_buildingType']]]
obj_data['obj_courtage'] = False

macro_data = pd.merge(pd.merge(pd.merge(osm_count, master, on="geo_plz"), geo, on="geo_plz"), population, on="geo_plz")
macro_data['density'] = macro_data['einwohner'] / (macro_data['area'] * 1000)
macro_data = macro_data[macro_data['geo_plz'] == geo_plz].to_dict(orient='records')[0]
data_to_predict = {**obj_data, **macro_data}
data_to_predict = {x:data_to_predict[x] for x in data_to_predict if x in aconst.feature_dict}
#print(data_to_predict)
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
	color_discrete_sequence=px.colors.qualitative.Set2[1:])
fig.layout.update(showlegend=False, plot_bgcolor='rgb(252,252,252)')
fig.update_xaxes(showgrid=True, gridwidth=2, gridcolor='rgb(200,200,200)')
fig.update_traces(
    hovertemplate='€%{x:.0f}')
st.plotly_chart(fig, use_container_width=True)
