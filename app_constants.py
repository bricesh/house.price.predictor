feature_dict = {
	'obj_heatingType': 'Heating Type',
	'obj_condition': 'Building Condition',
	'obj_buildingType': 'Building Type',
	'obj_energyEfficiencyClass': 'Energy Efficiency Class',
	'obj_interiorQual': 'Interior Quality',
	'obj_yearConstructed': 'Year Constructed',
	'obj_cellar': 'Has Cellar',
	'obj_livingSpace': 'Living Area',
	'obj_noRooms': 'Number of Rooms',
	'obj_noParkSpaces': 'Number of Parking Spaces',
	'obj_lotArea': 'Plot Area',
	'obj_courtage': 'Courtage',
	'bus_count': 'Number of Bus Stops',
	'food_count': 'Number of Restaurants',
	'gdp_per_hab': 'GDP per Habitant',
	'doctor_count': 'Number of Doctors',
	'child_pop': 'Child Age Population',
	'working_pop': 'Working Age Population',
	'retired_pop': 'Retirement Age Population',
	'residencial_building_per_qkm': 'Residential Buildings/km2',
	'percent_employed': 'Percent of Population Employed',
	'wage_per_per': 'Wage per Habitant',
	'percent_floor_area_traffic': 'Percent Traffic Area',
	'percent_floor_area_vegetation': 'Percent Vegetation Area',
	'percent_floor_use_residential': 'Percent Residential Area',
	'percent_floor_use_industry_commerce': 'Percent Industry/Commerce Area',
	'percent_floor_use_leisure': 'Percent Leisure Area',
	'density': 'Population Density',
	'ppl_per_building': 'Habitants per Building',
	'highrise_factor': 'High Rise Factor',
	'distance': 'Distance to Closest Large City',
	'new_apartment_permit_per_hab': 'New Aprt Permits per Habitant'
}

obj_buildingType_mapping = {
	'Bungalow': 'bungalow',
	'Castle/Manor': 'castle_manor_house',
	'End Terrace House': 'end_terrace_house',
	'Farmhouse': 'farmhouse',
	'Middle Terrace House': 'mid_terrace_house',
	'Multi-family House': 'multi_family_house',
	'Other': 'other_real_estate',
	'Semidetached House': 'semidetached_house',
	'Single Family House': 'single_family_house',
	'Special Real Estate': 'special_real_estate',
	'Villa': 'villa',
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
	'Luxury': 'luxurious',
	'Normal': 'normal',
	'Simple': 'simple',
	'Sophisticated': 'sophisticated',
}

obj_condition_mapping = {
	'First Time Use': 'first_time_use',
	'First Time Use (after refurbishment)': 'first_time_use_after_refurbishment',
	'Fully Renovated': 'fully_renovated',
	'In Need of Renovation': 'need_of_renovation',
	'Mint Condition': 'mint_condition',
	'Modernised': 'modernized',
	'Refurbished': 'refurbished',
	'Ripe for Demolition': 'ripe_for_demolition',
	'Well Kept': 'well_kept',
}

obj_heatingType_mapping = {
	'Heat Pump': 'heat_pump',
	'Gas': 'gas_heating',
	'Central': 'central_heating',
	'Floor': 'floor_heating',
	'Electric': 'electric_heating',
	'Stove': 'stove_heating',
	'Oil': 'oil_heating',
	'Self Contained Central Heating': 'self_contained_central_heating',
	'Night Storage': 'night_storage_heater',
	'District': 'district_heating',
	'Combined Heat and Power Plant': 'combined_heat_and_power_plant',
	'Wood Pellet': 'wood_pellet_heating',
	'Solar': 'solar_heating',
}

input_lists = {
	'obj_buildingType': [8, obj_buildingType_mapping],
	'obj_heatingType': [2, obj_heatingType_mapping],
	'obj_condition': [3, obj_condition_mapping],
	'obj_interiorQual': [1, obj_interiorQual_mapping],
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
	#'obj_courtage': False,
	'obj_cellar': True,
}

macro_cols = ['bus_count', 'food_count', 'gdp_per_hab',
	'doctor_count', 'child_pop', 'working_pop', 'retired_pop', 'residencial_building_per_qkm',
	'percent_employed', 'wage_per_per', 'percent_floor_area_traffic',
	'percent_floor_area_vegetation', 'percent_floor_use_residential',
	'percent_floor_use_industry_commerce', 'percent_floor_use_leisure', 'density',
	'ppl_per_building', 'highrise_factor', 'distance', 'new_apartment_permit_per_hab']

HOUSE_PRICE_INDEX = 1.1

energy_rating_mapping = {'A_PLUS': 9,
                         'A': 8,
                         'B': 7,
                         'C': 6,
                         'D': 5,
                         'E': 4,
                         'F': 3,
                         'G': 2,
                         'H': 1}

condition_mapping = {'first_time_use': 70,
                     'mint_condition': 55,
                     'first_time_use_after_refurbishment': 45,
                     'modernized': 40,
                     'well_kept': 40,
                     'fully_renovated': 35,
                     'refurbished': 35,
                     'need_of_renovation': 20,
                     'ripe_for_demolition': 0,
                     }

interior_condition_mapping = {'luxury': 6,
                              'sophisticated': 4,
                              'normal': 2,
                              'simple': 1}

heating_mapping = {'floor_heating': 55,
                   'district_heating': 52,
                   'combined_heat_and_power_plant': 51,
                   'solar_heating': 49,
                   'heat_pump': 48,
                   'wood_pellet_heating': 46,
                   'central_heating': 44,
                   'gas_heating': 43,
                   'oil_heating': 43,
                   'self_contained_central_heating': 43,
                   'electric_heating': 32,
                   'night_storage_heater': 31,
                   'stove_heating': 0,
                  }
				  
if __name__ == '__main__':
    print("should be used as import")
