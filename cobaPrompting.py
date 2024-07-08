from gpt4all import GPT4All
import time
import pprint

print("Hello-GPT")
#model = GPT4All(model_name="mistral-7b-openorca.Q4_0.gguf",model_path="/Users/iswbprasetya/workshop/tools/gpt4allStuffs/gpt4all")
start_time = time.time()
#model = GPT4All(model_name="mistral-7b-openorca.Q4_0.gguf",model_path=".")
model = GPT4All(model_name="mistral-7b-openorca.Q4_0.gguf",model_path="c:/apps/gpt4all/models",device="cpu")
#model = GPT4All(model_name="orca-mini-3b-gguf2-q4_0.gguf",model_path="c:/apps/gpt4all/models",device="gpu")
print("** loading time:  %s s" % (time.time() - start_time))
#model = GPT4All(model_name="starcoder-q4_0.gguf",model_path="/Users/iswbprasetya/workshop/tools/gpt4allStuffs/gpt4all")
print(model.list_gpus())

start_time = time.time()
with model.chat_session(system_prompt="You are an AI assistant. Answer shortly. Do NOT add explanation. Do NOT add examples."):
    print(model.generate(prompt="USER: Suppose x = 10", max_tokens=400))
    print(model.generate(prompt="USER: Suppose y = 3", max_tokens=400))
    print(model.generate(prompt="USER: What is 2*x + y ? ASSISTANT: ", max_tokens=400))
    pprint.pprint(model.current_chat_session)

# output = model.generate("A chat. USER: Can you write a Python assertion that checks that x is always positive or x is odd", max_tokens=300)
#output = model.generate("A chat. USER: Can you write Python assertion? ASSISTANT: ", max_tokens=300, temp=0)
#print(output)
#print(model.current_chat_session)

print("** inference time:  %s s" % (time.time() - start_time))
