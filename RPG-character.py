full_dot = '●'
empty_dot = '○'

# Function to validate character_name
def validate_character_name(character_name):
    if not isinstance(character_name, str):
        return 'The character name should be a string'
    elif len(character_name) > 10:
        return 'The character name is too long'
    elif character_name.find(' ') != -1:
        return 'The character name should not contain spaces'
    elif len(character_name) == 0:
        return 'The character should have a name'

# Function create character
def create_character (character_name, character_strength, character_intelligence, character_charisma):
    # Call function to validate character_name
    character_name_msg_error = validate_character_name(character_name)
    #check if character name is valid and return err
    if character_name_msg_error != None:
        return character_name_msg_error
    # check if stats variables are valid
    if not (isinstance(character_strength, int) and isinstance(character_intelligence, int) and isinstance(character_charisma, int)):
        return 'All stats should be integers'
    elif (character_strength < 1 or character_intelligence < 1 or character_charisma < 1):
        return 'All stats should be no less than 1'
    elif (character_strength > 4 or character_intelligence > 4 or character_charisma > 4):
        return 'All stats should be no more than 4'   
    elif (character_strength + character_intelligence + character_charisma) != 7:
        return 'The character should start with 7 points'  
    # Set result_to_print string to empty   
    result_to_print = ''
    # Fill first line of result_to_print (character_name)
    result_to_print += character_name + "\n"
    # Fill second line of result_to_print (stat strenght)
    result_to_print += 'STR ' + "".join([full_dot]*character_strength) + "".join([empty_dot]*(10-character_strength)) + "\n"
    # Fill third line of result_to_print (stat intelligence)
    result_to_print += 'INT ' + "".join([full_dot]*character_intelligence) + "".join([empty_dot]*(10-character_intelligence)) + "\n"
    # Fill fourth line of result_to_print (stat charisma)
    result_to_print += 'CHA ' + "".join([full_dot]*character_charisma) + "".join([empty_dot]*(10-character_charisma))
    return result_to_print

# print in consoloe the function result
print (create_character('Juan', 1, 2, 4))
