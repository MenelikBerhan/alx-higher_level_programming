#!/usr/bin/python3
"""takes in a letter & sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter set to variable 'q'.
If no argument is given, set q="", If the response body is properly JSON
formatted and not empty, display the id and name like this: [<id>] <name>
Otherwise: Display 'Not a valid JSON' if the JSON is invalid
    Display 'No result' if the JSON is empty"""
if __name__ == "__main__":
    import requests
    import sys

    my_data = {'q': "" if len(sys.argv) == 1 else sys.argv[1]}
    response = requests.post('http://0.0.0.0:5000/search_user', data=my_data)
    try:
        my_json = response.json()
        if my_json:
            print("[{}] {}".format(my_json.get('id'), my_json.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
