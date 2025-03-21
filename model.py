import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

model_name = "mistralai/Mistral-7B-v0.1"

# Load model in 4-bit
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True, 
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,  
    bnb_4bit_quant_type="nf4"
)

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    quantization_config=quantization_config
)

def generate_summary(text):
    """Summary generation"""
    inputs = tokenizer(text, return_tensors="pt").to("cuda")
    output = model.generate(**inputs, max_length=300)
    return tokenizer.decode(output[0], skip_special_tokens=True)