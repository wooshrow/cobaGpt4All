from gpt4all import GPT4All
import time
print("Hello-GPT")
start_time = time.time()
#model = GPT4All(model_name="mistral-7b-openorca.Q4_0.gguf",model_path="/Users/iswbprasetya/workshop/tools/gpt4allStuffs/gpt4all")
model = GPT4All(model_name="orca-mini-3b-gguf2-q4_0.gguf",
    model_path="/Users/iswbprasetya/workshop/tools/gpt4allStuffs/gpt4all",
    device='cpu')
#model = GPT4All(model_name="mistral-7b-openorca.Q4_0.gguf",model_path=".")
#model = GPT4All(model_name="starcoder-q4_0.gguf",model_path="/Users/iswbprasetya/workshop/tools/gpt4allStuffs/gpt4all")
print("** loading time:  %s s" % (time.time() - start_time))
start_time = time.time()
with model.chat_session(system_prompt="You are an AI assistant. Answer shortly. Do NOT explain. Do NOT add examples."):
    response1 = model.generate(prompt='USER: write the body of the following Python program.', temp=0.5)
    response2 = model.generate(prompt="""
    def checkPre(x: float, y: float) -> bool:
    \"\"\"
    Return true if x and y are non-negative.
    \"\"\"      
    """
    , temp=0.5, max_tokens=100),
    response3 = model.generate(prompt="""
    def checkPost(retval: float, x: float, y: float) -> bool:
    \"\"\"
    Return true if retval is the greatest of x and y.
    \"\"\"     
    """
    , temp=0.5, max_tokens=100),
    #response1 = model.generate(prompt='write a Python assertion that checks if x is positive', temp=0.5)
    #response1 = model.generate(prompt='def is_positive_and_even(x): ', temp=0.5)
    #response1 = model.generate(prompt='You are given an array azr of integers, check if it is monotonic or not. If the array is monotonic, then return 101, else return -13. An array is monotonic if it is either monotonically increasing or monotonocally decreasing. An array is monotonically increasing/decreasing if its elements increase/decrease as we move from left to right', temp=0.5, max_tokens=300)
    #response2 = model.generate(prompt='thank you', temp=0)
    print(model.current_chat_session)

# output = model.generate("A chat. USER: Can you write a Python assertion that checks that x is always positive or x is odd", max_tokens=300)
#output = model.generate("A chat. USER: Can you write Python assertion? ASSISTANT: ", max_tokens=300, temp=0)
#print(output)
#print(model.current_chat_session)

print("** inference time:  %s s" % (time.time() - start_time))
