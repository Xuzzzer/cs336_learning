from cs335_basics.bpe import train_bpe

import os, time

def main():
    input_path = os.path.join("..", "data", "TinyStoriesV2-GPT4-train.txt")
    vocab_size = 10000
    special_tokens = ["<|endoftext|>"]
    
    start_time = time.perf_counter()
    vocab, merges = train_bpe(input_path, vocab_size, special_tokens)
    end_time = time.perf_counter()
    print(f"Training BPE took {end_time - start_time:.2f} seconds")