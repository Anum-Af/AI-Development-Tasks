from openai import AsyncOpenAI
import tiktoken


class Chatclient:
    def __init__(self, api_key, base_url, model_id, input_price=0.0, output_price=0.0):
        self.messages = [
            {'role': 'developer',
             'content': 'you are a helpful python tutor'}
        ]
        self.client = AsyncOpenAI(
            api_key=api_key, 
            base_url=base_url,
        )
        self.model_id = model_id
        self.encoding = tiktoken.get_encoding("cl100k_base")

        self.input_price = input_price
        self.output_price = output_price

        self.total_cost = 0.0

    def count_tokens(self, text):
        token = self.encoding.encode(text)
        return len(token)
    
    def count_message_token(self):
        total = ""
        for message in self.messages:
            content = message.get('content')
            if content:
                token = self.count_tokens(content)
                total += token
        return total

    def calculate_cost(self, input_token, output_token):
        input_cost  = input_token * self.input_price / 1_000_000
        output_cost = output_token * self.output_price / 1_000_000
        cost = input_cost + output_cost
        self.total_cost += cost
        return cost

    async def send_message(self, user_input):
        self.messages.append({
            'role': 'user',
            'content': user_input
        })
        response = await self.client.chat.completions.create(
            model=self.model_id,
            messages=self.messages
        )
        answer = response.choices[0].message.content
        self.messages.append({
            'role': 'assistant',
            'content': answer
        })

        usage = response.usage
        if usage:
            cost = self.count_message_token(
                usage.prompt_tokens,
                usage.completion_tokens
            )
            print("\nInput tokens:", usage.prompt_tokens)
            print("Output tokens:", usage.completion_tokens)
            print("Request cost:", cost)

        return response

    async def stream_response(self, user_input):
        self.messages.append({
            'role': 'user',
            'content': user_input
        })

        stream_response = await self.client.chat.completions.create(
            model=self.model_id,
            messages=self.messages,
            stream=True
        )
        answer = ""
        async for chunk in stream_response:
            content = chunk.choices[0].delta.content
            if content:
                answer += content
                print(content)
        self.messages.append({
            'role': 'assistant',
            'content': answer
        })
        return answer

    async def close(self):
        await self.client.close()


