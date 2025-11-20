import requests

cookies = {
    'WWTRBQJP': '0297a45327-1bed-4ffGPmeNchPbrTtBNJT1yqczXT_5RPMzxuaRET2irzZavLOnbyhEILAiH_SfbRfnSt8gA',
    '_shibstate_1761107688_06bd': 'https%3A%2F%2Fuscdirectory.usc.edu%2Fweb%2Fdirectory%2Fstudent%2F',
    'cf_clearance': 'xlgENcTR5E21yCoZLAQwOdJ46abiatGvEf314vlDLDE-1761108020-1.2.1.1-BmWu1rsrKtpXbLHcXnUeyBcEE_Ayd6fic4xUaEut4IZiubhEigYOf5D7cFqcCKzXhCh8wdUygQ7G84uSDomFuSmjxNlpqDertC_riKcEfDP8t.Hb0cf2Is5PkWIS_nUWj5VuvzTjV2Xozhy7qu3hNt2GmZ90QmXrlMgamXN4ZqsFFHpqsJ0gXRBYxGEK8vB9uOLkACI11ftR2uknsCqqnQ2VgcM2LslFmacFf9VcZZM',
}

headers = {
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Pragma': 'no-cache',
    'Referer': 'https://uscdirectory.usc.edu/web/directory/faculty-staff/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="141", "Not?A_Brand";v="8"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    # 'Cookie': 'WWTRBQJP=0297a45327-1bed-4ffGPmeNchPbrTtBNJT1yqczXT_5RPMzxuaRET2irzZavLOnbyhEILAiH_SfbRfnSt8gA; _shibstate_1761107688_06bd=https%3A%2F%2Fuscdirectory.usc.edu%2Fweb%2Fdirectory%2Fstudent%2F; cf_clearance=xlgENcTR5E21yCoZLAQwOdJ46abiatGvEf314vlDLDE-1761108020-1.2.1.1-BmWu1rsrKtpXbLHcXnUeyBcEE_Ayd6fic4xUaEut4IZiubhEigYOf5D7cFqcCKzXhCh8wdUygQ7G84uSDomFuSmjxNlpqDertC_riKcEfDP8t.Hb0cf2Is5PkWIS_nUWj5VuvzTjV2Xozhy7qu3hNt2GmZ90QmXrlMgamXN4ZqsFFHpqsJ0gXRBYxGEK8vB9uOLkACI11ftR2uknsCqqnQ2VgcM2LslFmacFf9VcZZM',
}

params = {
    'basic': 'aar',
}

response = requests.get(
    'https://uscdirectory.usc.edu/web/directory/faculty-staff/proxy.php',
    params=params,
    cookies=cookies,
    headers=headers,
)

resp = response
print("Status:", resp.status_code)
print("Content-Type:", resp.headers.get("Content-Type"))
print("Length:", len(resp.text))
# print("First 500 chars:\n", resp.json())
