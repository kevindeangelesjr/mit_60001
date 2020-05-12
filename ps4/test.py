import string

def build_shift_dict(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.        
    
    shift (integer): the amount by which to shift every letter of the 
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to 
                another letter (string). 
    '''

    letters_list = string.ascii_lowercase
    letters_list_len = len(letters_list)
    
    shift_dict = {}

    if 0 <= shift < 26:
        for letter in letters_list:
            letter_position = letters_list.index(letter)
            shifted_position = letter_position + shift

            if shifted_position >= letters_list_len:
                shifted_position = abs((letters_list_len) - shifted_position)
            
            shifted_letter = letters_list[shifted_position]
            
            shift_dict.update( {letter : shifted_letter} )
            shift_dict.update( {letter.upper() : shifted_letter.upper()} )
    else:
        return
    
    return shift_dict

print(build_shift_dict(25))