import asyncio
from typing import List, Dict
import openai
from config import api_key, base_url, MODEL_ID
from chat_client import Chatclient

async def main():
    chat = await Chatclient(api_key=api_key, base_url=base_url,
                            model_id=MODEL_ID)
    try:
        while True:
            user_input  = input("enter your qs: ")
            if user_input.lower() == 'exit':
                break

            response = await chat.send_message(user_input)
            print("final response: ", response)

    except openai.APIStatusError as e:
        print('error_details', e.response.text)

    except openai.APIConnectionError as e:
        print('error details', e.response.text)

    except openai.BadRequestError as e:
        print("Status:", e.status_code)
        print("Error details:", e.response.text)
        
    finally:

        await chat.close()

asyncio.run(main())

# messages = []
# async def stream_response(messages) -> str:
#     try:    
#         stream_response = await client.chat.completions.create(
#                 model=MODEL_ID,
#                 messages=messages, stream=True
#             )
#         response = ""
#         async for chunk in stream_response:
#             content = chunk.choices[0].delta.content
#             if content:
#                 # print("conetnt", content)
#                 response += content
#     except openai.BadRequestError as e:
#         print("Status:", e.status_code)
#         print("Error details:", e.response.text)

#     except openai.APIStatusError as e:
#         print("Status:", e.status_code)
#         print("Error details:", e.response.text)
#     # print("actual response is: ", response)
#     return response
#     # print(response.choices[0].message.content)
    

# async def main():
#     user_input  = input("enter your qs: ")
#     messages.append({'role': 'user', 'content': user_input})
#     response = await stream_response(messages)
#     print("final response: ", response)
# asyncio.run(main())