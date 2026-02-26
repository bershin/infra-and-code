# fine_tune_gpt2_dialogue.py

# Step 1: Import Libraries
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from transformers import Trainer, TrainingArguments
from datasets import load_dataset

# Step 2: Load Pre-trained GPT-2 Model and Tokenizer
model_name = "gpt2"  # You can also use "gpt2-medium", "gpt2-large" depending on your system
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Adjust tokenizer
tokenizer.pad_token = tokenizer.eos_token

# Step 3: Load and Preprocess the Dataset
dataset = load_dataset("daily_dialog")
train_data = dataset['train']
valid_data = dataset['validation']

# Tokenize function
def tokenize_function(examples):
    return tokenizer(examples['dialogue'], padding="max_length", truncation=True)

# Apply tokenization
train_data = train_data.map(tokenize_function, batched=True)
valid_data = valid_data.map(tokenize_function, batched=True)

# Format data for PyTorch
train_data.set_format(type='torch', columns=['input_ids', 'attention_mask'])
valid_data.set_format(type='torch', columns=['input_ids', 'attention_mask'])

# Step 4: Set Training Arguments and Fine-tune the Model
training_args = TrainingArguments(
    output_dir="./gpt2-dialogue",
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    num_train_epochs=3,  # Adjust based on your resources and needs
    logging_dir="./logs",
    save_total_limit=2,
    evaluation_strategy="epoch",  # Evaluation after each epoch
    learning_rate=5e-5,  # Low learning rate to retain GPT-2's pre-trained knowledge
    weight_decay=0.01,
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_data,
    eval_dataset=valid_data,
)

# Step 5: Fine-tune the Model
trainer.train()

# Step 6: Save the Model
trainer.save_model("./gpt2-dialogue-finetuned")

# Evaluate the Model
eval_results = trainer.evaluate()
print(f"Evaluation Results: {eval_results}")

# Step 7: Generate Dialogues
prompt = "Hello! How are you doing today?"
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# Generate response
output = model.generate(input_ids, max_length=100, num_return_sequences=1, pad_token_id=tokenizer.eos_token)
response = tokenizer.decode(output[0], skip_special_tokens=True)

# Print the generated dialogue
print(f"Generated Dialogue: {response}")
