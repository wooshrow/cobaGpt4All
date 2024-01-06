from gpt4all import GPT4All
import time
print("Hello-GPT")
#model = GPT4All(model_name="mistral-7b-openorca.Q4_0.gguf",model_path="/Users/iswbprasetya/workshop/tools/gpt4allStuffs/gpt4all")
start_time = time.time()
model = GPT4All(model_name="mistral-7b-openorca.Q4_0.gguf",model_path=".")
print("** loading time:  %s s" % (time.time() - start_time))
#model = GPT4All(model_name="starcoder-q4_0.gguf",model_path="/Users/iswbprasetya/workshop/tools/gpt4allStuffs/gpt4all")
start_time = time.time()
with model.chat_session():
    #response1 = model.generate(prompt='write a Python assertion that checks if x is positive', temp=0.5)
    #response1 = model.generate(prompt='def is_positive_and_even(x): ', temp=0.5)
    response1 = model.generate(prompt='You are given an array azr of integers, check if it is monotonic or not. If the array is monotonic, then return 101, else return -13. An array is monotonic if it is either monotonically increasing or monotonocally decreasing. An array is monotonically increasing/decreasing if its elements increase/decrease as we move from left to right', temp=0.5, max_tokens=300)
    #response2 = model.generate(prompt='thank you', temp=0)
    print(model.current_chat_session)

# output = model.generate("A chat. USER: Can you write a Python assertion that checks that x is always positive or x is odd", max_tokens=300)
#output = model.generate("A chat. USER: Can you write Python assertion? ASSISTANT: ", max_tokens=300, temp=0)
#print(output)
#print(model.current_chat_session)

print("** inference time:  %s s" % (time.time() - start_time))
