import streamlit as stl
import os
import json
import requests
from dotenv import load_dotenv
from langchain_community.llms import HuggingFaceEndpoint
##pip install dotenv
# pip install langchain_community
stl.title("Welcome To Rahul's GPT")
output="";

try:
    load_dotenv("E:\\pyhton\\.env");
  #  stl.write("Fine");
except:
    print("Env file not found !!!Provide the .env file for getting the param value");
 #   stl.write("Not Fine!!!!");


#stl.write(os.getenv('Name'));

#stl.write(os.getenv('HUGGINGFACE_API_KEY'))


models=['mistralai/Mistral-7B-Instruct-v0.3',
       'google/flan-t5-xxl',
       'tiiuae/falcon-40b-instruct','deepseek-ai/DeepSeek-V4-Pro']

model_id=stl.sidebar.selectbox('select Model' , options=tuple(models));

#stl.write(stl.session_state)

#if'model-response' not in stl.session_state:
#    stl.session_state['model-response']='<provide query and click on Invoke to get the response>';

if 'output' not in stl.session_state:
    stl.session_state.output="";
query=stl.text_area('Query',placeholder='Input your Query Here');
response_box=stl.empty();

temp=stl.sidebar.slider('Temperature',min_value=0.0,max_value=1.0);

topP=stl.sidebar.slider(label='Top-P',min_value=0.0,max_value=1.0,value=0.01);

topK=stl.sidebar.slider(label='Top-K',min_value=1,max_value=50,value=10);

repetition_penalty=stl.sidebar.slider('Repetition_penalty',min_value=0.0,max_value=5.0,value=1.0);

max_tokens=stl.sidebar.number_input('Max Tokens',value=50);


stl.sidebar.button('Reset');

#stl.write("You selected Temp value = ",temp);
#stl.write("You selected Top-P value = ",topP);
#stl.write("You selected Top-K value = ",topK);
#stl.write("You selected repetition penalty value = ",repetition_penalty);
#stl.write("You selected Number of Tokens = ",max_tokens);

#def invoke():
#    headers = {
#        "Authorization":f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"
#    }
#    data={
#        "inputs":query,
#        "parameters":{
#            "temperature":temp,
#            "top_k":topK,
#            "top_p":topP,
#            "repetition_penalty":repetition_penalty,
#            "max_new_tokens":max_tokens
#        }
#    }


def invoke():
    response_box = stl.empty()
    payload = {
        "model": "mistral",
        "prompt": query,
    }
   # stl.write("Your model Id = ",model_id);

    #url=f"https://api-inference.huggingface.co/models/{model_id}";
   # url=f"https://huggingface.co/{model_id}";
    url = "http://localhost:11434/api/generate"
    #stl.write("Final url :",url);
    with stl.spinner('Invoking LLm ....'):
        response=requests.post(url,json=payload,stream=True)
        
        if response.status_code==200:
            if "output" not in stl.session_state:
                stl.session_state.output = ""

            response_box = stl.empty()  # placeholder
          #  stl.write(response.text);
            #result=response.json()
            #stl.session_state['model-response']=response.json().get("generated text","No response");
            for idx,line in enumerate(response.iter_lines()):
                if line:
                    data = json.loads(line.decode("utf-8"))
                    if "response" in data:
                        #global output
                        stl.session_state.output +=data["response"]
                        response_box.text_area('Response', value=stl.session_state.output, height=200,key=f"response_box_{idx}")
                    if data.get("done", False):
                        break
            response_box.text_area('Response', value=stl.session_state.output.strip(), height=200,key=f"response_box1") 
        else:
            stl.session_state.output = f"Error : {response.status_code} - {response.text}"
            stl.text_area(
                'Response',
                value=stl.session_state.output,
                height=200,
                key="response_box"
            )
           
    response_box.text_area('Response', value=stl.session_state.output.strip(), height=200,key=f"response_box")

#response_box.text_area('Response', value=output, height=200,key=f"resp_final1")

stl.button('Invoke',on_click=invoke);




        