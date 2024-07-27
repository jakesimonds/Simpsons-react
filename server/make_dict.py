
def return_index(string):


    def create_line_dictionary(file_path):
        line_dict = {}
        
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, 1):
                line_dict[line_number] = line.strip()
        
        return line_dict

    # Example usage
    file_path = 'simpsons_opt.txt'  # Replace with your file path
    result = create_line_dictionary(file_path)

    # Print the resulting dictionary
    for key, value in result.items():
        if string in value:
            return key
    
    #print(f"{key}: '{value}'")
    
num = return_index('Artie Ziff: Wealthy, Marge’s ex-boyfriend, inventor, Artie, obsessive, nerdy, jealous, entrepreneur, Springfield.')

print(num)