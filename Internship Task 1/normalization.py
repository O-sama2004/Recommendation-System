from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np

# Define the function to apply Standard scaling
def standard_scale(input_data):
    # Extract numerical values from the list of dictionaries
    numerical_values = [item['value'] for item in input_data if item['type'] == 'numerical']
    
    # Reshape the data for Standard Scaler
    values_reshaped = [[value] for value in numerical_values]
    
    # Apply Standard scaling
    scaler = StandardScaler()
    scaled_values = scaler.fit_transform(values_reshaped)
    
    # Update the original list with the scaled values
    scaled_index = 0
    for item in input_data:
        if item['type'] == 'numerical':
            item['value'] = scaled_values[scaled_index][0]
            scaled_index += 1 
    return input_data

# Define the function to apply Min-Max scaling
def min_max_scale(input_data):
    # Extract numerical values from the list of dictionaries
    numerical_values = [item['value'] for item in input_data if item['type'] == 'numerical']
    
    # Reshape the data for Min-Max Scaler
    values_reshaped = [[value] for value in numerical_values]
    
    # Apply Min-Max scaling
    scaler = MinMaxScaler()
    scaled_values = scaler.fit_transform(values_reshaped)
    
    # Update the original list with the scaled values
    scaled_index = 0
    for item in input_data:
        if item['type'] == 'numerical':
            item['value'] = scaled_values[scaled_index][0]
            scaled_index += 1
    return input_data


# Define the function to apply log transformation to numerical values
def log_transform(input_data):
    # Update the original list with the log-transformed values
    for item in input_data:
        if item['type'] == 'numerical':
            item['value'] = np.log(item['value'] + 1)
    return input_data

# Define a function to get the normalization method based on some criteria
def get_normalization_method(data_type):
    #fill with correct code when task is clearer
    
    return min_max_scale



# Example usage
input_data = [
    {"value": 123456, "type": "numerical"},
    {"value": 500, "type": "numerical"},
    {"value": "Some Text", "type": "text"}  # Non-numerical data ignored
]

normalization_method = get_normalization_method(input_data)
normalization_method(input_data)

print(input_data)

