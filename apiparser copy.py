import requests
from nltk.tokenize import RegexpTokenizer

def main():
    profFirstName = "Lauren"
    profLastName = "White"

    response = requests.get(
        'https://uscdirectory.usc.edu/web/directory/faculty-staff/proxy.php',
        params={'basic': f"{profFirstName} {profLastName}"} ,
        headers={'X-Requested-With': 'XMLHttpRequest'} ,
    )

    resp = response
    print("Status:", resp.status_code)
    print("Content-Type:", resp.headers.get("Content-Type"))
    # print("Length:", len(resp.text))
    # print(resp.json())
    data = resp.json()
    if type(data) is list:
        for person in data:
            print(person)
            tokenizer = RegexpTokenizer(r'\w+')
            name_set = set(tokenizer.tokenize(person['cn'][0]))
            if profFirstName in name_set and profLastName in name_set:
                print(person['displayname'])
    else:
        print(data['displayname'])
        # print(data)
    
if __name__ == "__main__":
    main()