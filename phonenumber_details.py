from phonenumbers import carrier
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import timezone

note = 'Phone number format : (+Countrycode)xxxxxxxxxx'
print(note)
number = input("Enter the phone number : ")


# parsing the String to Phone number
try:
    number = phonenumbers.parse(number, None)

    # Checking the possibility of the number``
    if not phonenumbers.is_possible_number(number):
        print('Invalid phone number.')

    # Validating the phone number
    if not phonenumbers.is_valid_number(number):
        print('Invalid phone number.')

    # Checking if the number is associated with a certain region in the country to which it belongs
    if not phonenumbers.is_number_geographical(number):
        print('This number does not belongs to any region in the country.')
except Exception:
    print('Given number is not considered to be a viable phone number (e.g. too few or too many digits) or if no default region was supplied and the number is not in international format (does not start with +).'
          )
    print("Enter a valid phone number.")

else:
    print('Countrycode : ', number.country_code)
    print('National number : ', number.national_number)
    print('International format : ', phonenumbers.format_number(
        number, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
    print('National format : ', phonenumbers.format_number(
        number, phonenumbers.PhoneNumberFormat.NATIONAL))

    # returns the location that corresponds to given phone number
    region = geocoder.description_for_valid_number(number, 'en')
    region_code = phonenumbers.region_code_for_number(number)
    print(f'Country : {region} ({region_code})')

    # returns the list of time zone names that the number potentially belongs to
    time_zone = timezone.time_zones_for_number(number)
    print("Time Zone : ", time_zone)

    # returns the name of the network/carrier who originally owned the given  phone number
    network = carrier.name_for_number(number, 'en')
    print("Network : ", "None" if network == '' else network)
    