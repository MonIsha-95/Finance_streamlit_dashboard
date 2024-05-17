
import openai
import pandas as pd
import json


openai.api_key ="sk-proj-VVsiQ0DlsaiMuOH0IlSlT3BlbkFJz9Cii9HHa6g2Y9Ml5C5j"
def extract_info(text):
    prompt = get_prompt()+text
    response = openai.Completion.create(
        model = 'gpt-3.5 turbo',
        message=[{'role':'user','content':'prompt'}]
        
    )
    content = response.choices[0]['message']['content']
    
    try:
        data = json.loads(content)
        return pd.DataFrame(data.items(),columns=["Measure","Value"])
    except(json.JSONDecodeError,IndexError):
        pass
    
        
    return pd.DataFrame({
    "Measure":["Comapny Name","Stock Symbol","Revenue","Net Income","EPS"],
    "Value":["","","","",""]})

def get_prompt():
     return '''Please retrieve company name, revenue, net income and earnings per share (a.k.a. EPS)
    from the following news article. If you can't find the information from this article 
    then return "". Do not make things up.    
    Then retrieve a stock symbol corresponding to that company. For this you can use
    your general knowledge (it doesn't have to be from this article). Always return your
    response as a valid JSON string. The format of that string should be this, 
    {
        "Company Name": "Walmart",
        "Stock Symbol": "WMT",
        "Revenue": "12.34 million",
        "Net Income": "34.78 million",
        "EPS": "2.1 $"
    }
    News Article:
    ============

    '''

if __name__ =='__main__':
    text='''
        Tesla's Earning news in text format: Tesla's earning this quarter blew all the estimates. They reported 4.5 billion $ profit against a revenue of 30 billion $. Their earnings per share was 2.3 $
    '''
    df = extract_info(text)
    print(df.to_string)
    