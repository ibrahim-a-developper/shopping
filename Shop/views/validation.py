
def validationCustomer(customer):
    # validation
    error_message = None
    if (not customer.first_name):
        error_message = 'First name required'
    elif (len(customer.first_name) < 4):
        error_message = 'First name must 4 char long or more'
    if (not customer.last_name):
        error_message = 'Last name required'
    elif (len(customer.last_name) < 4):
        error_message = 'Last name must 4 char long or more'
    if (not customer.phone):
        error_message = 'Phone name required'
    elif (len(customer.phone) < 4):
        error_message = 'Phone name must 4 char long or more'
    elif (len(customer.password) < 6):
        error_message = 'Password name must 6 char long or more'
    elif customer.isExists():
        error_message = "Email adesse has exist"
    return error_message

# def validator(customer):
#     validate={
#         customer.first_name: 'required|min:4',
#     }

