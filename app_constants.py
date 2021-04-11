feature_dict = {
    'obj_yearConstructed': 'Year Constructed',
    'obj_cellar': 'Has Cellar',
    'obj_livingSpace': 'Living Area',
    'obj_noRooms': 'Number of Rooms',
    'obj_condition': 'Building Condition',
    'obj_heatingType': 'Heating Type',
    'obj_noParkSpaces': 'Number of Parking Spaces',
    'obj_lotArea': 'Plot Area',
    'obj_courtage': 'Courtage',
    'obj_energyEfficiencyClass': 'Energy Efficiency Class',
    'obj_interiorQual': 'Interior Quality',
    'obj_buildingType': 'Building Type',
    'bus_count': 'Number of Bus Stops',
    'food_count': 'Number of Restaurants',
    'gdp_per_hab': 'GDP per Habitant',
    'airport_distance': 'Distance to Closet International Airport',
    'child_pop': 'Child Age Population',
    'retired_pop': 'Retirement Age Population',
    'residencial_building_per_qkm': 'Residential Buildings/km2',
    'wage_per_per': 'Wage per Habitant',
    'percent_floor_area_traffic': 'Percent Traffic Area',
    'percent_floor_use_industry_commerce': 'Percent Industry/Commerce Area',
    'percent_floor_use_leisure': 'Percent Leisure Area',
    'density': 'Population Density',
    'ppl_per_building': 'Habitants per Building',
    'highrise_factor': 'High Rise Factor',
    'distance': 'Distance to Closest Large City',
    'new_apartment_permit_per_hab': 'New Aprt Permits per Habitant',
}

obj_buildingType_mapping = {
	'Villa': 'villa',
	'Multi-family House': 'multi_family_house',
	'Special Real Estate': 'special_real_estate',
	'End Terrace House': 'end_terrace_house',
	'Semidetached House': 'semidetached_house',
	'Castle/Manor': 'castle_manor_house',
	'Single Family House': 'single_family_house',
	'Middle Terrace House': 'mid_terrace_house',
	'Bungalow': 'bungalow',
	'Other': 'other_real_estate',
	'Farmhouse': 'farmhouse',
}

obj_energyEfficiencyClass_mapping = {
	'A+': 'A_PLUS',
	'A': 'A',
	'B': 'B',
	'C': 'C',
	'D': 'D',
	'E': 'E',
	'F': 'F',
	'G': 'G',
	'H': 'H',
}

obj_interiorQual_mapping = {
	'Luxurious': 'luxury',
	'Sophisticated': 'sophisticated',
	'Normal': 'normal',
	'Simple': 'simple',
}

obj_condition_mapping = {
	'Mint Condition': 'mint_condition',
	'First Time Use': 'first_time_use',
	'Modernised': 'modernized',
	'Well Kept': 'well_kept',
	'First Time Use (after refurbishment)': 'first_time_use_after_refurbishment',
	'Fully Renovated': 'fully_renovated',
	'Refurbished': 'refurbished',
	'In Need of Renovation': 'need_of_renovation',
	'Ripe for Demolition': 'ripe_for_demolition',
}

obj_heatingType_mapping = {
	'Floor': 'floor_heating',
	'Heat Pump': 'heat_pump',
	'District': 'district_heating',
	'Combined Heat and Power Plant': 'combined_heat_and_power_plant',
	'Wood Pellet': 'wood_pellet_heating',
	'Solar': 'solar_heating',
	'Central': 'central_heating',
	'Gas': 'gas_heating',
	'Oil': 'oil_heating',
	'Self Contained Central Heating': 'self_contained_central_heating',
	'Electric': 'electric_heating',
	'Night Storage': 'night_storage_heater',
	'Stove': 'stove_heating',
}

input_lists = {
	'obj_buildingType': [6, obj_buildingType_mapping],
	'obj_heatingType': [6, obj_heatingType_mapping],
	'obj_condition': [7, obj_condition_mapping],
	'obj_interiorQual': [2, obj_interiorQual_mapping],
	'obj_energyEfficiencyClass': [4, obj_energyEfficiencyClass_mapping],
}

input_sliders = {
	'obj_yearConstructed': (1960, 2021, 1980),
	'obj_livingSpace': (30, 300, 100),
	'obj_lotArea': (0, 900, 450),
	'obj_noRooms': (1, 8, 4),
	'obj_noParkSpaces': (0, 5, 1),	
}

input_checks = {
	'obj_cellar': True,
}

#macro_cols = ['bus_count', 'food_count', 'gdp_per_hab',
#	'doctor_count', 'child_pop', 'working_pop', 'retired_pop', 'residencial_building_per_qkm',
#	'percent_employed', 'wage_per_per', 'percent_floor_area_traffic',
#	'percent_floor_area_vegetation', 'percent_floor_use_residential',
#	'percent_floor_use_industry_commerce', 'percent_floor_use_leisure', 'density',
#	'ppl_per_building', 'highrise_factor', 'distance', 'new_apartment_permit_per_hab']

HOUSE_PRICE_INDEX = 1.08

energy_rating_mapping = {
	'A_PLUS': 59,
	'A': 57,
	'B': 56,
	'C': 55,
	'D': 53,
	'E': 51,
	'F': 48,
	'G': 44,
	'H': 20
}
						 
condition_mapping = {
	'mint_condition': 63,
	'first_time_use': 54,
	'modernized': 53,
	'well_kept': 52,
	'first_time_use_after_refurbishment': 51,
	'fully_renovated': 50,
	'refurbished': 49,
	'need_of_renovation': 37,
	'ripe_for_demolition': 0,
}

interior_condition_mapping = {
	'luxury': 62,
	'sophisticated': 48,
	'no_information': 36,
	'normal': 36,
	'simple': 22
}

building_type_mapping = {
    'villa': 58,
    'multi_family_house': 44,
    'special_real_estate': 43,
    'end_terrace_house': 41,
    'semidetached_house': 40,
    'no_information': 40,
    'castle_manor_house': 39,
    'single_family_house': 38,
    'mid_terrace_house': 37,
    'bungalow': 35,
    'other_real_estate': 30,
    'farmhouse': 27,
}

heating_mapping = {
	'floor_heating': 59,
	'heat_pump': 58,
	'district_heating': 56,
	'combined_heat_and_power_plant': 54,
	'wood_pellet_heating': 51,
	'solar_heating': 50,
	'central_heating': 49,
	'gas_heating': 48,
	'oil_heating': 47,
	'self_contained_central_heating': 46,
	'electric_heating': 41,
	'night_storage_heater': 40,
	'stove_heating': 0,
}
		  
if __name__ == '__main__':
    print("should be used as import")
