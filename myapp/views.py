from django.shortcuts import render
import requests
import json
def home(request):
    data = request.POST.get('name')
    
    url = "https://docker.api.srifintech.com/testassignment"

    if (data==None):
        data = "RELIANCE"

    payload = json.dumps({
    "ticker": data
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response)
    vari = response.json()
    context = {'data':data,  "strike": vari['strike'], "calloi": vari['calloi'], "putoi":vari['putoi']}
    return render(request, 'myapp/home.html', context)

